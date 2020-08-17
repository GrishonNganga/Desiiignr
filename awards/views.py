from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, get_user_model
import json

from .models import Profile, Post, Follower, Like, Comment
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

@login_required(login_url='/login')
def index(request):
    posts = Post.get_all_posts()
    followers = list(Follower.objects.filter(user = request.user))
    pass_followers = []
    for follower in followers:
        pass_followers.append(follower.username)


    return render(request, 'index.html', {'posts': posts, 'followers': pass_followers})



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



@login_required(login_url='/login')
def show_post(request, post_id):
    post = Post.objects.get(id = post_id)
    comments = list(Comment.objects.filter(post=post))
    print(comments)
    return render(request, 'post.html', {'post': post, 'comments': comments})


@login_required(login_url='/login')
def follow_request(request):
    if request.method =='POST':
        if request.POST.get('follow'):
            user_id = int(request.POST.get('follow'))
            if isinstance(user_id, int):
                print(user_id)
                user_to_follow = User.objects.get(id = user_id)
                follow = Follower(username=user_to_follow.username)
                follow.save()
                follow.user.add(request.user)
                data = {'success': 'Successfully followed the user'}
                return JsonResponse(data)
            else:
                data = {'fail': 'Something wrong happened.'}
                return JsonResponse(data)
                


@login_required(login_url='/login')
def like_post(request):
    if request.method =='POST':
        if request.POST.get('like'):
            post_id = int(request.POST.get('like'))
            if isinstance(post_id, int):
                print(post_id)
                post_to_like = Post.objects.get(id = post_id)
                like_post = Like(username=request.user.username)
                like_post.save()
                like_post.post.add(post_to_like)
                data = {'success': 'Successfully liked the post'}
                return JsonResponse(data)
            else:
                data = {'fail': 'Something wrong happened.'}
                return JsonResponse(data)


@login_required(login_url='/login')
def make_comment(request):
    if request.method =='POST':
        if request.POST.get('comment'):
            post_id = int(request.POST.get('post'))
            comment = request.POST.get('comment')
        elif request.POST.get('comment-lg'):
            post_id = int(request.POST.get('post-lg'))
            comment = request.POST.get('comment-lg')
        else:
            data = {'fail': 'Something wrong happened.'}
            return JsonResponse(data)

        if isinstance(post_id, int):
            print(post_id)
            print(comment)
            post_to_comment = Post.objects.get(id = post_id)
            comment_post = Comment(username=request.user.username, comment = comment)
            comment_post.save()
            comment_post.post.add(post_to_comment)
            profile = Profile.objects.filter(user=request.user.id).exists()
            if profile:
                comment = {'user': request.user.username,'image': request.user.profile.profile_image.url, 'comment': comment}
            else:
                comment = {'user': request.user.username,'image': None, 'comment': comment}
            data = {'success': 'Successfully liked the post', 'comment': comment}
            return JsonResponse(data)
        else:
            data = {'fail': 'Something wrong happened.'}
            return JsonResponse(data)





