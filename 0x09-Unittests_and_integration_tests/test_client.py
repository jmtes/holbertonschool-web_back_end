#!/usr/bin/env python3
''' Test client.py '''

from unittest import TestCase, mock
from parameterized import parameterized
import client


class TestGithubOrgClient(TestCase):
    ''' Test class GithubOrgClient '''

    @parameterized.expand([
        ('buttercup'),
        ('verne'),
        ('koi')
    ])
    @mock.patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        ''' Test GithubOrgClient.org() '''

        goc = client.GithubOrgClient(org_name)

        goc.org()
        mock_get_json.assert_called_once_with(
            'https://api.github.com/orgs/{}'.format(org_name))
