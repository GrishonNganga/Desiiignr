from django.urls import path, include
from insta.views import index

urlpatterns = [
    path('', index, name='index'),
    # path('home', home, name = 'other')
]