from django.urls import path
from . import views
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView

urlpatterns = [
    path('<int:category_id>/', views.by_category, name='by_category'),
    path('', views.index, name='index'),
    path('feed/', views.feedback, name='feedback'),
    path('api/', views.api_news),
    path('soroka.png', RedirectView.as_view(url='news/static/images/soroka.png', permanent=True)),
    path('robots.txt', TemplateView.as_view(template_name="news/robots.txt", content_type='text/plain')),
]