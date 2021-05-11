from blog.views import article_list_view, article_create_view
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('', article_list_view),
    path('detail/', article_create_view),
    
]
