from django.urls import path
from .views import TagView, CategoryView, PostViewSet


urlpatterns = [
    # path('posts/', PostView.as_view()),
    # path('posts/<slug:pk>/', PostDetailView.as_view()), 
    path('tags/', TagView.as_view()),
    path('categories/', CategoryView.as_view()),
    path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('posts/<slug:pk>/', PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}))

]