#!/usr/bin/env python3
"""Parameterize and patch as decorators
"""
import requests
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """test GithubOrgClient class
    """
    @parameterized.expand([('google',), ('abc',)])
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        """
        test org method
        """

        obj = GithubOrgClient(org_name)
        res = obj.org
        ress = obj.org
        mock.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
