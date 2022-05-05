class RecipeValidator:

    def __init__(self, data):
        """
        Create a parameterized constructor and 
        assign request data for validation processing 

        :param: self
        :param: data
        """
        self.errors, self.valid = self.validate_recipe_data(data)


    def validate_recipe_data(self, data):
        """
        Validate the request body to see if the 
        inputs are valid types and in valid range

        :param: self
        :param: data

        :rtype: list, bool
        """

        errors = []
        valid = False
        
        # Validate if the required key are in request body
        recipe_body_keys = ["name", "pre_time", "difficulty", "vegetarian"]
        for key in recipe_body_keys:
            if key not in data:
                errors.append(
                    {
                        "error": "'%s' key was not found in request body." % (key)
                    }
                )
                return errors, valid

        # Validate 'name' key from request body
        if data["name"] == "" or len(data["name"]) > 100:
            errors.append(
                {
                    "error": "'name' key cannot be empty or be more than 100 characters."
                }
            )
            return errors, valid

        # Validate 'pre_time' key from request body
        if not isinstance(data["pre_time"], int):
            errors.append(
                {
                    "error": "'pre_time' key needs to be a whole number."
                }
            )
            return errors, valid

        elif int(data["pre_time"]) <= 0:
            errors.append(
                {
                    "error": "'pre_time' key cannot be less than or equal to 0."
                }
            )
            return errors, valid

        # Validate 'difficulty' key from request body
        if not isinstance(data["difficulty"], int):
            errors.append(
                {
                    "error": "'difficulty' key needs to be a whole number."
                }
            )
            return errors, valid
        
        elif data["difficulty"] < 1 or data["difficulty"] > 3:
            errors.append(
                {
                    "error": "'difficulty' key cannot be less than 1 or greater than 3."
                }
            )
            return errors, valid

        # Validate 'vegetarian' key from request body
        if not isinstance(data["vegetarian"], bool):
            errors.append(
                {
                    "error": "'vegetarian' key needs to be a boolean value."
                }
            )
            return errors, valid

        # Check if there were any errors
        if not errors:
            valid = True

        return errors, valid
        

    def is_valid(self):
        """
        returns valid class property

        :param: self

        :rtype: bool
        """
        return self.valid

class RatingValidator:

    def __init__(self, data):
        """
        Create a parameterized constructor and 
        assign request data for validation processing 

        :param: self
        :param: data
        """

        self.errors, self.valid = self.validate_rating_data(data)


    def validate_rating_data(self, data):
        """
        Validate the request body to see if the 
        inputs are valid types and in valid range

        :param: self
        :param: data

        :rtype: list, bool
        """

        errors = []
        valid = False
        
        # Validate if the required key are in request body
        rate_body_keys = ["rating"]
        for key in rate_body_keys:
            if key not in data:
                errors.append(
                    {
                        "error": "'%s' key was not found in request body." % (key)
                    }
                )
                return errors, valid

        # Validate 'rating' key from request body
        if not isinstance(data["rating"], int):
            errors.append(
                {
                    "error": "'rating' key needs to be a whole number."
                }
            )
            return errors, valid
        
        elif data["rating"] < 1 or data["rating"] > 5:
            errors.append(
                {
                    "error": "'rating' key cannot be less than 1 or greater than 5."
                }
            )
            return errors, valid

        # Check if there were any errors
        if not errors:
            valid = True

        return errors, valid

    def is_valid(self):
        """
        returns valid class property

        :param: self

        :rtype: bool
        """
        return self.valid