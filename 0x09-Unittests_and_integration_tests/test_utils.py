#!/usr/bin/env python3
''' Testing suite for utils.py. '''

from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map


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
