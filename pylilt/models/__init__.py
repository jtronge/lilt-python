# coding: utf-8

# flake8: noqa
"""
    Lilt REST API

    The Lilt REST API enables programmatic access to the full-range of Lilt backend services including:   * Training of and translating with interactive, adaptive machine translation   * Large-scale translation memory   * The Lexicon (a large-scale termbase)   * Programmatic control of the Lilt CAT environment   * Translation memory synchronization  Requests and responses are in JSON format. The REST API only responds to HTTPS / SSL requests. ## Authentication Requests are authenticated via REST API key, which requires the Business plan.  Requests are authenticated using [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Add your REST API key as both the `username` and `password`.  For development, you may also pass the REST API key via the `key` query parameter. This is less secure than HTTP Basic Auth, and is not recommended for production use.   # noqa: E501

    OpenAPI spec version: v2.0
    Contact: support@lilt.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from pylilt.models.document_pretranslating import DocumentPretranslating
from pylilt.models.document_with_segments import DocumentWithSegments
from pylilt.models.document_without_segments import DocumentWithoutSegments
from pylilt.models.error import Error
from pylilt.models.file import File
from pylilt.models.lexicon_entry import LexiconEntry
from pylilt.models.match_band import MatchBand
from pylilt.models.memory import Memory
from pylilt.models.project import Project
from pylilt.models.project_quote import ProjectQuote
from pylilt.models.project_status import ProjectStatus
from pylilt.models.qa_rule_matches import QARuleMatches
from pylilt.models.resource_status import ResourceStatus
from pylilt.models.segment import Segment
from pylilt.models.tagged_segment import TaggedSegment
from pylilt.models.translation import Translation
from pylilt.models.translation_list import TranslationList
from pylilt.models.translation_memory_entry import TranslationMemoryEntry
