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
    def test_access_nested_map(self, input_map, input_path, expected_output):
        ''' Test utils.access_nested_map '''
        actual = access_nested_map(input_map, input_path)
        self.assertEqual(actual, expected_output)
