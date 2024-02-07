from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView, name='home_url'),
    path('news', NewsView, name='news_url'),
    path('news/<int:category_id>/', NewsView, name='news_with_category_url'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)