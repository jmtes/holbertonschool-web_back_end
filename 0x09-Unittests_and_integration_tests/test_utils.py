#!/usr/bin/env python3
''' Testing suite for utils.py. '''

from unittest import TestCase, mock
from parameterized import parameterized
from utils import access_nested_map, get_json, requests


class TestAccessNestedMap(TestCase):
    ''' Test utils.access_nested_map '''

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, map, path, expected):
        ''' Test utils.access_nested_map '''
        actual = access_nested_map(map, path)
        self.assertEqual(actual, expected)

    @parameterized.expand([
        ({}, ('a',), 'a'),
        ({'a': 1}, ('a', 'b'), 'b')
    ])
    def test_access_nested_map_exception(
            self, map, path, expected):
        ''' Test utils.access_nested_map exceptions. '''
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(expected, str(e.exception))


class TestGetJson(TestCase):
    ''' Test utils.get_json '''

    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    def test_get_json(self, url, payload):
        ''' Test utils.get_json '''

        mock_res = mock.Mock()
        mock_res.json.return_value = payload

        def mock_get(url):
            ''' Mock requests.get '''
            return mock_res

        with mock.patch('requests.get', side_effect=mock_get):
            res_json = get_json(url)
            mock_res.json.assert_called_once()
            self.assertEqual(res_json, payload)
