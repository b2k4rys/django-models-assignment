from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from news.models import News, Comment
from news.forms import NewsPostForm, CommentPostForm
from django.shortcuts import get_object_or_404
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
      new_news = form.save()
      id = new_news.id

      return redirect('news:news_detail', pk=id)

class NewsDetailView(DetailView):
   
  model = News
  context_object_name = 'news'
  template_name = 'news/news_detail.html'
  

  def get_context_data(self, **kwargs):
      pk = self.kwargs.get('pk')
      news = get_object_or_404(News, pk=pk)
      comments = Comment.objects.filter(news_comment=news).all()
      context = super().get_context_data(**kwargs)
      context['form'] = CommentPostForm()
      context['comments'] = comments
      return context

  def post(self, request, pk, *args, **kwargs):
    
    form = CommentPostForm(request.POST)

    if form.is_valid():
        news = get_object_or_404(News, pk=pk)
        comment = form.save(commit=False)
        comment.news_comment = news
        comment.save()
        id = news.id
        return redirect('news:news_detail', pk=id)
    




    
   

   


