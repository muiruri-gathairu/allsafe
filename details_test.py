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
        