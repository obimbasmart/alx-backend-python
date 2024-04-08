#!/usr/bin/env python3

"""Parameterize a unit test
"""

import unittest
from unittest.mock import (patch, MagicMock)
from parameterized import parameterized
from utils import access_nested_map, get_json
from typing import (
    Mapping,
    Sequence,
    Dict,
    Any
)


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any):
        """test nested map"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_err):
        """test KeyError"""
        with self.assertRaises(expected_err):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests')
    def test_get_json(self, test_url: str, payload: Dict, mocked_request):
        """test get_json"""

        mock_response = MagicMock()
        mock_response.json.return_value = payload
        mocked_request.get.return_value = mock_response

        self.assertEqual(get_json(test_url), payload)
