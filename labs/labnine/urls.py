from . import views
from django.urls import path

urlpatterns = [
    path('gameapi/', views.GameApiView.as_view()),
    path('gameapi/<int:pk>/', views.GameDetailApiView.as_view())
]
