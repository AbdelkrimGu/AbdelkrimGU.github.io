from django.urls import path 
from .views import  article_detail , ArticleAPIView



urlpatterns = [
    path('article/', ArticleAPIView.as_view()), 
    path('article/<int:pk>/', article_detail),
]
