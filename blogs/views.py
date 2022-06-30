from django.shortcuts import render
from .models import BlogModel
from django.views.generic import ListView

class BlogsView(ListView):
    model = BlogModel
    template_name = 'main/posts.html'
    paginate_by = 1
    page_kwarg = 'blog'