#!/usr/bin/env python3
"""Parameterize and patch as decorators
"""
import requests
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """test GithubOrgClient class
    """
    @parameterized.expand([('google',), ('abc',)])
    def test_org(self, org_name):
        """
        test org method
        """
        obj = GithubOrgClient(org_name)
        with patch.object(GithubOrgClient, 'org') as mock:
            res = obj.org()
            mock.assert_called_once()
