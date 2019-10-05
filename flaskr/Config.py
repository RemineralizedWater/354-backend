import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'DEV'
    DATABASE_URL = os.environ.get('DATABASE_URL') or ''
    SMTP_HOST = 'smtp.mailgun.org' # Placeholder
    SMTP_PORT = 587 # Placeholder
    SMTP_USERNAME = 'postmaster@sandboxf55aa089a27a4ed686e941fee0ddd632.mailgun.org' # Placeholder
    SMTP_PASSWORD = 'f85b0f946e0c2262f9f6be0cfa99bd9d-b892f62e-6a855db0' # Placeholder