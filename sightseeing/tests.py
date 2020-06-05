from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client


#   tests will be added
class ReviewTestCase(TestCase):
    @classmethod
    def setUp(cls):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

        c = Client()
        cls.logged_in = c.login(username='testuser', password='12345')

    def test_logged(self):
        self.assertTrue(self.logged_in)
