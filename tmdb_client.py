import requests
import json

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyYjBhNTA1ZjFhODE0MjAwYzE1NTgxZjEyNTRiYzhkNyIsInN1YiI6IjYxNTIyMzVjNjdkY2M5MDA4Y2U3MTJmMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.gLDUgiPELKhb2kjwkyq0jYUuJxaIhLtTL-J3AqT2z2M"
    headers = {
        "Authorization": f'Bearer {api_token}'
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

# dictionary = get_popular_movies()
# print(dictionary) - te dwa zapisy - żeby zobaczyć wynikw terminalu

def get_poster_url(poster_api_path, size='W342'):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"
    
