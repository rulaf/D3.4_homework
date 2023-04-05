# from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView
# выводить список объектов из БД
from .models import *


# Create your views here.
class NewsList(ListView):
    model = Post
    template_name = 'flatpages/news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['value1'] = None
        return context


class NewDetail(DetailView):
    model = Post
    template_name = 'flatpages/post_detail.html'
    context_object_name = 'post_detail'
