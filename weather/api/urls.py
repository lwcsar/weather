from django.urls import path

from . import views

urlpatterns = [
    path('t/', views.TemperatureList.as_view()),
    path('t/<int:pk>/', views.TemperatureDetail.as_view()),
    path('rh/', views.HumidityList.as_view()),
    path('rh/<int:pk>/', views.HumidityDetail.as_view()),
    path('bp/', views.PressureList.as_view()),
    path('bp/<int:pk>/', views.PressureDetail.as_view()),
]