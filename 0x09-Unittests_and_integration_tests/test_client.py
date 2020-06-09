#!/usr/bin/env python3
''' Test client.py '''

from unittest import TestCase, mock
import client


class TestGithubOrgClient(TestCase):
    ''' Test class GithubOrgClient '''

    def test_org(self):
        ''' Test GithubOrgClient.org() '''

        goc = client.GithubOrgClient('buttercup')

        with mock.patch('client.get_json') as m:
            goc.org()
            m.assert_called_once_with('https://api.github.com/orgs/buttercup')
