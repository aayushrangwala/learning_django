from django.conf.urls import url
from blog import views

urlpatterns = [
            url(r'^$', views.MainPage, name = 'main_page'),
            url(r'^(?P<post_id>[0-9]+)/$', views.PostDetails, name = 'post_details'),
            url(r'^(?P<post_id>[0-9]+)/latestnews/$', views.LatestNews, name = 'latest_news'),

    ]
