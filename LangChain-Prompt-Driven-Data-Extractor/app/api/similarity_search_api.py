from flask import Blueprint, request, jsonify
from app.services.google_drive_loader_service import GoogleDriveLoaderService
from app.document_loaders.embeddings import Embeddings
from app.services.google_drive_loader import GoogleDriveLoader
from app.document_loaders.vector_store import VectorStore
from app.config import Config
import json

# Create a Blueprint for similarity search
similarity_search_api = Blueprint('similarity_search_api', __name__)

@similarity_search_api.route('/similarity_search', methods=['POST'])
def similarity_search():
    global vectordb
    question = request.json['question']
    k = request.json.get('k', 5)

    if vectordb is not None:
        docs = vectordb.similarity_search(question, k=k)
        results = [{"document": doc.page_content} for doc in docs]
        return jsonify({"results": results})
    else:
        return jsonify({"error": "Vector database not initialized."})


@similarity_search_api.route('/similarity_search_with_score', methods=['POST'])
def similarity_search_with_score():
    global vectordb
    question = request.json['question']
    k = request.json.get('k', 5)

    if vectordb is not None:
        docs = vectordb.similarity_search_with_score(question, k=k)
        results = [{"document": doc[0].page_content, "score": doc[1]} for doc in docs]
        return jsonify({"results": results})
    else:
        return jsonify({"error": "Vector database not initialized."})


@similarity_search_api.route('/similarity_search_best_score', methods=['POST'])
def similarity_search_best_score():
    global vectordb
    question = request.json['question']
    k = request.json.get('k', 5)

    if vectordb is not None:
        docs = vectordb.similarity_search_with_score(question, k=k)
        min_score_result = min(docs, key=lambda x: x[1])
        result_item = {
            "document": min_score_result[0].page_content,
            "score": min_score_result[1]
        }
        return jsonify({"result": result_item})
    else:
        return jsonify({"error": "Vector database not initialized."})

@similarity_search_api.route('/get_shortlisted_doc', methods=['POST'])
def get_shortlisted_doc():
    try:
        # global vectordb

        # Get the JSON data from the request
        data = request.get_json()
        # Ensure that the data contains the expected keys
        if 'question' not in data or 'username' not in data or 'files' not in data:
            return jsonify(
                {'error': 'Invalid JSON data format. Expecting "question," "username," and "files" keys'}), 400

        # Extract the values from the JSON data
        question = data['question']
        username = data['username']
        files = data['files']

        gdl_instance = GoogleDriveLoader()
        docs = gdl_instance.load_documents_from_list(json.loads(files), username)
        embedding = Embeddings().get_openai_embedding()
        persist_directory = 'docs/chroma/'+username+"/"
        vectordb_internal = VectorStore().load_and_create_vector_store(embedding, persist_directory, documents=docs)

        docs = vectordb_internal.similarity_search_with_score(question, k=5)
        min_score_result = min(docs, key=lambda x: x[1])
        result_item = {
            "document": min_score_result[0].page_content,
            "score": min_score_result[1]
        }
        return jsonify({"result": result_item})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@similarity_search_api.route('/get_documents', methods=['GET'])
def get_documents():
    global vectordb

    if vectordb is not None:
        documents = vectordb.get()
        return jsonify({"documents": documents})
    else:
        return jsonify({"error": "Vector database not initialized."})