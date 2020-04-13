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
from lilt.models.qa_rule_matches_matches import QARuleMatchesMatches  # noqa: E501
from lilt.rest import ApiException

class TestQARuleMatchesMatches(unittest.TestCase):
    """QARuleMatchesMatches unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test QARuleMatchesMatches
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = lilt.models.qa_rule_matches_matches.QARuleMatchesMatches()  # noqa: E501
        if include_optional :
            return QARuleMatchesMatches(
                context = lilt.models.qa_rule_matches_context.QARuleMatches_context(
                    length = 7, 
                    offset = 19, 
                    text = 'This segment has a speling mistake', ), 
                length = 7, 
                message = 'Possible spelling mistake found', 
                offset = 19, 
                replacements = [], 
                rule = lilt.models.qa_rule_matches_rule.QARuleMatches_rule(
                    category = lilt.models.qa_rule_matches_rule_category.QARuleMatches_rule_category(
                        id = 'TYPOS', 
                        name = 'Possible Typo', ), 
                    description = 'Possible spelling mistake', 
                    id = 'MORFOLOGIK_RULE_EN_US', 
                    issue_type = 'misspelling', 
                    sub_id = '0', 
                    urls = [], ), 
                short_message = 'Spelling mistake'
            )
        else :
            return QARuleMatchesMatches(
                context = lilt.models.qa_rule_matches_context.QARuleMatches_context(
                    length = 7, 
                    offset = 19, 
                    text = 'This segment has a speling mistake', ),
                length = 7,
                message = 'Possible spelling mistake found',
                offset = 19,
                replacements = [],
        )

    def testQARuleMatchesMatches(self):
        """Test QARuleMatchesMatches"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
