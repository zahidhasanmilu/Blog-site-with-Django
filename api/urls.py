from django.urls import path
from .import views
urlpatterns = [
    path('', views.all_blogs, name='allblogs'),
    path('<int:id>/', views.single_blog, name='single_blog'),
    path('update-api/<int:id>/', views.update_blog, name='update_blog'),
    path('create-api/', views.create_blog, name='create_blog'),
    path('delete_blog/<int:id>', views.delete_blog, name='delete_blog'),
]
