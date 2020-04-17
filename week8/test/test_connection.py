import unittest
from connector import DB_connection


class TestConnection(unittest.TestCase):
    def test_local_connection(self):
        cnx = DB_connection()
        self.assertIsNotNone(cnx)
        cnx.close()
