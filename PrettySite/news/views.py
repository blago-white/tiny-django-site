import datetime
from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from .models import Posts
from .forms import PostsForm


def news(request: WSGIRequest):
    posts = Posts.objects.order_by('-date')
    posts = {'posts': [post for post in posts]}
    return render(request, 'news/news_home.html', context=posts)


def create_news(request: WSGIRequest):
    error = ''
    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Неверно заполнена форма'

    form = PostsForm()
    data = {
        'form': form,
        'error': error,
        'creating_header': error if error else 'Create your post!'
    }

    return render(request, 'news/create_news.html', data)
