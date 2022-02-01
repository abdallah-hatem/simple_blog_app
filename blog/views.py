from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):

    all_posts = Post.objects.filter(status='published')

    return render(request, 'home.html', {'posts': all_posts})


def post_single(request, post):

    post = get_object_or_404(Post, slug=post, status='published')

    return render(request, 'singlePost.html', {'post': post})
