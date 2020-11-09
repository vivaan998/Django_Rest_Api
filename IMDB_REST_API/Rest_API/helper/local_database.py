from Rest_API.models import Movie
from datetime import date, datetime

def find_movie_in_db(imdb_id):
    movie = Movie.objects.filter(imdbid=imdb_id)
    if movie:
        return movie[0]
    return None


def parse_movie_data(movie_data):
    
    IGNORE = ['response', 'ratings', 'type', 'released', 'runtime', 'dvd', 'imdbvotes']
    parsed_movie_data = {}

    for key, v in movie_data.items():
        if v == 'N/A':
            continue

        key_lower = key.lower()

        if key_lower not in IGNORE:
            parsed_movie_data[key_lower] =  v
        elif key_lower == "released" or key_lower == "runtime":
            if(key_lower == "released"):
                v = datetime.strptime(v, '%d  %b %Y').date()
            else:
                v = int(v.replace(' min', ''))
            parsed_movie_data[key_lower] =  str(v)

    parsed_movie_data['type_picture'] = movie_data['Type']

    
    return parsed_movie_data


def create_new_movie(movie_data):

    if not movie_data:
        return None

    movie_data = parse_movie_data(movie_data)
    movie = Movie(**movie_data)
    movie.save()

    return movie


