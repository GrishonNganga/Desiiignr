from django.conf.urls import url
from insta.views import index

urlpatterns = [
    url('', index, name='index'),
]