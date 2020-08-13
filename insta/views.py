from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import RegisterUserForm

def register(request):
    form = RegisterUserForm()

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'accounts/register.html', {'register_form': form})


@login_required
def index(request):
    return render(request, 'index.html')


