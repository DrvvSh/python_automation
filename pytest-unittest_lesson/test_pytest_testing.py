import pytest
import requests

@pytest.fixture(scope='session')
def pre_post():
    print()
    print('---START---')
    yield None
    print()
    print('---END---')

@pytest.fixture()
def new_post_id():
    body = {"title": "foo", "body": "bar", "userId": 1}
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json = body, headers = headers)
    post_id = response.json()['id']
    yield post_id
    print()
    print('---Deleting the post---')
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')


def test_get_one_post(new_post_id, pre_post):
    print()
    print('---GET ONE POST started---')
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    assert response['id'] == new_post_id


def test_get_all_posts():
    print()
    print('---GET ALL POSTS started---')
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100, 'Not all posts returned'


def test_make_a_post():
    print()
    print('---MAKE A POST started---')
    body = {"title": "foo", "body": "bar", "userId": 1}
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json = body, headers = headers)
    assert response.status_code == 201, 'Status code is incorrect'
    assert response.json()['id'] == 101, 'Id is incorrect'
