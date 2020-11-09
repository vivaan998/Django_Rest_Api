# Django Rest_Api Project with OMDB's API to Display Movies.   

## Requirements

This Project is developed using **Django** and **Django REST Framework** . Additional requirements are included in **requirement.txt** file for interaction with *www.omdbapi.com* api. 
<br/>Also change the **OMDB_API_KEY** in the **settings.py** 

## How to run project locally

Clone repository and got to project's root directory afterwards follow steps:

1. Activate python virtual environment <br />
`source /path/to/local/env`

2. Install requirements <br />
`pip install -r requirements.txt`

3. Make Migrations <br />
**Currently sqllite3 database is used, you can change it according to your convenience.** <br />   
`python manage.py makemigrations` <br />
`python manage.py migrate`

3. Run server <br />
`python manage.py runserver`


### GET /movies/

Shows you the list of all the movies in the local database.

### POST /movies/

Fetches movie data from external api and save it in to the local database.

Required Headers: <br />
Content-Type: application/json

Required json body fields: <br />
title

```json
{
    "title": "movie name"
}
```

### DELETE or UPDATE /movies/<movie-id>/ <br />  

Deletes movie from local database or updates content of that movie in local database.

### Published Year fetch
 movies/published_year/year/
eg: movies/published_year/2007/

This will return all the movies published in the year 2007.

### Movies fetched based on ratings
 movies/ratings/rating/
eg: movies/ratings/8/

This will return all the movies having ratings equal to or greater than 8. 

### Genre based fetching
 movies/genres/genre/
eg: movies/genres/comedy/

This will return all the movies whose genre has comedy in it.

##For better Visualization and Understanding of the project please refer to the Screenshots folder

