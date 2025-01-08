from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/<int:id>/edit/', views.edit_post, name='post_edit'),
    path('post/<int:id>/delete/', views.delete_post, name='post_delete'),
]
