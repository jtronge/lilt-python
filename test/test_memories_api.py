# coding: utf-8

"""
    Lilt REST API

    The Lilt REST API enables programmatic access to the full-range of Lilt backend services including:   * Training of and translating with interactive, adaptive machine translation   * Large-scale translation memory   * The Lexicon (a large-scale termbase)   * Programmatic control of the Lilt CAT environment   * Translation memory synchronization  Requests and responses are in JSON format. The REST API only responds to HTTPS / SSL requests. ## Authentication Requests are authenticated via REST API key, which requires the Business plan.  Requests are authenticated using [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Add your REST API key as both the `username` and `password`.  For development, you may also pass the REST API key via the `key` query parameter. This is less secure than HTTP Basic Auth, and is not recommended for production use.   # noqa: E501

    The version of the OpenAPI document: v2.0
    Contact: support@lilt.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import lilt
from lilt.api.memories_api import MemoriesApi  # noqa: E501
from lilt.rest import ApiException


class TestMemoriesApi(unittest.TestCase):
    """MemoriesApi unit test stubs"""

    def setUp(self):
        self.api = lilt.api.memories_api.MemoriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_memory(self):
        """Test case for create_memory

        Create a Memory  # noqa: E501
        """
        pass

    def test_delete_memory(self):
        """Test case for delete_memory

        Delete a Memory  # noqa: E501
        """
        pass

    def test_get_memory(self):
        """Test case for get_memory

        Retrieve a Memory  # noqa: E501
        """
        pass

    def test_import_memory_file(self):
        """Test case for import_memory_file

        File import for a Memory  # noqa: E501
        """
        pass

    def test_query_memory(self):
        """Test case for query_memory

        Query a Memory  # noqa: E501
        """
        pass

    def test_sync_delete_memory(self):
        """Test case for sync_delete_memory

        Delete-sync for a Memory  # noqa: E501
        """
        pass

    def test_sync_down_memory(self):
        """Test case for sync_down_memory

        Get-sync for a Memory  # noqa: E501
        """
        pass

    def test_sync_insert_memory(self):
        """Test case for sync_insert_memory

        Insert-sync for a Memory  # noqa: E501
        """
        pass

    def test_sync_update_memory(self):
        """Test case for sync_update_memory

        Update-sync for a Memory  # noqa: E501
        """
        pass

    def test_update_memory(self):
        """Test case for update_memory

        Update the name of a Memory  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
