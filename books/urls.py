from . import views
from django.urls import path

urlpatterns = [
    path('publisher/', views.list_publisher, name='list_publisher'),
    path('publisher/add/', views.add_publisher, name='add_publisher'),
    path('publisher/<int:id>/edit/', views.edit_publisher, name='edit_publisher'),
    path('publisher/<int:id>/delete/', views.delete_publisher, name='delete_publisher'),

    path('author/', views.list_authors, name='list_authors'),
    path('author/add', views.add_author, name='add_author'),
    path('author/<int:id>/edit/', views.edit_author, name='edit_author'),
    path('author/<int:id>/detail/', views.author_detail, name='author_detail'),
    path('author/<int:id>/delete/', views.delete_author, name='delete_author'),

    path('list/', views.list_book, name='list_books'),
    path('add/', views.add_book, name='add_book'),
    path('<int:id>/edit/', views.edit_book, name='edit_book'),
    path('<int:id>/delete/', views.delete_book, name='delete_book'),
]
