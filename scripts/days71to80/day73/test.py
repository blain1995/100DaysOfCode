import requests
import os

API_KEY = os.environ.get('MOVIE_DB_API_KEY')

MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"