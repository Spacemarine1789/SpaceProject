from django.shortcuts import render
from .models import Post


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, template, context)
