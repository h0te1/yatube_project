from django.shortcuts import render


def index(request):
    templates = 'posts/index.html'
    return render(request, templates)
