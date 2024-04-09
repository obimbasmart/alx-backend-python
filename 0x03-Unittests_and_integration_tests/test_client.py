#!/usr/bin/env python3

"""Test client
"""
import unittest
from unittest.mock import (
    MagicMock,
    patch,
    PropertyMock
)
from typing import Dict, Callable
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test client"""

    @parameterized.expand([
        ("Google", {}),
        ("abc", {})
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, expected: Dict, mocked_get_json):
        """test org"""

        github_org = GithubOrgClient(org_name)
        mocked_get_json.return_value = MagicMock(expected)
        result = github_org.org()
        self.assertIsInstance(result, dict)
        mocked_get_json.assert_called_with(
            github_org.ORG_URL.format(org=org_name))
        mocked_get_json.assert_called_once()

    def test_public_repos_url(self):
        """test public repos url"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mocked_prop:
            mocked_prop.return_value = {"repos_url": "www"}
            result = GithubOrgClient("Google")._public_repos_url
            self.assertEqual(result, "www")
