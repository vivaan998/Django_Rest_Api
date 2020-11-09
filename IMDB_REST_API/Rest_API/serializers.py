from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'year',
            'released',
            'genre',
            'director',
            'writer',
            'actors',
            'plot',
            'language',
            'country',
            'awards',
            'poster',
            'metascore',
            'imdbrating',
            'imdbid',
            'type_picture',
            
        )
        read_only_fields = ('id', 'title',)



