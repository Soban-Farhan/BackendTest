from db.curd import create_recipe_query, update_recipe_query, delete_recipe_query, recipe_rating_query, fetch_all_recipes_query
from servers.response import Response
from servers.status import *
from settings.responses import *
from recipes.validators import *

class List:
    
    def get(self):
        """
        Get all records for recipes with 
        child ratings as an average

        :param: self

        :rtype: Response(data, status)
        """
        data = fetch_all_recipes_query()
        return Response(data=data, status=HTTP_200_OK)

class Get:
    
    def get(self, id=None):
        """
        Get a single record of recipes with 
        child ratings as an average

        :param: self

        :rtype: Response(data, status)
        """
        recipes = fetch_all_recipes_query()
        return_data = []
        for recipe in recipes:
            if recipe['id'] == int(id):
                return_data.append(recipe)

        # Validate if there are any records to return
        if not return_data:
            return Response(data=[DATA_NOT_FOUND], status=HTTP_400_BAD_REQUEST)

        return Response(data=return_data, status=HTTP_200_OK)


class Create:

    def post(self, data):
        """
        Creates a new record of recipe

        :param: self
        :param: data

        :rtype: Response(data, status)
        """

        # Validate request data sent
        valid = RecipeValidator(data)
        if not valid.is_valid():
            return Response(data=valid.errors, status=HTTP_400_BAD_REQUEST)

        message, status = create_recipe_query(data=data)
        return Response(data=message, status=status)


class Update:
    
    def post(self, data, id=None):
        """
        Updates an existing record of recipe using data 
        and finding it using id

        :param: self
        :param: data
        :param: id

        :rtype: Response(data, status)
        """
        # Validate request data sent
        valid = RecipeValidator(data)
        if not valid.is_valid():
            return Response(data=valid.errors, status=HTTP_400_BAD_REQUEST)


        data['id'] = id
        message, status = update_recipe_query(data)
        return Response(data=message, status=status)


class Delete:

    def delete(self, id=None):
        """
        Deletes an existing record of recipe 
        by finding it using id

        :param: self
        :param: id

        :rtype: Response(data, status)
        """

        message, status = delete_recipe_query({ "id" : id })
        return Response(data=message, status=status)


class Rate:

    def post(self, data, id=None):
        """
        Creates a new rating record which will 
        be child record of recipe

        :param: self
        :param: data
        :param: id

        :rtype: Response(data, status)
        """

        # Validate request data sent
        valid = RatingValidator(data)
        if not valid.is_valid():
            return Response(data=valid.errors, status=HTTP_400_BAD_REQUEST)
        
        data['id'] = id
        message, status = recipe_rating_query(data=data)
        return Response(data=message, status=status)