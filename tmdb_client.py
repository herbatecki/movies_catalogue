import requests
import json
import random
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



def get_movies(how_many):       # do wersji bez list
    data = get_popular_movies()
    beta = random.sample(data['results'], len(data['results'])) # wziąłem z komunikatora , dlaczego i jak to działa? :D a random.shuffle czy .choices nie?
    return beta[:how_many]

# print(type(get_popular_movies())) # - to jest słownik
# print(type(get_movies(1)))  # a to już lista?

def get_movies2(list_type='popular', how_many=8): # funkcja dla list
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f'Bearer {API_TOKEN}'
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data # wzięte z pewną modyfikacją z czatu, tj. bez sortowania i z odrzucenie w reurnie slicem z how_many bo nie rozponował go debugger - unhashable type

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

