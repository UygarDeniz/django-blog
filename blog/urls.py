
from django.urls import path
from .views import Home, CreateNewPost, PostDetailView, UpdatePostView, DeletePostView

app_name = "blog"
urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("posts/new", CreateNewPost.as_view(), name="post-new"),
    path("post/<int:pk>/update", UpdatePostView.as_view(), name="post-update"),
    path("post/<int:pk>/delete", DeletePostView.as_view(), name="post-delete"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]