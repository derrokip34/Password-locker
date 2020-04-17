import unittest
from password import User, Credentials

class TestUser(unittest.TestCase):
    """
    This class tests the behaviour of User class
    """

    def setUp(self):
        """
        Setup method to run before each test
        """

        self.new_user = User("Derrick","Kiprop","enkay2008")

    def test_init(self):
        """
        Test if the object is correctly initialized
        """

        self.assertEqual(self.new_user.first_name,"Derrick")
        self.assertEqual(self.new_user.last_name,"Kiprop")
        self.assertEqual(self.new_user.password,"enkay2008")

    def test_save_user(self):
        """
        test to see if a user is saved to a users_list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run
        """
        User.users_list = []

    def test_save_multiple_user(self):
        """
        test to see if we can save multiple users to users_list
        """
        self.new_user.save_user()
        test_user = User("Derrick","Kiprop","enkay2008")
        test_user.save_user()
        self.assertEqual(len(User.users_list),2)

    def test_delete_user(self):
        """
        test to see if we can delete a user from users_list
        """
        self.new_user.save_user()
        test_user = User("Derrick","Kiprop","enkay2008")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.users_list),1)

class TestCredentials(unittest.TestCase):
    """
    Class that tests behaviour of credentials class
    """
    
    def setUp(self):
        """
        setup method that defines instructions
        """
        self.new_credentials = Credentials("Rockstar games","orred34","montolivo18")

    def test_init(self):
        """
        test to see if credentials object is initialized correctly
        """
        self.assertEqual(self.new_credentials.account_name,"Rockstar games")
        self.assertEqual(self.new_credentials.username,"orred34")
        self.assertEqual(self.new_credentials.account_password,"montolivo18")

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run
        """
        Credentials.credentials_list = []

    def test_save_credentials(self):
        """
        test to see if a contact is saved 
        """
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
        """
        test for saving multiple contacts
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Marvel","Derrick","enkay2008")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_view_credentials(self):
        """
        test to view account credentials
        """
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == '__main__':
    unittest.main()