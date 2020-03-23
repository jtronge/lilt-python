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

import pylilt
from models.qa_rule_matches import QARuleMatches  # noqa: E501
from pylilt.rest import ApiException


class TestQARuleMatches(unittest.TestCase):
    """QARuleMatches unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testQARuleMatches(self):
        """Test QARuleMatches"""
        # FIXME: construct object with mandatory attributes with example values
        # model = pylilt.models.qa_rule_matches.QARuleMatches()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
