from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.gallery_view, name='gallery'),
    path('upload/', views.upload_view, name='upload'),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
    path('photo/<int:pk>/delete/', views.delete_photo, name='delete_photo'),
    path('photo/<int:pk>/download/', views.download_photo, name='download_photo'),
]