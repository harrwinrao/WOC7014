from . import views
from django.urls import path

urlpatterns = [
    path('lunch', views.lunch_randomiser, name='lunch_randomiser'),
    path('patterns', views.display_patterns, name='display_patterns'),
    path('scores', views.marks_calculator_view, name='marks_calculator_view')
]
