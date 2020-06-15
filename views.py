from django.shortcuts import render
from .models import News, Category, Messages
from .serializers import NewsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import MessageForm
from django.core.mail import EmailMessage
from django.conf import settings
import datetime
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView


def index(request):
    news = News.objects.filter(published__date__gte=datetime.datetime.today().date())
    categories = Category.objects.all()
    context = {'news': news, 'categories': categories}
    return render(request, 'news/index.html', context)


def by_category(request, category_id):
    news = News.objects.filter(category=category_id).filter(published__date__gte=datetime.datetime.today().date())
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'news': news, 'categories': categories, 'current_category': current_category}
    return render(request, 'news/by_category.html', context)


def feedback(request):
    if request.method == 'POST':
       feed = MessageForm(request.POST)
       if feed.is_valid():
           feed.save()
           email = EmailMessage(subject='У Вас новое сообщение в форме обратной связи на сайта новостей Magpie',
                                 body=str(Messages.objects.first().text), to=['wdv85@mail.ru'])
           return render(request, 'news/msgsend.html')
       else:
          context = {'form': feed}
          return render(request, 'news/feedback.html', context)
    else:
        feed = MessageForm()
        context = {'form': feed}
        return render(request, 'news/feedback.html', context)


@api_view(['GET'])
def api_news(request):
    if request.method == 'GET':
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)


class RobotsTxt(TemplateView):
    template_name = 'news/robots.txt'
    content_type = "text/plane"