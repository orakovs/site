from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator


def HomeView(request, category_id=None):
    sliders = Slider.objects.all()
    selected_category = None
        
    category_id = 1
    selected_category = get_object_or_404(NewsCategory, pk=category_id)
    
    news = News.objects.filter(category=selected_category).order_by('-datetime')[:4]
    
    context = {
        'current_page': 'home_url',
        'sliders': sliders,
        'news': news,
        'selected_category': selected_category,
    }
    
    return render(request, 'home.html', context)


def NewsView(request, category_id=None):
    news_category = NewsCategory.objects.all()
    selected_category = None
    news = News.objects.all().order_by('-datetime')
    
    query = request.GET.get('q')
    if query:
        news = news.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    
    if category_id:
        selected_category = get_object_or_404(NewsCategory, pk=category_id)
        news = news.filter(news_category=selected_category)
        
    paginator = Paginator(news, 8)
    page_number = request.GET.get('page')
    news_page = paginator.get_page(page_number)
    
    context = {
        'current_page': 'news_url',
        'news_category':news_category,
        'news_page': news_page,
        'selected_category': selected_category,
        'search_query': query,
    }
    return render(request, 'news.html', context)
