from django.urls import path
from django.contrib import admin
from .views import index, posts, posting

app_name = 'posts'

urlpatterns=[
    path("admin/", admin.site.urls),
    path('', index),
    path('posts/', posts),
    path("posts/<int:pk>/", posting, name="posting"),
]