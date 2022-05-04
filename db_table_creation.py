from db.database_connection import conn, curr


recipe_table = "CREATE TABLE recipes (id serial PRIMARY KEY , " \
                "name VARCHAR(100), " \
                "pre_time INTEGER CHECK (pre_time > 0), " \
                "difficulty INTEGER check (difficulty > 0 AND difficulty < 5), " \
                "vegetarian BOOLEAN)"

recipe_rating = "CREATE TABLE recipe_rating (id serial PRIMARY KEY, " \
                "recipe_id INTEGER REFERENCES recipes, " \
                "rating INTEGER CHECK( rating > 0 AND rating < 5))"


#  Check if the tables exist. If not, create new recipe table
curr.execute("select exists(SELECT * FROM sqlite_master WHERE type=? AND name=?)", ('table', 'recipes',))
if curr.fetchone()[0]:
    pass
else:
    curr.execute(recipe_table)



#  Check if the tables exist. If not, create new recipe rating table
curr.execute("select exists(SELECT * FROM sqlite_master WHERE type=? AND name=?)", ('table', 'recipe_rating',))
if curr.fetchone()[0]:
    pass
else:
    curr.execute(recipe_rating)

conn.commit()
