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
import datetime

import lilt
from lilt.models.translation import Translation  # noqa: E501
from lilt.rest import ApiException

class TestTranslation(unittest.TestCase):
    """Translation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Translation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = lilt.models.translation.Translation()  # noqa: E501
        if include_optional :
            return Translation(
                target = '0', 
                target_with_tags = '0', 
                align = '0', 
                provenance = '0', 
                score = 1.337, 
                is_tm_match = True, 
                target_delimiters = [
                    '0'
                    ], 
                target_words = [
                    '0'
                    ]
            )
        else :
            return Translation(
        )

    def testTranslation(self):
        """Test Translation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
