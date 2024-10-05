from django.urls import path
from news.views import NewsListView, NewsDetailView

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('102/<int:pk>/', NewsDetailView.as_view(), name='news_detail')
]
