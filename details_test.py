from details import Details
import unittest 

class TestDetails(unittest.TestCase):
    
    def setUp(self):
    
        self.bb = Details("Naf","12345678") 

    def test_init(self):

        self.assertEqual(self.bb.username,"Naf")
        self.assertEqual(self.bb.password,"12345678")

    def test_save_details(self):

        self.bb.save_details() 
        self.assertEqual(len(Details.details_list),1)

    def test_find_contact_by_username(self):
        self.bb.save_details()
        test_details = Details("Naf","12345678") 
        test_details.save_details()
        found_details = Details.find_by_username("Naf")
        self.assertEqual(found_details.username, test_details.username)      
           
    def test_delete_credentials(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("James","123456") # new contact
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()# Deleting a contact object
            self.assertEqual(len(Credentials.credentials_list),1)
              