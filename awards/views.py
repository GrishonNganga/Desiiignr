from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
import json
import math

from .serializers import UsersSerialized, ProjectsSerialized

from .models import Profile, Post, Rate, Comment
User = get_user_model()

from .forms import RegisterUserForm, LoginUserForm

def registerPage(request):
    form = RegisterUserForm()

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'accounts/register.html', {'register_form': form})

def loginPage(request):
    form = LoginUserForm()
    if request.method == 'POST':
        pass
        email = request.POST.get('email')
        password = request.POST.get('password')
        email1 = request.POST.get('email1')
        password1 = request.POST.get('password1')
        user = None
        next = request.POST.get('next')

        if password != None and email != None:
            user_from_email = User.objects.filter(email = email)
            if user_from_email.exists():
                user_from_obj = list(user_from_email)[0]
                user_email = user_from_obj.email
                print(user_email)
                user = authenticate(request, username = user_from_obj.username, password = password)

        else:
            user_from_email = User.objects.filter(email = email1)
            if user_from_email.exists():
                user_from_obj = list(user_from_email)[0]
                user_email = user_from_obj.email
                print(user_email)
                user = authenticate(request, username = user_from_obj.username, password = password1)
        if user:
            login(request, user_from_obj)
            print('Login Success')

        
            print('Next is')
            print(next)
            if next:
                return redirect(next)
            else:
                return HttpResponseRedirect('/')
        else:
            return render(request, 'accounts/login.html', {'login_form': form, 'error': 'Error! Username or password is incorrect'})

        
        return redirect('/')


    return render(request, 'accounts/login.html', {'login_form': form})

def index(request):
    posts = Post.get_all_posts()
    print(posts)
    return render(request, 'index.html', {'posts': posts})



@login_required(login_url='/login')
def profile(request):
    if request.method == 'POST' and request.FILES.get('profile'):
        profile_image = request.FILES.get('profile')
        user = request.user
        profile = Profile(user=user, profile_image = profile_image)
        profile.save()
        user.profile = profile
        user.save()
        
    posts = Post.get_posts_for_user(request.user.id)
    posts_count = len(posts)
    return render(request, 'profile.html', {'posts': posts, 'posts_count': posts_count})



@login_required(login_url='/login')
def upload_pic(request):
    if request.method == 'POST':
        if request.FILES.get('upload'):
            post_image = request.FILES.get('upload')
            post_description = request.POST.get('description')

            user = request.user
            post = Post(user = user, post_description = post_description, post_image = post_image)
            post.save()
            user.post = post
            user.save()
            return redirect('/')
        else:
            return render(request, 'upload.html', {'error': 'Make sure you select an image'})
    else:
        return render(request, 'upload.html')



def show_post(request, post_id):
    post = Post.objects.get(id = post_id)
    rate_for_post_exists = Rate.objects.filter(post=post_id)
    no_of_rates = len(rate_for_post_exists)

    if no_of_rates != 0:
        a_users_avg_rate = 0
        total_rates = 0
        for rate in rate_for_post_exists:
            a_users_avg_rate = ((int(rate.usability) + int(rate.design) + int(rate.content)) / 30) * 100
            total_rates = a_users_avg_rate
        
        final_rating = math.floor(total_rates/ no_of_rates)
    else:
        final_rating = 0
    print(final_rating)
    return render(request, 'post.html', {'post': post, 'rating': final_rating})


# @login_required(login_url='/login')
# def follow_request(request):
#     if request.method =='POST':
#         if request.POST.get('follow'):
#             user_id = int(request.POST.get('follow'))
#             if isinstance(user_id, int):
#                 print(user_id)
#                 user_to_follow = User.objects.get(id = user_id)
#                 follow = Follower(username=user_to_follow.username)
#                 follow.save()
#                 follow.user.add(request.user)
#                 data = {'success': 'Successfully followed the user'}
#                 return JsonResponse(data)
#             else:
#                 data = {'fail': 'Something wrong happened.'}
#                 return JsonResponse(data)
                


@login_required(login_url='/login')
def vote_post(request, id):
    if request.method =='POST':
        if request.POST.get('design') and request.POST.get('usability') and request.POST.get('content'):
            design = request.POST.get('design')
            usability = request.POST.get('usability')
            content = request.POST.get('content')
            post_to_rate = Post.objects.get(id = id)
            rate_post = Rate(username=request.user.username, design = design, usability = usability, content= content)
            rate_post.save()
            rate_post.post.add(post_to_rate)
            data = {'success': 'Successfully rated the post'}
            return redirect('/post/{{ post_to_rate.id }}')
        else:
            data = {'fail': 'Something wrong happened.'}
            return redirect('/login')


class UsersList(APIView):
    def get(self, request, format=None):
        all_users = User.objects.all()
        serializers = UsersSerialized(all_users, many=True)
        return Response(serializers.data)




class ProjectsList(APIView):
    def get(self, request, format=None):
        all_posts = Post.objects.all()
        serializers = ProjectsSerialized(all_posts, many=True)
        return Response(serializers.data)


# @login_required(login_url='/login')
# def make_comment(request):
#     if request.method =='POST':
#         if request.POST.get('comment'):
#             post_id = int(request.POST.get('post'))
#             comment = request.POST.get('comment')
#         elif request.POST.get('comment-lg'):
#             post_id = int(request.POST.get('post-lg'))
#             comment = request.POST.get('comment-lg')
#         else:
#             data = {'fail': 'Something wrong happened.'}
#             return JsonResponse(data)

#         if isinstance(post_id, int):
#             print(post_id)
#             print(comment)
#             post_to_comment = Post.objects.get(id = post_id)
#             comment_post = Comment(username=request.user.username, comment = comment)
#             comment_post.save()
#             comment_post.post.add(post_to_comment)
#             profile = Profile.objects.filter(user=request.user.id).exists()
#             if profile:
#                 comment = {'user': request.user.username,'image': request.user.profile.profile_image.url, 'comment': comment}
#             else:
#                 comment = {'user': request.user.username,'image': None, 'comment': comment}
#             data = {'success': 'Successfully liked the post', 'comment': comment}
#             return JsonResponse(data)
#         else:
#             data = {'fail': 'Something wrong happened.'}
#             return JsonResponse(data)





