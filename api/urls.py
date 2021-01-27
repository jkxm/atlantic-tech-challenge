from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.api_overview),
    path('all_customers/', views.all_customers),
    path('all_subscriptions/', views.all_subscriptions),
    path('get_customer/<str:id>/', views.get_customer),
    path('get_subscription/<str:id>/', views.get_subscription),
    path('receive_customer', views.receive_customer)
]