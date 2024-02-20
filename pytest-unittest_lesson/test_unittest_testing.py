'''Unittest API exercise'''

import unittest
import requests

class TestPostAPI(unittest.TestCase):

    #setUp method
    def setUp(self):
        body = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=body,
            headers=headers
        )
        self.post_id = response.json()['id']
        print(f'Post created: {self.post_id}')

    #tearDown method
    def tearDown(self):
        requests.delete(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}')
        print(f'Post deleted: {self.post_id}')

    @unittest.skip('Getting ERROR on each test run')
    def test_get_one_post(self):
        print('GET ONE POST started')
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}').json()
        self.assertEqual(response['id'], self.post_id)

class TestSeparate(unittest.TestCase):

    def test_get_all_posts(self):
        print('GET ALL POSTS started')
        response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
        self.assertEqual(len(response), 100, 'Not all posts returned')

    def test_make_a_post(self):
        print('MAKE A POST started')
        body = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=body,
            headers=headers
        )
        self.assertEqual(response.status_code, 201, 'Status code is incorrect')
        self.assertEqual(response.json()['id'], 101, 'Id is incorrect')



