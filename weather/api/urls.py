from django.urls import path

from . import views

urlpatterns = [
    path('', views.TemperatureList.as_view()),
    path('<int:pk>/', views.TemperatureDetail.as_view()),
]