import base64

class TestAPIUser:

    # string property of TestAPIUser
    basic_token = ''

    def set_auth_token(self, username, password):
        """
        Method is used to set TestAPIUser token property 
        used for Basic Authentication

        :param: usernae
        :param: password
        :rtype: str
        """
        self.basic_token = base64.b64encode(
            bytes('%s:%s' % (username, password), 'utf-8')).decode('ascii')


    def get_auth_token(self):
        """
        Return a base64 encrypted token property
        :return: a string
        :rtype: str
        """
        return self.basic_token


def basic_auth_token():
    """
    Creates base64 encrypted token using user's 
    username and password.
    
    :return: base64 encrypted token
    :rtype: str
    """
    user = TestAPIUser()
    # username and password
    user.set_auth_token('test', 'password')
    return user.get_auth_token()

