import os

# Set base dir variable for later use
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__name__)))

# String of all allowed host from env
ALLOWED_HOSTS = 'localhost'
PORT = 5000

# Database settings
DATABASE = 'RecipeAPI.db'