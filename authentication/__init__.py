from django.test import TestCase
from authentication.models import User

class TestSetup(TestCase):

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