from db.database_connection import conn, curr


recipe_table = "CREATE TABLE recipes (id INTEGER PRIMARY KEY , " \
                "name VARCHAR(100), " \
                "pre_time INTEGER CHECK (pre_time > 0), " \
                "difficulty INTEGER check (difficulty >= 0 AND difficulty <= 3), " \
                "vegetarian BOOLEAN)"

recipe_rating = "CREATE TABLE recipe_rating (id INTEGER PRIMARY KEY, " \
                "recipe_id INTEGER REFERENCES recipes, " \
                "rating INTEGER CHECK( rating >= 0 AND rating <= 5))"


#  Check if the tables exist. If not, create new recipe table
curr.execute("select exists(SELECT * FROM sqlite_master WHERE type=? AND name=?)", ('table', 'recipes',))
if curr.fetchone()[0]:
    pass
else:
    curr.execute(recipe_table)
    print("Sucess - Created Recipe table.")


#  Check if the tables exist. If not, create new recipe rating table
curr.execute("select exists(SELECT * FROM sqlite_master WHERE type=? AND name=?)", ('table', 'recipe_rating',))
if curr.fetchone()[0]:
    pass
else:
    curr.execute(recipe_rating)
    print("Sucess - Created Recipe rating table.")

    # Both tables were created and now 
    # add all the mock data to both tables
    sql_file = open("db/mock_data.sql")
    sql_as_string = sql_file.read()
    curr.executescript(sql_as_string)
    print("Sucess - Generated mock data for Recipe and Rating table.")

conn.commit()
