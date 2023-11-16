from django.urls import path
from . import views
app_name = 'item' # namespace for item app

urlpatterns = [
    path('<int:id>/', views.detail, name='detail'),
    path('create-item/', views.createItem, name='create-item'),
    path('women/', views.women, name='women'),
    path('men/', views.men, name='men'),
    path('kids/', views.kids, name='kids'),


]