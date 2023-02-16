from django.urls import path
from DemoApp2 import views

urlpatterns = [
    path('third/', views.f3),
    path('four/', views.f4),
];