from app.models.document import Document
from app.services.google_drive_loader import GoogleDriveLoader  # Import your existing GoogleDriveLoader class

class GoogleDriveLoaderService:
    # def init_app(app):
        # Initialize or configure your Google Drive service here
        # For example, set up routes or register blueprints specific to this service
        # You might also load configuration from app.config if needed
        # app.register_blueprint("google_drive_api")

    def load_from_google_drive(self, username):
        gdl_instance = GoogleDriveLoader()

        # Load documents from Google Drive using the existing class
        docs = gdl_instance.load(username)

        return [Document(page_content=doc.page_content, metadata=doc.metadata) for doc in docs]
