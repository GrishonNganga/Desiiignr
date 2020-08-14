from django.test import TestCase
from django.contrib.auth.models import User
import os

from django.core.files.uploadedfile import SimpleUploadedFile

class Test_Profile(TestCase):
    def setUp(self):
        self.user = User.objects.create(username = 'kishy', email = 'kishy.gikish@gmail.com', password='123@Iiht')

    def test_user(self):
        users = list(User.objects.all())

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].id, 3)
        self.assertEqual(users[0].username, 'kishy')
        self.assertEqual(users[0].email, 'kishy.gikish@gmail.com')

    def test_profile_create(self):
        self.image = SimpleUploadedFile("file.jpg", b"file_content", content_type="image/jpg")
        self.user.profile.profile_image = self.image
        self.user.save()

        self.assertNotEqual(self.user.profile.profile_image, None )
        self.assertEqual(self.user.profile.profile_image.name, 'profiles/file.jpg')
        directory = os.getcwd() + '\media\profiles'
        
        os.remove(directory + '\\' + self.image.name)

    def test_post_create(self):
        self.image = SimpleUploadedFile("photo.jpg", b"file_content", content_type="image/jpg")
        self.user.post.post_image = self.image
        self.user.post.post_description = 'Oluwa Burna'
        self.user.save()

        self.assertNotEqual(self.user.post.post_image, None )
        self.assertEqual(self.user.post.post_image.name, 'posts/photo.jpg')
        self.assertEqual(self.user.post.post_description, 'Oluwa Burna')
        directory = os.getcwd() + '\media\posts'
        
        os.remove(directory + '\\' + self.image.name)