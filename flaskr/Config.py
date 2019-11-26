import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'DEV'
    DATABASE_URL = os.environ.get('DATABASE_URL') or 'postgresql://postgres:vLfmVz@7O51P@dev.354thestars.com:5432/postgres'
    SMTP_HOST = 'smtp.sendgrid.net' # Placeholder
    SMTP_PORT = 587 # Placeholder
    SMTP_USERNAME = 'noreply@354thestars.com' # Placeholder
    SMTP_LOGIN = 'apikey'
    SMTP_PASSWORD = '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' # Placeholder
    SCHEMA_FOLDER = 'schemas'
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}