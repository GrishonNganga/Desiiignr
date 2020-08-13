from django.test import TestCase
from django.contrib.auth import get_user_model


class Test_Profile(TestCase):
    def setUp(self):
        User = get_user_model()
        user = list(User.objects.all())
        print(user)

    def test_profile(self):
        pass