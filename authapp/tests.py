from re import U
from django.test import TestCase
from .models import User

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(email="tomhollend@gmail.com",password="tomhollen@1234",username="Tom-hollen",role="seller")
    
    def test_user(self):
        userobj = User.objects.get(email="tomhollend@gmail.com")
        self.assertEqual(str(userobj),"tomhollend@gmail.com")
