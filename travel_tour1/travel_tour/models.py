from django.db import models

class Tour(models.Model):
    
    class Meta:
        verbose_name = 'тур'
        verbose_name_plural = 'туры'
    
    name = models.CharField(verbose_name='название', max_length=100)
    image = models.ImageField(verbose_name='изображение', upload_to='tour_images')
    price = models.IntegerField(verbose_name='цена')
    description = models.TextField(verbose_name='описание', max_length=300)
    tags = models.ManyToManyField('Tag', verbose_name='теги')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='tours', verbose_name='категория')
    location = models.CharField(max_length=200, verbose_name='местоположение')

    def __str__(self):
        return self.name


class Category(models.Model):
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
    
    name = models.CharField(max_length=100, verbose_name='название')

    def __str__(self):
        return self.name


class Tag(models.Model):
    
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
    
    name = models.CharField(max_length=100, verbose_name='название')

    def __str__(self):
        return self.name
