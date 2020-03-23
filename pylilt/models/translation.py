# coding: utf-8

"""
    Lilt REST API

    The Lilt REST API enables programmatic access to the full-range of Lilt backend services including:   * Training of and translating with interactive, adaptive machine translation   * Large-scale translation memory   * The Lexicon (a large-scale termbase)   * Programmatic control of the Lilt CAT environment   * Translation memory synchronization  Requests and responses are in JSON format. The REST API only responds to HTTPS / SSL requests. ## Authentication Requests are authenticated via REST API key, which requires the Business plan.  Requests are authenticated using [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Add your REST API key as both the `username` and `password`.  For development, you may also pass the REST API key via the `key` query parameter. This is less secure than HTTP Basic Auth, and is not recommended for production use.   # noqa: E501

    OpenAPI spec version: v2.0
    Contact: support@lilt.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Translation(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'target': 'str',
        'target_with_tags': 'str',
        'align': 'str',
        'provenance': 'str',
        'score': 'float',
        'is_tm_match': 'bool',
        'target_delimiters': 'list[str]',
        'target_words': 'list[str]'
    }

    attribute_map = {
        'target': 'target',
        'target_with_tags': 'targetWithTags',
        'align': 'align',
        'provenance': 'provenance',
        'score': 'score',
        'is_tm_match': 'isTMMatch',
        'target_delimiters': 'targetDelimiters',
        'target_words': 'targetWords'
    }

    def __init__(self, target=None, target_with_tags=None, align=None, provenance=None, score=None, is_tm_match=None, target_delimiters=None, target_words=None):  # noqa: E501
        """Translation - a model defined in Swagger"""  # noqa: E501
        self._target = None
        self._target_with_tags = None
        self._align = None
        self._provenance = None
        self._score = None
        self._is_tm_match = None
        self._target_delimiters = None
        self._target_words = None
        self.discriminator = None
        if target is not None:
            self.target = target
        if target_with_tags is not None:
            self.target_with_tags = target_with_tags
        if align is not None:
            self.align = align
        if provenance is not None:
            self.provenance = provenance
        if score is not None:
            self.score = score
        if is_tm_match is not None:
            self.is_tm_match = is_tm_match
        if target_delimiters is not None:
            self.target_delimiters = target_delimiters
        if target_words is not None:
            self.target_words = target_words

    @property
    def target(self):
        """Gets the target of this Translation.  # noqa: E501

        The target string.  # noqa: E501

        :return: The target of this Translation.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this Translation.

        The target string.  # noqa: E501

        :param target: The target of this Translation.  # noqa: E501
        :type: str
        """

        self._target = target

    @property
    def target_with_tags(self):
        """Gets the target_with_tags of this Translation.  # noqa: E501

        The target string with source tags projected into the target.  # noqa: E501

        :return: The target_with_tags of this Translation.  # noqa: E501
        :rtype: str
        """
        return self._target_with_tags

    @target_with_tags.setter
    def target_with_tags(self, target_with_tags):
        """Sets the target_with_tags of this Translation.

        The target string with source tags projected into the target.  # noqa: E501

        :param target_with_tags: The target_with_tags of this Translation.  # noqa: E501
        :type: str
        """

        self._target_with_tags = target_with_tags

    @property
    def align(self):
        """Gets the align of this Translation.  # noqa: E501

        \"MT only: A whitespace delimited list of source-target alignment indices.\"   # noqa: E501

        :return: The align of this Translation.  # noqa: E501
        :rtype: str
        """
        return self._align

    @align.setter
    def align(self, align):
        """Sets the align of this Translation.

        \"MT only: A whitespace delimited list of source-target alignment indices.\"   # noqa: E501

        :param align: The align of this Translation.  # noqa: E501
        :type: str
        """

        self._align = align

    @property
    def provenance(self):
        """Gets the provenance of this Translation.  # noqa: E501

        Positive values indicate that the word is from the Memory, with contiguous identical entries (e.g., 2 2) indicating phrase matches. Negative contiguous values indicate entries from the Lexicon. 0 indicates a word from the background data.   # noqa: E501

        :return: The provenance of this Translation.  # noqa: E501
        :rtype: str
        """
        return self._provenance

    @provenance.setter
    def provenance(self, provenance):
        """Sets the provenance of this Translation.

        Positive values indicate that the word is from the Memory, with contiguous identical entries (e.g., 2 2) indicating phrase matches. Negative contiguous values indicate entries from the Lexicon. 0 indicates a word from the background data.   # noqa: E501

        :param provenance: The provenance of this Translation.  # noqa: E501
        :type: str
        """

        self._provenance = provenance

    @property
    def score(self):
        """Gets the score of this Translation.  # noqa: E501

        The score of the translation.  # noqa: E501

        :return: The score of this Translation.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this Translation.

        The score of the translation.  # noqa: E501

        :param score: The score of this Translation.  # noqa: E501
        :type: float
        """

        self._score = score

    @property
    def is_tm_match(self):
        """Gets the is_tm_match of this Translation.  # noqa: E501

        TM only: If true, indicates an exact translation memory match.  # noqa: E501

        :return: The is_tm_match of this Translation.  # noqa: E501
        :rtype: bool
        """
        return self._is_tm_match

    @is_tm_match.setter
    def is_tm_match(self, is_tm_match):
        """Sets the is_tm_match of this Translation.

        TM only: If true, indicates an exact translation memory match.  # noqa: E501

        :param is_tm_match: The is_tm_match of this Translation.  # noqa: E501
        :type: bool
        """

        self._is_tm_match = is_tm_match

    @property
    def target_delimiters(self):
        """Gets the target_delimiters of this Translation.  # noqa: E501

        A format string that indicates, for each word, if the word should be preceded by a space.  # noqa: E501

        :return: The target_delimiters of this Translation.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_delimiters

    @target_delimiters.setter
    def target_delimiters(self, target_delimiters):
        """Sets the target_delimiters of this Translation.

        A format string that indicates, for each word, if the word should be preceded by a space.  # noqa: E501

        :param target_delimiters: The target_delimiters of this Translation.  # noqa: E501
        :type: list[str]
        """

        self._target_delimiters = target_delimiters

    @property
    def target_words(self):
        """Gets the target_words of this Translation.  # noqa: E501

        A list of target words corresponding with the same dimension as  `targetDelimiters`. The target string can be constructed by prefixing each word with its corresponding value in `targetDelimiters`, and then concatenating the words.   # noqa: E501

        :return: The target_words of this Translation.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_words

    @target_words.setter
    def target_words(self, target_words):
        """Sets the target_words of this Translation.

        A list of target words corresponding with the same dimension as  `targetDelimiters`. The target string can be constructed by prefixing each word with its corresponding value in `targetDelimiters`, and then concatenating the words.   # noqa: E501

        :param target_words: The target_words of this Translation.  # noqa: E501
        :type: list[str]
        """

        self._target_words = target_words

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Translation, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Translation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
