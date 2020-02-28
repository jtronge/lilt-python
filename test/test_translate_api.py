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
from api.translate_api import TranslateApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTranslateApi(unittest.TestCase):
    """TranslateApi unit test stubs"""

    def setUp(self):
        self.api = api.translate_api.TranslateApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_register_segment(self):
        """Test case for register_segment

        Register a segment  # noqa: E501
        """
        pass

    def test_translate_segment(self):
        """Test case for translate_segment

        Translate a segment  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
