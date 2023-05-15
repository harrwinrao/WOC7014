from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='gamereview'),
    path('register', views.AddUserFormView.as_view(), name='register')
]
