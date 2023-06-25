import requests
import random


# Generate a random IMDb ID
def generate_random_imdb_id():
    random_id = ''.join(random.choices('0123456789', k=7))
    return f'tt{random_id}'

API_KEY = 'e3b2f6f4'

# Fetch movie details from OMDb API using IMDb ID
def fetch_movie_details(imdb_id):
    url = f'http://www.omdbapi.com/?i={imdb_id}&apikey={API_KEY}'
    response = requests.get(url)
    return response.json()

# Fetch 10 random movies
def fetch_random_movies():
    movies = []
    while True:
        imdb_id = generate_random_imdb_id()
        movie_data = fetch_movie_details(imdb_id)
        if 'Error' not in movie_data:
            movies.append(movie_data)
        if len(movies) == 10:
            break
    return movies

def check_movie_year(func):
    def wrapper(movie):
        if int(movie['Year']) >= 2000 and int(movie['Year']) <= 2020:
            return func(movie)
        else:
            print("Movie year is not between 2000 and 2020")
    return wrapper

# Display movie details
@check_movie_year
def display_movie_details(movie):
    print('Title:', movie['Title'])
    print('Year:', movie['Year'])
    print('Genre:', movie['Genre'])
    print('---')


# Fetch and display 10 random movies
random_movies = fetch_random_movies()
for movie in random_movies:
    display_movie_details(movie)
