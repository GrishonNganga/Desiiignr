from django.test import TestCase
from django.contrib.auth.models import User
import os
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Post, Follower, Like, Profile, Comment

class Test_Profile(TestCase):
    def setUp(self):
        self.user = User.objects.create(username = 'kishy', email = 'kishy.gikish@gmail.com', password='123@Iiht')

        self.image_profile = SimpleUploadedFile("file.jpg", b"file_content", content_type="image/jpg")
        self.profile = Profile(user=self.user, profile_image = self.image_profile)
        self.profile.save()
        self.user.profile = self.profile
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
        
        self.assertEqual(len(posts), 1)
        

    def test_get_posts_for_user(self):
        id = self.user.id
        
        posts = Post.get_posts_for_user(id)

    def tearDown(self):
        directory_posts = os.getcwd() + '\media\posts'
        os.remove(directory_posts + '\\' + self.image_post.name)


class TestFollower(TestCase):
    def setUp(self):
        self.user = User.objects.create(username = 'kishy', email = 'kishy.gikish@gmail.com', password='123@Iiht')
        self.user2 = User.objects.create(username = 'Grish', email = 'grish@gmail.com', password='123@Iiht')
        
            
    def test_create_follower(self):
        self.follower = Follower(username= self.user2.username)
        self.follower.save()
        self.follower.user.add(self.user)
        self.assertEqual(len(Follower.objects.all()), 1)



class TestLike(TestCase):
    def setUp(self):
        self.user = User.objects.create(username = 'kishy', email = 'kishy.gikish@gmail.com', password='123@Iiht')

        self.image_post = SimpleUploadedFile("photo.jpg", b"file_content", content_type="image/jpg")
        self.post = Post(user = self.user, post_image = self.image_post, post_description = 'Oluwa Burna' )
        self.post.save()
        self.user.post = self.post
        self.user.save()
        
            
    def test_create_like(self):
        self.liker = Like(username= self.user.username)
        self.liker.save()
        self.liker.post.add(self.post)
        self.assertEqual(len(Like.objects.all()), 1)
        self.assertEqual(Like.objects.all()[0].username, 'kishy')

    
    def tearDown(self):
        directory_posts = os.getcwd() + '\media\posts'
        os.remove(directory_posts + '\\' + self.image_post.name)


class TestComment(TestCase):
    def setUp(self):
        self.user = User.objects.create(username = 'kishy', email = 'kishy.gikish@gmail.com', password='123@Iiht')

        self.image_post = SimpleUploadedFile("photo.jpg", b"file_content", content_type="image/jpg")
        self.post = Post(user = self.user, post_image = self.image_post, post_description = 'Oluwa Burna' )
        self.post.save()
        self.user.post = self.post
        self.user.save()
        
            
    def test_create_like(self):
        self.comment = Comment(username = self.user.username, comment= 'Wow that is a beautiful babe!')
        self.comment.save()
        self.comment.post.add(self.post)
        self.assertEqual(len(Comment.objects.all()), 1)
        self.assertEqual(Comment.objects.all()[0].username, 'kishy')
        self.assertEqual(Comment.objects.all()[0].comment, 'Wow that is a beautiful babe!')


    def tearDown(self):
        directory_posts = os.getcwd() + '\media\posts'
        os.remove(directory_posts + '\\' + self.image_post.name)