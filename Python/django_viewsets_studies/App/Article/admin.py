# django imports
from django.contrib import admin

# app imports
from .models import Article, Author


admin.site.register(Article)
admin.site.register(Author)
