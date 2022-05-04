import os
from dotenv import load_dotenv

# Set base dir variable for later use
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__name__)))

# Load env file from root dir
load_dotenv()

# String of all allowed host from env
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS')

# Database settings
DATABASE = {
    "dbname": os.getenv('DATABASE_NAME'),
    "user": os.getenv('DATABASE_USERNAME'),
    "password": os.getenv('DATABASE_PASSWORD'),
    "host": os.getenv('DATABASE_HOST'),
    "port": os.getenv('DATABASE_PORT')
}