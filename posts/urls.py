from django.urls import path
from django.contrib import admin
from .views import index, posts, posting, newpost, deletepost, signup
from django.contrib.auth import views as auth_views

app_name = 'posts'

urlpatterns=[
    path("admin/", admin.site.urls),
    path('', index),
    path('posts/', posts),
    path("posts/<int:pk>/", posting, name="posting"),
    path("newpost/", newpost),
    path('posts/<int:pk>/remove/', deletepost),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
]