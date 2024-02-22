"""
URL configuration for model_relationships project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from main_app import views

urlpatterns = [
    path('', views.show, name='home'),
    path('api/artists/', views.fetch_or_save_artist, name='fetch_or_save_artist'),
    path('api/artists/<int:id>/', views.fetch_artist, name='fetch_artist'),
    path('api/artists/<int:id>/update/', views.update_artist, name='update_artist'),
    path('api/artists/<int:id>/delete/', views.delete_artist, name='delete_artist'),
    path('api/artists/<int:id>/albums/', views.artist_albums, name='artist_albums'),
    path('admin/', admin.site.urls),
]


# api/artists/ Fetch all artists GET
# api/artists/ Create artists POST
# api/artists/1 Fetch details of artist GET
# api/artists/1/update/ update details of artist PUT/ PATCH
# api/artists/1/delete/ delete an artist DELETE
