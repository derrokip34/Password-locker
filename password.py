import string
import random

class User:
    """
    Class for login details for the user in the app
    """
    users = []

    def __init__(self,first_name,last_name,password):
        """
        This function initializes user's details
        """

        self.first_name = first_name
        self.last_name = last_name
        self.password = password