from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogHomePage, name='home'),
    path('blog-post/', views.blogPost, name='blogPost'),
    path('edit-blog/<int:pk>/', views.editBlog, name='editBlog'),
    path('blog/<int:pk>/', views.DetailBlog, name='detailBlog'),
    path('delete-blog/<int:pk>/', views.deleteBlog, name='deleteBlog'),
    
]