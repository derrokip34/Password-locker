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

    def delete_user(self):
        """
        method that deletes a user
        """
        User.users_list.remove(self)

class Credentials:
    """
    Class that generates new instances of credentials
    """
    credentials_list = []

    def __init__(self,account_name,username,account_password):
        """
        This function initializes user's credentials
        """

        self.account_name = account_name
        self.username = username
        self.account_password = account_password

    def save_credentials(self):
        """
        save credentials object onto credentials list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        function to delete credentials
        """
        Credentials.credentials_list.remove(self)

    
    @classmethod
    def display_credentials(cls):
        """
        function to display account credentials
        """
        return cls.credentials_list

    @classmethod
    def generate_password(stringLength = 10):
        """
        function that will generate a random password
        """
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
        size = 8
        return ''.join(random.choice(chars) for x in range(size,15))

    @classmethod
    def find_by_name(cls,name):
        """
        function that finds an account object by name
        """
        for account in cls.credentials_list:
            if account.account_name == name:
                return account