from django.shortcuts import render, get_object_or_404
from .models import Post, Group

# Количество отображаемых постов на страницах
SHOW_POSTS = 10


# Функция для главной страницы
def index(request):
    template = 'posts/index.html'  # Шаблон
    posts = Post.objects.all()[:SHOW_POSTS]  # Посты
    context = {
        'posts': posts
    }
    return render(request, template, context)


# Функция для страницы группы
def group_posts(request, slug):
    template = 'posts/group_list.html'  # Шаблон
    group = get_object_or_404(Group, slug=slug)  # Группа
    posts = group.group_posts.all()[:SHOW_POSTS]  # Посты
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, template, context)
