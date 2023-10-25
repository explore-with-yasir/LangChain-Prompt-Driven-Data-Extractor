class Config:
    import os

    # Flask Configuration
    DEBUG = True  # Set to False in production
    SECRET_KEY = 'your_secret_key'  # Replace with a strong, unique secret key

    # Google Drive Configuration
    GOOGLE_DRIVE_CREDENTIALS_PATH = '/path/to/credentials.json'  # Path to Google Drive API credentials file
    GOOGLE_DRIVE_TOKEN_PATH = '/path/to/token.json'  # Path to the token file
    GOOGLE_DRIVE_SERVICE_ACCOUNT_KEY = '/path/to/service_account_key.json'  # Path to the service account key file

    # Application-specific Configuration
    BASE_PATH = '/path/to/your/base/directory'  # Base directory for your application
    PERSIST_DIRECTORY = os.path.join(BASE_PATH, 'docs/chroma')  # Directory for storing documents

    # Additional Configuration Options
    # Add any other configuration options your application needs

    # Example Database Configuration (if using a database)
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///myapp.db'  # Example SQLite database URI

    # Logging Configuration (customize this as needed)
    # LOG_DIR = '/path/to/log/directory'
    # LOG_FILENAME = 'app.log'
    # LOG_LEVEL = 'INFO'

    # Add more configuration settings specific to your application as needed

    # Production Configuration (override the above settings in production)
    if os.environ.get('FLASK_ENV') == 'production':
        DEBUG = False
        # Override other settings for production environment

    # Development Configuration (override settings for development)
    if os.environ.get('FLASK_ENV') == 'development':
        DEBUG = True

    # Test Configuration (override settings for testing)
    if os.environ.get('FLASK_ENV') == 'test':
        DEBUG = True

