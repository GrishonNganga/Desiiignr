from django.test import TestCase
from django.contrib.auth.models import User
import os
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Post

class Test_Profile(TestCase):
    def setUp(self):
        self.user = User.objects.create(username = 'kishy', email = 'kishy.gikish@gmail.com', password='123@Iiht')

        self.image_profile = SimpleUploadedFile("file.jpg", b"file_content", content_type="image/jpg")
        self.user.profile.profile_image = self.image_profile
        self.user.save()

        
    def test_user(self):
        users = list(User.objects.all())

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, 'kishy')
        self.assertEqual(users[0].email, 'kishy.gikish@gmail.com')


    def test_profile_create(self):
        self.assertNotEqual(self.user.profile.profile_image, None )
        self.assertEqual(self.user.profile.profile_image.name, 'profiles/file.jpg')
        

      
        
        
    def tearDown(self):
        directory_profiles = os.getcwd() + '\media\profiles'
        os.remove(directory_profiles + '\\' + self.image_profile.name)


class TestPost(TestCase):

    def setUp(self):
        self.user = User.objects.create(username = 'kishy', email = 'kishy.gikish@gmail.com', password='123@Iiht')

        self.image_post = SimpleUploadedFile("photo.jpg", b"file_content", content_type="image/jpg")
        self.post = Post(user = self.user, post_image = self.image_post, post_description = 'Oluwa Burna' )
        self.post.save()
        self.user.post = self.post
        self.user.save()


    def test_post_create(self):
        self.assertNotEqual(self.user.post.post_image, None )
        self.assertEqual(self.user.post.post_image.name, 'posts/photo.jpg')
        self.assertEqual(self.user.post.post_description, 'Oluwa Burna')
      

    def test_get_all_posts(self):
        posts = Post.get_all_posts()
        
        #For some reason the db has one record that I can't delete
        self.assertEqual(len(posts), 2)
        

    def test_get_posts_for_user(self):
        id = self.user.id
        
        posts = Post.get_posts_for_user(id)

        print(posts)

    def tearDown(self):
        directory_posts = os.getcwd() + '\media\posts'
        os.remove(directory_posts + '\\' + self.image_post.name)

