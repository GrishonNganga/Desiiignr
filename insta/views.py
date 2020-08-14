from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, get_user_model

from .models import Profile
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
    return render(request, 'index.html')



@login_required(login_url='/login')
def profile(request):
    if request.method == 'POST' and request.FILES.get('profile'):
        profile_image = request.FILES.get('profile')
        user = request.user
        user.profile.profile_image = profile_image

        user.save()
        print(profile_image)

    print(request.user.profile.profile_image)
    return render(request, 'profile.html')



@login_required(login_url='/login')
def upload_pic(request):

    if request.method == 'POST' and request.FILES.get('upload') and request.POST.get('description'):
        print('We good')
    else:
        print('Make sure you have filled all fields.')
    return render(request, 'upload.html')