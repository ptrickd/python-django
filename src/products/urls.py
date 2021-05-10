from products.views import product_detail_view, product_create_view
from django.urls import path

app_name = 'products'
urlpatterns = [
    path('', product_detail_view),
    path('create/', product_create_view),
    
]
