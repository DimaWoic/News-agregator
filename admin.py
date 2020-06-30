from django.contrib import admin

# Register your models here.
from .models import News, Category, Messages, TUsers


class NewsAdmin(admin.ModelAdmin):
    model = News
    list_display = ('published', 'category', 'title', 'description')
    list_display_links = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    model = Category


class  MassagesAdmin(admin.ModelAdmin):
    model = Messages
    list_display = ('published', 'name', 'email', 'text')


class TUsersAdmin(admin.ModelAdmin):
    model = TUsers
    list_display = ('user_id', 'user', 'subscription')

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Messages, MassagesAdmin)
admin.site.register(TUsers, TUsersAdmin)