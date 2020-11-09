from django.urls import path
from Rest_API import views


urlpatterns = [
    path('', views.movies, name='movies'),
   
    path('movie/imdb/<str:imdb_id>/', views.movies_id, name='imdb_id'),
    path('movies/published_year/<int:year>/', views.year, name='movies_year'),
    path('movies/ratings/<int:rating>/', views.ratings, name='movies_rating'),
    path('movies/genres/<str:genre>/', views.genres, name='movies_genre'),

    path('movies/<int:movie_id>/',
         views.Edit.as_view(), name='update_delete_movie'),
]