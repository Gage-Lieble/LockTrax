
from django.urls import path, include
from . import views

app_name = 'search_locktrax'
urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.results, name='results'),
]
