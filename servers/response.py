import json

class Response:

    def __init__(self, status, data):
        """
        Sets class properties when 
        the class is created

        :param self:
        :param status:
        :param data:
        """
        self.status = status
        self.data = data

    
    def data_pass_with_status(self):
        """
        Returns response data in a serialized
        form with an appropriate status code

        :param self:
        :param status:
        :param data:
        """
        serializer = json.dumps(self.data)

        return serializer, self.status
