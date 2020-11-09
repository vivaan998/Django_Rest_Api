from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

# Create your views here.

from .models import Movie
from .serializers import MovieSerializer

#helper functions
from .helper.local_database import (create_new_movie, find_movie_in_db)
from .helper.omdb_databse import get_movie_data


@api_view(['POST', 'GET'])
def movies(request):
    if request.method == 'POST':

        if 'title' not in request.data:
            return HttpResponseBadRequest({'Title field can\'t be empty'})

        title = request.data['title']
        movie_data = get_movie_data(title)
        if movie_data == {}:
            return HttpResponseNotFound('Movie could not be fetched from IMDB\'s Database')

        imdb_id = movie_data.get('imdbID')

        movie = find_movie_in_db(imdb_id=imdb_id)

        if movie:
            return Response('Movie already exsists in local database', status=201)
        
        movie = create_new_movie(movie_data)

        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=201)

    elif request.method == 'GET':
        all_movies = Movie.objects.all()
        serializer = MovieSerializer(all_movies, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def movies_id(request, imdb_id):
    
    if request.method == 'GET': 
        qs = Movie.objects.all().filter(imdbid= imdb_id)
        # print(qs)
        serializer = MovieSerializer(qs, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def year(request, year):

    if request.method == 'GET':
        qs = Movie.objects.all().filter(year=year)
        # print(qs)
        serializer = MovieSerializer(qs, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def ratings(request, rating):

    if request.method == 'GET':
        qs = Movie.objects.all().filter(imdbrating__gte= rating)
        # print(qs)
        serializer = MovieSerializer(qs, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def genres(request, genre):

    if request.method == 'GET':
        qs = Movie.objects.filter(genre__icontains=genre)
        # print(qs)
        serializer = MovieSerializer(qs, many=True)
        return Response(serializer.data)


class Edit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_url_kwarg = 'movie_id'


