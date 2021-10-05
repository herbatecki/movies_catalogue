from flask import Flask, render_template
import tmdb_client

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = tmdb_client.get_popular_movies()["results"][:12]
    return render_template('homepage.html', movies=movies)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.context_processor
def get_movie_info():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    def tmdb_popular_title(title):
        return tmdb_client.get_poster_url(title)
    return {"tmdb_popular_title": tmdb_popular_title, "tmdb_image_url": tmdb_image_url}


if __name__ == '__main__':
    app.run(debug=True)