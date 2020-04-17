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

if __name__ == '__main__':
    unittest.main()