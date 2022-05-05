import re
from servers.default_user import basic_auth_token
from servers.status import *
import recipes.views as views
from settings.responses import *

# Import off all endpoint functions
recipes = views.List()
recipe = views.Get()
create_recipe = views.Create()
update_recipe = views.Update()
delete_recipe = views.Delete()
recipe_rating = views.Rate()

# base64 encrypted token used to check header Authentication
auth_token = basic_auth_token()


def get_path(url, request, data=None, authentication=None):
    """
    Method is used to run the get and delete request functionality.
    This method manages List(), Get() and Delete() 
    with Basic authentication

    List(): Returns all Recipes
    Get(): Gets a single Recipes using id
    Delete(): Deletes a Recipes record using id

    :param: url
    :param: request
    :param: data
    :param: authentication

    :rtype: dict, Liteal
    """

    if request == 'GET':
        get_arg_id = re.findall("\d+", url)

        paths = [
            ('/recipes', recipes.get()),
        ]
        # If request has id arg, search for 
        # the single record if possible
        if get_arg_id:
            id = get_arg_id[0]
            paths = [
                ('/recipes/{}'.format(id), recipe.get(id=id)),
            ]

            if url == '/recipes/{}'.format(id):
                return paths[0][1].status, paths[0][1].data
            else:
                return HTTP_404_NOT_FOUND, URL_NOT_FOUND

        if url == '/recipes':
            return paths[0][1].status, paths[0][1].data
        else:
            return HTTP_404_NOT_FOUND, URL_NOT_FOUND

    
    elif request == 'DELETE':
        get_arg_id = re.findall("\d+", url)
        
        # Return UNAUTHORIZED if no Basic Authentication was sent
        if authentication is None:
            return HTTP_401_UNAUTHORIZED, UNAUTHORIZED

        elif authentication == 'Basic ' + str(auth_token):
            if get_arg_id:
                id = get_arg_id[0]
                paths = [
                    ('/recipes/{}'.format(id), delete_recipe.delete(id=id)),
                ]
                
                if url == '/recipes/{}'.format(id):
                    return paths[0][1].status, paths[0][1].data

                return HTTP_404_NOT_FOUND, URL_NOT_FOUND
            else:
                return HTTP_404_NOT_FOUND, URL_NOT_FOUND

        else:
            return HTTP_401_UNAUTHORIZED, UNAUTHORIZED


def post_path(url, request, data=None, authentication=None):
    """
    Method is used to run the post request functionality.
    This method manages Create() with Basic authentication 
    for new Recipes and Rating records

    Create(): Create new Recipe or Rating 
    depending on url request

    :param: url
    :param: request
    :param: data
    :param: authentication


    :rtype: dict, Liteal
    """

    if request == 'POST':

        get_arg_id = re.findall("\d+", url)

        # Return UNAUTHORIZED if no Basic Authentication was sent
        if authentication is None and url == '/recipes':
            return HTTP_401_UNAUTHORIZED, UNAUTHORIZED

        elif authentication == 'Basic ' + str(auth_token) and not get_arg_id:
            paths = [
                ('/recipes', create_recipe.post(data)),
            ]

            if url == '/recipes':
                return paths[0][1].status, paths[0][1].data
            else:
                return HTTP_404_NOT_FOUND, URL_NOT_FOUND

        elif get_arg_id and url == '/recipes/{}/rating'.format(get_arg_id[0]):
            id = get_arg_id[0]
            paths = [
                ('/recipes/{}/rating'.format(id), recipe_rating.post(data=data, id=id)),
            ]

            if url == '/recipes/{}/rating'.format(id):
                return paths[0][1].status, paths[0][1].data
            else:
                return HTTP_404_NOT_FOUND, URL_NOT_FOUND

        else:
            return HTTP_404_NOT_FOUND, URL_NOT_FOUND


def put_patch_path(url, request, data=None, authentication=None):
    """
    Method is used to run the patch/put request functionality.
    This method manages Update() with Basic authentication 
    for updating existing Recipes records

    Update(): Update an existing record of Recipe where 
    id is the same from request

    :param: url
    :param: request
    :param: data
    :param: authentication

    :rtype: dict, Liteal
    """

    if request == 'PUT' or request == 'PATCH':

        get_arg_id = re.findall("\d+", url)

        # Return UNAUTHORIZED if no Basic Authentication was sent
        if authentication is None:
            return HTTP_401_UNAUTHORIZED, UNAUTHORIZED

        elif authentication == 'Basic ' + str(auth_token):

            if get_arg_id:
                id = get_arg_id[0]
                paths = [
                    ('/recipes/{}'.format(id), update_recipe.post(data=data, id=id)),
                ]

                if url == '/recipes/{}'.format(id):
                    return paths[0][1].status, paths[0][1].data

                return HTTP_404_NOT_FOUND, URL_NOT_FOUND
            else:
                return HTTP_404_NOT_FOUND, URL_NOT_FOUND
        else:
            return HTTP_401_UNAUTHORIZED, UNAUTHORIZED