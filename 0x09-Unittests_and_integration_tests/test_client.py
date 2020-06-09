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
    def test_org(self, org_name):
        ''' Test GithubOrgClient.org() '''

        goc = client.GithubOrgClient(org_name)

        with mock.patch('client.get_json') as m:
            goc.org()
            m.assert_called_once_with(
                'https://api.github.com/orgs/{}'.format(org_name))
