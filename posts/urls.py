from django.urls import path
from posts.views import feeds,video_feed

app_name = "posts"
urlpatterns = [
    path("feeds/",feeds, name="feeds"),
    path("videa_feed/",video_feed, name="video_feed"),
]

