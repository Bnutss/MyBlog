from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_list')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})


def like_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.likes += 1
    post.save()
    return JsonResponse({'likes': post.likes})