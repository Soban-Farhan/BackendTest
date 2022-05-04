import os
from dotenv import load_dotenv

# Set base dir variable for later use
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__name__)))

# Load env file from root dir
load_dotenv()

# String of all allowed host from env
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS')

# Database settings
DATABASE = os.getenv('DATABASE_NAME')