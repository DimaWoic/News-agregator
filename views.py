from django.shortcuts import render
from .models import News, Category, Messages
from .serializers import NewsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import MessageForm
from django.views.generic import TemplateView


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(news, 20)
    try:
        page_num = request.GET.get('page')
    except EmptyPage:
        page_num = paginator.get_page(paginator.num_pages)
    except PageNotAnInteger:
        page_num = paginator.get_page(paginator.num_pages)
    page = paginator.get_page(page_num)
    page_list = page.object_list
    context = {'news': news, 'categories': categories, 'page': page, 'page_list': page_list}
    return render(request, 'news/index.html', context)


def by_category(request, category_id):
    news = News.objects.filter(category=category_id)
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    paginator = Paginator(news, 20)
    try:
        page_num = request.GET.get('page')
    except EmptyPage:
        page_num = paginator.get_page(paginator.num_pages)
    except PageNotAnInteger:
        page_num = paginator.get_page(paginator.num_pages)
    page = paginator.get_page(page_num)
    page_list = page.object_list
    context = {'news': news, 'categories': categories, 'current_category': current_category, 'page': page, 'page_list': page_list}
    return render(request, 'news/by_category.html', context)


def feedback(request):
    if request.method == 'POST':
       feed = MessageForm(request.POST)
       if feed.is_valid():
           feed.save()
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