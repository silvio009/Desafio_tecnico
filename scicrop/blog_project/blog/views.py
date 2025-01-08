from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Ordena pelo mais recente
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Redireciona para a lista de posts
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})

def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')  # Redireciona para a lista de posts
    
    return render(request, 'blog/confirm_delete.html', {'post': post})

