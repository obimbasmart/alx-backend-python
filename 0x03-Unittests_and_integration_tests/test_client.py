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
        result = github_org.org()
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

    @patch("client.get_json")
    def test_public_repos(self, mocked_get_json):
        """test public repos"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mocked_prop:
            mocked_prop.return_value = {"repos_url": "www"}
            mocked_get_json.return_value = MagicMock(return_value={})
            result = GithubOrgClient("Google").public_repos()
            self.assertEqual(result, [])
