from flask import Blueprint, request, jsonify
from app.services.google_drive_loader_service import GoogleDriveLoaderService

google_drive_api = Blueprint('google_drive_api', __name__)
loader_service = GoogleDriveLoaderService()

@google_drive_api.route('/load_gdrive', methods=['POST'])
def load_gdrive():
    try:
        # Extract and validate the request data
        data = request.get_json()
        username = data['username']

        # Call the service to load documents from Google Drive
        docs = loader_service.load_from_google_drive(username)

        return jsonify({"documents": [doc.to_dict() for doc in docs]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

