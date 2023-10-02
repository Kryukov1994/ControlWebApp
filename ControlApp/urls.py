from django.urls import path

from . import views

app_name = "ControlApp"

urlpatterns = [
    path("", views.base, name="base"),
    path("post/", views.post, name="post"),
    path("post/<int:post_id>/", views.poststr, name="poststr"),
]
