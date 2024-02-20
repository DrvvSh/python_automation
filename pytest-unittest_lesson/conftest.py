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