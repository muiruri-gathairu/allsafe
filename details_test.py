import unittest 
from details import Details

class TestDetails(unittest.TestCase):
    
    def setUp(self):
    
        self.bb = Details("Naf","12345678") 

    def test_init(self):

        self.assertEqual(self.bb.username,"Naf")
        self.assertEqual(self.bb.password,"12345678")

