
from django.contrib import admin
from django.conf.urls import url, include
from awards.views import loginPage, registerPage, show_post

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^register', registerPage, name='register'),
    url(r'^login', loginPage, name='login'),
    url('', include('awards.urls') ), 
    url(r'^profile', include('awards.urls')),
    url(r'^upload', include('awards.urls')),
    url(r'^post/(\d)/', include('awards.urls')),
]
