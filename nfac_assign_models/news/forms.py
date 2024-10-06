from django import forms 
from news.models import News, Comment


class NewsPostForm(forms.ModelForm):
  class Meta:
    model = News
    fields = ('title', 'content')
    
class CommentPostForm(forms.ModelForm):
  class Meta: 
    model = Comment
    fields = ('content',)