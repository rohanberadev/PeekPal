"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page),
    path('home/', views.home_page, name="home"),
    path('notifications/', views.notifications_page),
    path('peeks/', views.peeks_page),
    path('vault/', views.vault_page),
    path('friends/', views.friends_page),
    path('profile/', views.profile_page),
    path('', include('myauth.urls')),
    path('', include('post.urls')),
    path('user/', views.search_user, name="search_user"),
    path('user/<str:username>', views.user_profile, name="user_profile"),
    path('not-found', views.not_found, name="not_found"),
]
