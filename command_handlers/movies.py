import requests
from util import bot
from pymessenger import Element

API_KEY = 'b94374197eb60285181dd064d2827abc'
HOST = 'https://api.themoviedb.org/3'
IMG_PATH = 'https://image.tmdb.org/t/p/w185'

class Movies:
    def __init__(self, user_id):
        self.user_id = user_id

    def execute(self, command):
        if command == 'popular':
            movies = requests.get(HOST + '/movie/popular?api_key=' + API_KEY)
            elements = []
            for movie in movies.json()['results']:
                web_url = 'https://www.themoviedb.org/movie/{}'.format(movie['id'])
                elements.append(
                    Element(
                        title=movie['original_title'],
                        image_url=IMG_PATH + movie['poster_path'],
                        subtitle=movie['overview'],
                        item_url=web_url
                    )
                )
            bot.send_generic_message(self.user_id, elements[:10])


if __name__ == '__main__':
    movie = Movies('1479472262126245')
    print movie.execute('popular')
