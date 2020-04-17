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

if __name__ == '__main__':
    unittest.main()