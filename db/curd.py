from db.database_connection import conn, curr

from settings.responses import *

def fetch_all_recipes_query():

    curr.execute(
        "SELECT recipes.id, name, pre_time, difficulty, vegetarian, ROUND(AVG(rating),2) "
        "FROM recipes LEFT JOIN recipe_rating ON recipe_id=id GROUP BY recipes.id ORDER BY id ASC")

    recipes = []
    for item in curr.fetchall():
        data = dict()
        data['id'] = item[0]
        data['name'] = item[1]
        data['pre_time'] = item[2]
        data['difficulty'] = item[3]
        data['vegetarian'] = item[4]
        data['average_rating'] = str(item[5])
        recipes.append(data)
    return recipes

def create_recipe_query(data):
    curr.execute("INSERT INTO recipes (name, pre_time, difficulty, vegetarian) VALUES (?, ?, ?, ?)",
               (data['name'], data['pre_time'], data['difficulty'], data['vegetarian'],))
    conn.commit()

    status_code = 201
    return RECIPE_CREATED, status_code


def update_recipe_query(data):
    curr.execute("UPDATE recipes SET name=?, pre_time=?, difficulty=?, vegetarian=?, WHERE id=?",
               (data['name'], data['pre_time'], data['difficulty'], data['vegetarian'], data['id']))
    conn.commit()

    status_code = 200
    return RECIPE_UPDATED, status_code


def delete_recipe_query(data):
    recipes = fetch_all_recipes_query()
    for recipe in recipes:
        if recipe['id'] == int(data['id']):
            curr.execute("DELETE FROM recipes where id=?", (data['id'],))
            conn.commit()
            status_code = 200
            return RECIPE_DELETED, status_code

    status_code = 400
    return DATA_NOT_FOUND, status_code


def recipe_rating_query(data):
    recipes = fetch_all_recipes_query()
    for recipe in recipes:
        if recipe['id'] == int(data['id']):
            curr.execute("INSERT INTO recipe_rating (recipe_id, rating) VALUES (?, ?)", (data['id'], data['rating']))
            conn.commit()
            status_code = 201
            return RECIPE_RATING, status_code

    status_code = 400
    return DATA_NOT_FOUND, status_code
