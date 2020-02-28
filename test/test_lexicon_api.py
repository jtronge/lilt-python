# coding: utf-8

"""
    Lilt REST API

    The Lilt REST API enables programmatic access to the full-range of Lilt backend services including:   * Training of and translating with interactive, adaptive machine translation   * Large-scale translation memory   * The Lexicon (a large-scale termbase)   * Programmatic control of the Lilt CAT environment   * Translation memory synchronization  Requests and responses are in JSON format. The REST API only responds to HTTPS / SSL requests. ## Authentication Requests are authenticated via REST API key, which requires the Business plan.  Requests are authenticated using [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Add your REST API key as both the `username` and `password`.  For development, you may also pass the REST API key via the `key` query parameter. This is less secure than HTTP Basic Auth, and is not recommended for production use.   # noqa: E501

    OpenAPI spec version: v2.0
    Contact: support@lilt.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.lexicon_api import LexiconApi  # noqa: E501
from swagger_client.rest import ApiException


class TestLexiconApi(unittest.TestCase):
    """LexiconApi unit test stubs"""

    def setUp(self):
        self.api = api.lexicon_api.LexiconApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_query_lexicon(self):
        """Test case for query_lexicon

        Query a Lexicon  # noqa: E501
        """
        pass

    def test_update_lexicon(self):
        """Test case for update_lexicon

        Update a Lexicon  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
