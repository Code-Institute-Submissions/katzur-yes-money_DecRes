from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
    def test_should_show_register_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/register.html")


    def test_should_show_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/login.html")


    def test_should_signup_user(self):
        self.user = {
            "username": "username",
            "email": "email@gmail.com",
            "password": "password"
        }

        response = self.client.post(reverse("register"), self.user)
        self.assertEqual(response_status_code, 302)


