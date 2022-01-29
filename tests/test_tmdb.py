import tmdb_client

def test_get_poster_url_uses_default_size():
    # przygotowanie danych
    poster_api_path = "some-poster-path"
    expected_default_size = 'w342'
    # wywolanie kodu, ktory testujemy
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    # Porównanie wyników
    # assert expected_default_size in poster_url
    assert poster_url == "https://image.tmdb.org/t/p/w342/some-poster-path" # też ten sposób działa, bardziej konkretne porównanie z dokładnym adresem

def test_get_movies_list_popular():
    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list is not None


# ----- przykład insidowy na abstrakcyjnych danych niezwiązanych z zadaniem -------
def some_function_to_mock():
    raise Exception("Original was called")

from unittest.mock import Mock

def test_mocking(monkeypatch):
   my_mock = Mock()
   my_mock.return_value = 2
   monkeypatch.setattr("tests.test_tmdb.some_function_to_mock", my_mock)
   result = some_function_to_mock()
   assert result == 2
# ----- koniec przykładu ---------

def test_get_movies_list(monkeypatch):
    # lista, która bedzie zwracać przysłonięte "zapytanie do API"
    mock_movies_list = ['Movie 1', 'Movie 2']

    requests_mock = Mock()
    # wynik wywołania zapytania do API
    response = requests_mock.return_value
    # przysłaniay wynik wywołania metody .json()
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list == mock_movies_list
    # assert movies_list == ['Movie 1', 'Movie 3'] - # to sprawdzenie da błąd, bo jest "Movie 3" miast "Movie 2"