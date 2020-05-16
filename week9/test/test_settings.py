import unittest
from connector import DB_connection


class Tests(unittest.TestCase):
    def test_connection(self):
       self.assertIsNotNone(DB_connection())
    
    #def test_pathing(self):
    #    img = "dope"
    #    self.assertIsNotNone(os_parse_path(img))
