from user import Users
from details import Details
import random
import unittest

class TestUser(unittest.TestCase):

    def setUp(self):
        
        self.aa = Users("Naf", "12345678") 

    def test_init(self):
        
        self.assertEqual(self.aa.username, "Naf")
        self.assertEqual(self.aa.password, "12345678")     

    def test_save_user(self):

        self.aa.login()
        self.assertEqual(len(Users.aa), 1)           

    def tearDown(self):

        Users.aa = []

    @classmethod
    def display_details(cls, username):

                users_details_list = []
                for detail in details.bb:
                     if detail.username == username:
                        users_details_list.append(detail)
                        return users_details_list


if __name__ == "__main__":
    unittest.main()
        

    