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
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


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


@parameterized_class(['org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'], TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """"Test Integration"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.get_patcher = patch('requests.get', side_effect=[
            cls.org_payload, cls.repos_payload
        ])
        cls.mocked_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        """test public repos """

    def test_public_repos_with_license(self):
        """test public with license"""
