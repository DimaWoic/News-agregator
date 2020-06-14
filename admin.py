from django.contrib import admin

# Register your models here.
from .models import News, Category, Messages


class NewsAdmin(admin.ModelAdmin):
    model = News
    list_display = ('published', 'category', 'title', 'description')
    list_display_links = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    model = Category


class  MassagesAdmin(admin.ModelAdmin):
    model = Messages
    list_display = ('published', 'name', 'email', 'text')

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Messages, MassagesAdmin)