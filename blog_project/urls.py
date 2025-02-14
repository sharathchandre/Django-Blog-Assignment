from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Redirect root URL to the blogs list page
def redirect_to_blogs(request):
    return redirect('/blogs/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include('blog.urls')),  # Include blog app's URLs
    path('', redirect_to_blogs),  # Redirect root URL to blogs/
]
