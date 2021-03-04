from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView
from django.core.paginator import Paginator

from .forms import BlogForm
from .models import Blog


def blog_list(request):
    blogs = Blog.objects.filter(author=request.user)
    blog_list = Blog.objects.all().filter(author=request.user)
    paginator = Paginator(blog_list, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/blog_list.html', {'blogs': blogs, 'posts': posts})


def upload_blog(request):
    if request.method == 'POST':
        ac = Blog.objects.create(author=request.user)
        form = BlogForm(request.POST, request.FILES, instance=ac)
        if form.is_valid():
            form.author = request.user
            form.save()
            return redirect('blog:blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog/upload_blog.html', {'form': form})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'file', 'text']
    success_url = reverse_lazy('blog:blog_list')
    template_name_suffix = '_update'
