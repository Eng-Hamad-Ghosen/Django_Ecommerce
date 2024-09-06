from django.urls import path
from . import views

app_name='product'
urlpatterns = [
    path('',views.product_list,name='product_list'),
    path('<str:slug>',views.product_details,name='product_details'),
]