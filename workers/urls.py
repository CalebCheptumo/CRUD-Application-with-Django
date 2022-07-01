from django.urls import path
from . import views


app_name = 'workers'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('edit/<int:worker_id>/', views.edit, name='edit'),
    path('delete/<int:worker_id>/', views.delete, name='delete'),
    path('insert/', views.insert, name='insert'),
    path('update/<int:worker_id>/', views.update, name='update'),

]