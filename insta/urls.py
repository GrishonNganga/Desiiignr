from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from insta.views import index, profile, upload_pic

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^profile', profile, name='profile'),
    url(r'^upload', upload_pic, name='upload')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)