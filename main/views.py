from django.shortcuts import render, get_object_or_404
from .models import *


def Home(request, category_id=None):
    sliders = Slider.objects.all()
    selected_category = None
    
    category_id = 1
    selected_category = get_object_or_404(NewsCategory, pk=category_id)
    
    news = News.objects.filter(category=selected_category).order_by('-datetime')
    
    context = {
        'current_page': 'home_url',
        'sliders': sliders,
        'news': news,
        'selected_category': selected_category,
    }
    
    return render(request, 'home.html', context)
