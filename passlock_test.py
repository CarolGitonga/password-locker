import unittest # Importing the unittest module
from passlock import User # Importing the user class

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the User class.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("CarolGitonga","Carol@15T")

    def test_init(self):
        """
        test_init test case to check if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username,"CarolGitonga")
        self.assertEqual(self.new_user.password,"Carol@15T")


if __name__ == '__main__':
    unittest.main()