
from django.contrib import admin
from .models import Tour, Category, Tag


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'location', 'price', 'get_tags')
    list_display_links = ('id', 'name')
    list_filter = ('category', 'tags')
    search_fields = ('name', 'description', 'location', 'category__name', 'tags__name')
    readonly_fields = ('get_tags',)

    @admin.display(description='Теги')
    def get_tags(self, instance):
        return ', '.join(tag.name for tag in instance.tags.all())


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
