from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import BlogPost

# View to list all blogs
class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'

# View to display a single blog post
class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'

# View to create a new blog post
class BlogCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/blog_form.html'
    fields = ['title', 'author', 'content']
    success_url = reverse_lazy('blog_list')  # Redirect to the blog list after creation
