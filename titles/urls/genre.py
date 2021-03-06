from django.urls import path

from ..views import GenreDetailAPIView, GenreListAPIView

app_name = 'genres'

urlpatterns = [
    path('', GenreListAPIView.as_view(), name='genre_list'),
    path('<slug:slug>/', GenreDetailAPIView.as_view(), name='genre_detail'),
]
