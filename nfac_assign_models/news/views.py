from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from news.models import News
from news.forms import NewsPostForm
# Create your views here.

class NewsListView(ListView):
  model = News
  template_name = 'news/news_list_view.html'
  context_object_name = 'news'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['form'] = NewsPostForm()
      return context

  def post(self, request, *args, **kwargs):
    form  = NewsPostForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect('/news')

class NewsDetailView(DetailView):
   model = News
   context_object_name = 'news'
   template_name = 'news/news_detail.html'
   
