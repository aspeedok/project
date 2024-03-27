from django.urls import path

from apps.posts.views import PostCreateView
from apps.posts.views import PostListAPIView
from apps.posts.views import PostDetailAPIView

urlpatterns = [
    path("create_post/", PostCreateView.as_view(), name="create-post"),
    path("posts/", PostListAPIView.as_view(), name="posts-list"),
    path("posts/<int:pk>/", PostDetailAPIView.as_view(), name="post-detail"),
]
