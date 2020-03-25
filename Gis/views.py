from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from Gis.models import Article


def home(request):
    '''
    return HttpResponse("Hello world")
    # return render(request, "Gis/home.html")
    articles = Article.objects.all()
    context = {
        'articles': articles
    }

    return render(request, "Gis/home.html", context)
    '''
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, "Gis/home.html", context)


def about(request):
    return render(request, "Gis/about.html")



def show_articles(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'gis/article.html', {'article': article})


def map(request):
    return render(request, "Gis/map.html")
