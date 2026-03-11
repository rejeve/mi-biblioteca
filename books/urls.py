from . import views
from django.urls import path

urlpatterns = [
    path('publisher/', views.list_publisher, name='list_publisher'),
    path('add_publisher/', views.add_publisher, name='add_publisher'),
    path('edit_publisher/<int:id>/', views.edit_publisher, name='edit_publisher'),
    path('delete_publisher/<int:id>/', views.delete_publisher, name='delete_publisher'),
    path('author/', views.list_authors, name='list_authors'),
    path('add_author/', views.add_author, name='add_author'),
    path('edit_author/<int:id>/', views.edit_author, name='edit_author'),
    path('delete_author/<int:id>/', views.delete_author, name='delete_author'),
    path('list/', views.list_book, name='list_books'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:id>/', views.delete_book, name='delete_book'),
]
