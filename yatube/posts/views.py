from django.shortcuts import render


def index(request):
    templates = 'posts/index.html'
    text = 'Это главная страница проекта Yatube'
    context = {
        'text': text,
    }
    return render(request, templates, context)
