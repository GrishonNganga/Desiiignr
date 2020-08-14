from django.test import TestCase
from django.contrib.auth.models import User

import mock
from django.core.files import File


class Test_Profile(TestCase):
    def setUp(self):
        self.user = User.objects.create(username = 'kishy', email = 'kishy.gikish@gmail.com', password='123@Iiht')

    def test_user(self):
        users = list(User.objects.all())

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].id, 2)
        self.assertEqual(users[0].username, 'kishy')
        self.assertEqual(users[0].email, 'kishy.gikish@gmail.com')

    def test_profile_create(self):
        file_mock = mock.MagicMock(spec=File, name='FileMock')
        self.user.profile_image = file_mock

        users = list(User.objects.all())

        self.assertNotEqual(users[0].profile.profile_image, None)