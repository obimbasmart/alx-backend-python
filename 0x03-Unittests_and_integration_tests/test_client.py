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
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, name, mocked_get_json):
        """Test that Github client returns correct value"""
        endpoint = 'https://api.github.com/orgs/{}'.format(name)
        github_org = GithubOrgClient(name)
        github_org.org()
        mocked_get_json.assert_called_once_with(endpoint)

    def test_public_repos_url(self):
        """---- -- -----"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mocked_prop:
            mocked_prop.return_value = {"repos_url": "www"}
            result = GithubOrgClient("Google")._public_repos_url
            self.assertEqual(result, "www")

    @patch("client.get_json")
    def test_public_repos(self, mocked_get_json):
        """---- - -------"""
        payload = [{"name": "NBC"}, {"name": "PG"}]
        mocked_get_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_prop:
            mocked_prop.return_value = "example.com"
            result = GithubOrgClient("Google").public_repos()
            self.assertEqual(result, ["NBC", "PG"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict, license_key: str, expected: bool):
        """--- --- ---"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)
