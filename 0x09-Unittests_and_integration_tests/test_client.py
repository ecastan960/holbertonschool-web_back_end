#!/usr/bin/env python3
"""_summary_
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError


class TestGithubOrgClient(unittest.TestCase):
    """_summary_"""
    @parameterized.expand([
        ("google"),
        ("abc"),
        ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name, mock_get):
        """_summary_"""
        test_client = GithubOrgClient(org_name)
        test_return = test_client.org
        self.assertEqual(test_return, mock_get.return_value)

    def test_public_repos_url(self):
        """_summary_"""
        with patch.object(GithubOrgClient, "org", new_callable=PropertyMock,
                          return_value={"repos_url": "holberton"}) as mock_get:
            test_json = {"repos_url": "holberton"}
            test_client = GithubOrgClient(test_json.get("repos_url"))
            test_return = test_client._public_repos_url
            mock_get.assert_called_once
            self.assertEqual(test_return,
                             mock_get.return_value.get("repos_url"))

    @patch("client.get_json", return_value=[{"name": "holberton"}])
    def test_public_repos(self, mock_get):
        """_summary_"""
        with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as mock_pub:
            test_client = GithubOrgClient("hoberton")
            test_return = test_client.public_repos()
            self.assertEqual(test_return, ["holberton"])
            mock_get.assert_called_once
            mock_pub.assert_called_once

    """_summary_

    Returns:
        _type_: _description_
    """
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ])
    def test_has_license(self, repo, license_key, expected_return):
        """_summary_"""
        test_client = GithubOrgClient("holberton")
        test_return = test_client.has_license(repo, license_key)
        self.assertEqual(expected_return, test_return)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """_summary_"""
    @classmethod
    def setUpClass(cls):
        """_summary_"""
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """_summary_"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """_summary_"""
        test_class = GithubOrgClient("holberton")
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("random"), [])

    def test_public_repos_with_license(self):
        """_summary_"""
        test_class = GithubOrgClient("holberton")
        self.assertEqual(test_class.public_repos(license="apache-2.0"),
                         self.apache2_repos)
