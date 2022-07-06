from django.shortcuts import render
from .models import BlogModel
from django.views.generic import ListView, DetailView

class BlogsView(ListView):
    model = BlogModel
    template_name = 'main/posts.html'
    page_kwarg = 'blog'


class BlogsDetailView(DetailView):
    model = BlogModel
    template_name = 'main/blogdetail.html'