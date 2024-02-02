from django.urls import path
from .views import PostView, PostDetailView, TagView, CategoryView


urlpatterns = [
    path('posts/', PostView.as_view()),
    path('posts/<slug:pk>/', PostDetailView.as_view()), 
    path('tags/', TagView.as_view()),
    path('categories/', CategoryView.as_view())
]