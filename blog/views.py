from datetime import datetime
from django.shortcuts import render
from django.utils import timezone
from blog.models import Article

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})

def addition(request, nombre1, nombre2):
    total = int(nombre1) + int(nombre2)

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())

def article_liste(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_liste.html', {'articles': articles})

def index(request):
    return render(request, 'blog/index.html')