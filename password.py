import string
import random

class User:
    """
    Class for login details for the user in the app
    """
    users_list = []

    def __init__(self,first_name,last_name,password):
        """
        This function initializes user's details
        """

        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        """
        function to save user's details
        """
        User.users_list.append(self)

class Credentials:
    """
    Class that generates new instances of credentials
    """
    credentials_list = []

    def __init__(self,account_name,username,password):
        """
        This function initializes user's credentials
        """

        self.account_name = account_name
        self.username = username
        self.password = password