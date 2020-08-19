from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from awards.views import index, profile, upload_pic, show_post, vote_post, UsersList, ProjectsList
#follow_request, like_post, make_comment

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^profile', profile, name='profile'),
    url(r'^upload', upload_pic, name='upload'),
    url(r'^post/(\d)/', show_post, name='post'),
    # url(r'^follow$', follow_request, name='follow' ),
    url(r'^vote/(\d)/', vote_post, name='vote' ),
    url(r'^api/users/$', UsersList.as_view()),
    url(r'^api/projects/$', ProjectsList.as_view())
    # url(r'^comment', make_comment, name='comment')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)