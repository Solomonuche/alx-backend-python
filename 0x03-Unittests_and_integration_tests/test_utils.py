#!/usr/bin/env python3
"""
A module for testing utils module
"""
import requests
import unittest
from unittest.mock import patch
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Tests the `access_nested_map` function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """Tests `access_nested_map`'s output"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
        ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """Tests `access_nested_map`'s exception raising."""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Mock HTTP calls
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch.object(requests, 'get')
    def test_get_json(self, url: str, payload: Dict, mock_get: Mock) -> None:
        """
        test_get_json method
        """
        mock_get.return_value.json.return_value = payload
        result = get_json(url)

        # assert that the mocked request is calld once with a url
        mock_get.assert_called_once_with(url)
        self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    """
    Parameterize and patch
    """
    def test_memoize(self):
        """
        test_memoize
        """
        class TestClass:
            """
            test class
            """
            def a_method(self):
                """
                return 42
                """
                return 42

            @memoize
            def a_property(self):
                """ return a method
                """
                return self.a_method()

        obj = TestClass()
        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            res_1 = obj.a_property
            res_2 = obj.a_property

            self.assertEqual(res_1, 42)
            self.assertEqual(res_2, 42)
            mock.assert_called_once()
