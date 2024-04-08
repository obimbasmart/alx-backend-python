#!/usr/bin/env python3

"""Test client
"""
import unittest
from unittest.mock import (
    MagicMock,
    patch
)
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test client"""

    @parameterized.expand([
        ("Google", {}),
        ("abc", {})
    ])
    @patch("client.get_json")
    def test_org(self, org_name, expected, mocked_get_json):
        """test org"""

        github_org = GithubOrgClient(org_name)
        mocked_get_json.return_value = MagicMock(expected)
        result = github_org.org()
        self.assertIsInstance(result, dict)
        mocked_get_json.assert_called_with(
            github_org.ORG_URL.format(org=org_name))
        mocked_get_json.assert_called_once()
