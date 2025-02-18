from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.popular_list, name='popular'),
    path('shop/', views.product_list, name='product_list'),
    path('shop/category/<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<slug:slug>/', views.product_detail,
         name='product_detail'),
]