import sqlite3

from settings.settings import DATABASE

# Connect to our sqllite db (Create if it doesn't exist)
conn = sqlite3.connect(DATABASE)

# Open connection cursor for database operations
curr = conn.cursor()
