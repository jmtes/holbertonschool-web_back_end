#!/usr/bin/env python3
''' Testing suite for utils.py. '''

from unittest import TestCase, mock
from parameterized import parameterized
from sys import modules
from utils import access_nested_map, get_json, requests, memoize


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

        with mock.patch('requests.get', return_value=mock_res):
            res_json = get_json(url)
            mock_res.json.assert_called_once()
            self.assertEqual(res_json, payload)


class TestMemoize(TestCase):
    ''' Test utils.memoize '''

    def test_memoize(self):
        ''' Test utils.memoize '''

        class TestClass:
            ''' Test class. '''

            def a_method(self):
                ''' Return 42 '''
                return 42

            @memoize
            def a_property(self):
                ''' Return memoized property '''
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method', return_value=42) as p:
            tc = TestClass()

            am_return = tc.a_property
            am_return = tc.a_property

            self.assertEqual(am_return, 42)
            p.assert_called_once()
