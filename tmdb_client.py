import requests
import json
import random


from requests.models import HTTPError
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyYjBhNTA1ZjFhODE0MjAwYzE1NTgxZjEyNTRiYzhkNyIsInN1YiI6IjYxNTIyMzVjNjdkY2M5MDA4Y2U3MTJmMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.gLDUgiPELKhb2kjwkyq0jYUuJxaIhLtTL-J3AqT2z2M"

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f'Bearer {API_TOKEN}'
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

# dictionary = get_popular_movies()
# print(dictionary) - te dwa zapisy - żeby zobaczyć wynik terminalu

def get_poster_url(poster_api_path, size='W342'):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    try:
        response.raise_for_status()
    except HTTPError:
        return get_movies_list(list_type='popular')
    return response.json()

def get_movies3(how_many, list_type):       
    alfa = get_movies_list(list_type)
    gamma = random.sample(alfa['results'], len(alfa['results']))
    return gamma[:how_many]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"] # a czemu ten dopisek? Tworzymy cały czas jeden plik .json i wybieramy konkretne klucze z wartościami?

