# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Group


# Функция для главной страницы
def index(request):
    template = 'posts/index.html'  # Шаблон
    posts = Post.objects.order_by('-pub_date')[:10]  # Пост
    context = {
        'posts': posts
    }
    return render(request, template, context)


# Функция для страницы группы
def group_posts(request, slug):
    template = 'posts/group_list.html'  # Шаблон
    group = get_object_or_404(Group, slug=slug)  # Группа
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]  # Пост
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, template, context)
