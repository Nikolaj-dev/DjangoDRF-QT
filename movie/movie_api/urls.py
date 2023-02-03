from django.urls import path
from . import views


urlpatterns = [
    path('movie/all', views.movie_list),
    path('movie/all/<int:pk>', views.movie_detail),
]