from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from insta.views import index, profile, upload_pic, show_post, follow_request

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^profile', profile, name='profile'),
    url(r'^upload', upload_pic, name='upload'),
    url(r'^post/(\d)/', show_post, name='post'),
    url(r'^follow$', follow_request, name='follow' )
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)