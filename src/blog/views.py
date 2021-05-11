from django.shortcuts import render


# from django.views.generic import (
#     ListView
# )
from .forms import ArticleForm, RawArticleForm
# Create your views here.
from .models import Article

def article_list_view(request):
    obj = Article.objects.get(id=1)
    context = {
        'title': obj.title,
        'description': obj.content
    }
    return render(request, 'blog/article_list.html', context)

def article_create_view(request):
    my_form = RawArticleForm()
    if request.method == 'POST':
        my_form = RawArticleForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {'form':my_form}
    return render(request, 'blog/')

# class ArticleListView(ListView):
#     queryset = Article.objects.all()
