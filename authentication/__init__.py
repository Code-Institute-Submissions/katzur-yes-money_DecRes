import unittest
from django.test import TestCase

class TestSetup(unittest.TestCase):

    def setUp(self):
        print('Test started')
        self.user = {
            "username": "username",
            "email": "email",
            "password": "password",
            "password2": "password"
        }
        

    def tearDown(self):
        print('Test finished')
        return super().tearDown()

unittest.main()