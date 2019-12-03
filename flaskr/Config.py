import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'DEV'
    DATABASE_URL = os.environ.get('DATABASE_URL') or 'postgresql://postgres:vLfmVz@7O51P@dev.354thestars.com:5432/postgres'
    SMTP_HOST = 'smtp.sparkpostmail.com' # Placeholder
    SMTP_PORT = 587 # Placeholder
    SMTP_USERNAME = 'noreply@354thestars.com' # Placeholder
    SMTP_LOGIN = 'SMTP_Injection'
    #SMTP_PASSWORD = 'U0cuZkhpSVV1ZzlTcUNwcUVXRTNjdmtFZy5xTGlBclJQcElpMXROM25qTjFpZ241ODFPX0pSZ1VseGt6NWdOLXhXRDVZ'
    SMTP_PASSWORD = '83bd0e4c62092fc5f916a66c5cbf1086b1886eb2' # Placeholder
    SCHEMA_FOLDER = 'schemas'
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}