import unittest # Importing the unittest module
from passlock import User # Importing the user class
from passlock import Credentials 

class TestClass(unittest.TestCase):

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

    def test_save_user(self):
        """
        test_save_user test case to test if a new user instance has been saved into the User list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
    """
    A test class that defines test cases for credentials class

    """ 
    def setUp(self):
        """
        Method that runs before each individual credentials test methods run.

        """
        self.new_credential = Credentials('Gmail','Carol_Gitonga','lorac@15G')
    def test_init(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credential.account,'Gmail')
        self.assertEqual(self.new_credential.userName,'Carol_Gitonga')
        self.assertEqual(self.new_credential.password,'lorac@15G')


if __name__ == '__main__':
    unittest.main()