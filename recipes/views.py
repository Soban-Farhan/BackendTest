from db.curd import create_recipe_query, update_recipe_query, delete_recipe_query, recipe_rating_query, fetch_all_recipes_query
from servers.response import Response
from servers import status

class List:

    def get(self):
        data = fetch_all_recipes_query()
        return Response(data=data, status=status.HTTP_200_OK)

class Get:

    def get(self, pk=None):
        recipes = fetch_all_recipes_query()
        return_data = []
        for recipe in recipes:
            if recipe['id'] == int(pk):
                return_data.append(recipe)
        return Response(data=return_data, status=status.HTTP_200_OK)


class Create:

    def post(self, data):
        message, status_code = create_recipe_query(data=data)
        return Response(data=message, status=status_code)


class Update:

    def post(self, data, pk=None):
        data['id'] = pk
        message, status_code = update_recipe_query(data)
        return Response(data=message, status=status_code)


class Delete:

    def delete(self, pk=None):
        message, status_code = delete_recipe_query({"id": pk})
        return Response(data=message, status=status_code)


class Rate:

    def post(self, data, pk=None):
        data['id'] = pk
        message, status_code = recipe_rating_query(data=data)
        return Response(data=message, status=status_code)