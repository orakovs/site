from django.db import models
from django.utils import timezone


#sliders
class Slider(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='slider')
    link = models.URLField(max_length=256)

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры"

    def __str__(self):
        return self.name

#news category
class NewsCategory(models.Model):
    name = models.CharField(max_length=128)    
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Категория новостей"
        verbose_name_plural = "Категории новостей"

    def __str__(self):
        return self.name

#news
class News(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='news')
    datetime = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.name