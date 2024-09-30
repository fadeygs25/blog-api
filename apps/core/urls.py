from django.urls import path
from .views import BlogPostViewSet

urlpatterns = [
    path('posts/', BlogPostViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('posts/<int:pk>/', BlogPostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
