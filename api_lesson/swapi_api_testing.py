import requests

BASE_URL = 'https://swapi.dev/api/'


def get_films():
    response = requests.get('https://swapi.dev/api/films/').json()
    print(response)


def options_films():
    response = requests.options('https://swapi.dev/api/films/').json()
    print(response)


def get_character():
    response = requests.get('https://swapi.dev/api/people/1/').json()
    print(response)

# calling
get_films()
options_films()
get_character()