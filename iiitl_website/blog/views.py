from django.shortcuts import render

from .models import Post


def homepage(request):
    latest_posts = Post.objects.get_latest_posts()[:6]
    return render(request, 'blog/index.html', {'latest_posts': latest_posts})


def post_lists(request):
    posts = Post.objects.get_latest_posts()
    return render(request, 'blog/posts_list.html', {'posts': posts})
