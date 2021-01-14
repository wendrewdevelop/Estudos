# django imports
from django.urls import path

# app imports
from .views import ArticleView


app_name = "articles"
urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('articles/<int:id>', ArticleView.as_view()),
]