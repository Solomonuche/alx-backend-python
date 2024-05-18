#!/usr/bin/env python3
"""
Parameterize and patch as decorators
"""
import requests
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    test GithubOrgClient class
    """

    @parameterized.expand([('google'), ('abc')])
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        """
        test org method
        """

        obj = GithubOrgClient(org_name)
        obj.org()
        obj.org()
        mock.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """
        test_public_repos_url
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "https://api.github.com/orgs/abc"}
            mock.return_value = payload

            client = GithubOrgClient("abc")
            client.org
            url = {"repos_url": client._public_repos_url}
            mock.assert_called()
            self.assertEqual(url, payload)
