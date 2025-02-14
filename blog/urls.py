from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),  # /blogs/ → List all blog posts
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),  # /blogs/<int:id>/ → View a single post
    path('new/', BlogCreateView.as_view(), name='blog_create'),  # /blogs/new/ → Create a blog post
]
