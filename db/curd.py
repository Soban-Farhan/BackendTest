from db.database_connection import conn, curr
from settings.responses import *


def fetch_all_recipes_query():
    """
    Method is used to fetch all recipes record from 
    table recipes with average of all recipes rating

    :rtype: list
    """

    curr.execute(
        "SELECT recipes.id, name, pre_time, difficulty, vegetarian, ROUND(AVG(rating),2) "
        "FROM recipes LEFT JOIN recipe_rating ON recipe_id=recipes.id GROUP BY recipes.id ORDER BY recipes.id ASC")

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
    """
    Creates a new recipe record using the request data 
    sent from postman

    :param data:
    :rtype: dict, Liteal
    """

    curr.execute("INSERT INTO recipes (name, pre_time, difficulty, vegetarian) VALUES (?, ?, ?, ?)",
               (data['name'], data['pre_time'], data['difficulty'], data['vegetarian'],))
    conn.commit()

    status = 201
    return RECIPE_CREATED, status


def update_recipe_query(data):
    """
    Updates all fields of recipes row where the 
    provided id matches.

    :param data:
    :rtype: dict, Liteal
    """

    curr.execute("UPDATE recipes SET name=?, pre_time=?, difficulty=?, vegetarian=? WHERE id=?",
                    (data['name'], data['pre_time'], data['difficulty'], data['vegetarian'], data['id']))
    conn.commit()

    status = 200
    return RECIPE_UPDATED, status


def delete_recipe_query(data):
    """
    Deletes an existing record from db where the 
    provided id matches.

    :param data:
    :rtype: dict, Liteal
    """

    recipes = fetch_all_recipes_query()
    for recipe in recipes:
        if recipe['id'] == int(data['id']):
            curr.execute("DELETE FROM recipes where id=?", (data['id'],))
            conn.commit()
            status = 200
            return RECIPE_DELETED, status

    status = 400
    return DATA_NOT_FOUND, status


def recipe_rating_query(data):
    """
    Creates a new rating record using request data 
    for an existing parent recipe record 

    :param data:
    :rtype: dict, Liteal
    """

    recipes = fetch_all_recipes_query()
    for recipe in recipes:
        if recipe['id'] == int(data['id']):
            curr.execute("INSERT INTO recipe_rating (recipe_id, rating) VALUES (?, ?)", (data['id'], data['rating']))
            conn.commit()
            status = 201
            return RECIPE_RATING, status

    status = 400
    return DATA_NOT_FOUND, status
