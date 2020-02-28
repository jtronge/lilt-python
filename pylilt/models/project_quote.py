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


class ProjectQuote(object):
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
        'id': 'int',
        'num_source_words': 'int',
        'num_words_new': 'int',
        'num_segments_new': 'int',
        'num_words_repetition': 'int',
        'num_segments_repetition': 'int',
        'resources': 'list[MatchBand]'
    }

    attribute_map = {
        'id': 'id',
        'num_source_words': 'num_source_words',
        'num_words_new': 'num_words_new',
        'num_segments_new': 'num_segments_new',
        'num_words_repetition': 'num_words_repetition',
        'num_segments_repetition': 'num_segments_repetition',
        'resources': 'resources'
    }

    def __init__(self, id=None, num_source_words=None, num_words_new=None, num_segments_new=None, num_words_repetition=None, num_segments_repetition=None, resources=None):  # noqa: E501
        """ProjectQuote - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._num_source_words = None
        self._num_words_new = None
        self._num_segments_new = None
        self._num_words_repetition = None
        self._num_segments_repetition = None
        self._resources = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if num_source_words is not None:
            self.num_source_words = num_source_words
        if num_words_new is not None:
            self.num_words_new = num_words_new
        if num_segments_new is not None:
            self.num_segments_new = num_segments_new
        if num_words_repetition is not None:
            self.num_words_repetition = num_words_repetition
        if num_segments_repetition is not None:
            self.num_segments_repetition = num_segments_repetition
        if resources is not None:
            self.resources = resources

    @property
    def id(self):
        """Gets the id of this ProjectQuote.  # noqa: E501

        A unique Project identifier.  # noqa: E501

        :return: The id of this ProjectQuote.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectQuote.

        A unique Project identifier.  # noqa: E501

        :param id: The id of this ProjectQuote.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def num_source_words(self):
        """Gets the num_source_words of this ProjectQuote.  # noqa: E501

        The number of source words in the Project.  # noqa: E501

        :return: The num_source_words of this ProjectQuote.  # noqa: E501
        :rtype: int
        """
        return self._num_source_words

    @num_source_words.setter
    def num_source_words(self, num_source_words):
        """Sets the num_source_words of this ProjectQuote.

        The number of source words in the Project.  # noqa: E501

        :param num_source_words: The num_source_words of this ProjectQuote.  # noqa: E501
        :type: int
        """

        self._num_source_words = num_source_words

    @property
    def num_words_new(self):
        """Gets the num_words_new of this ProjectQuote.  # noqa: E501

        The number of new source words in the Project.  # noqa: E501

        :return: The num_words_new of this ProjectQuote.  # noqa: E501
        :rtype: int
        """
        return self._num_words_new

    @num_words_new.setter
    def num_words_new(self, num_words_new):
        """Sets the num_words_new of this ProjectQuote.

        The number of new source words in the Project.  # noqa: E501

        :param num_words_new: The num_words_new of this ProjectQuote.  # noqa: E501
        :type: int
        """

        self._num_words_new = num_words_new

    @property
    def num_segments_new(self):
        """Gets the num_segments_new of this ProjectQuote.  # noqa: E501

        The number of new segments in the Project.  # noqa: E501

        :return: The num_segments_new of this ProjectQuote.  # noqa: E501
        :rtype: int
        """
        return self._num_segments_new

    @num_segments_new.setter
    def num_segments_new(self, num_segments_new):
        """Sets the num_segments_new of this ProjectQuote.

        The number of new segments in the Project.  # noqa: E501

        :param num_segments_new: The num_segments_new of this ProjectQuote.  # noqa: E501
        :type: int
        """

        self._num_segments_new = num_segments_new

    @property
    def num_words_repetition(self):
        """Gets the num_words_repetition of this ProjectQuote.  # noqa: E501

        The number of repetition source words in the Project.  # noqa: E501

        :return: The num_words_repetition of this ProjectQuote.  # noqa: E501
        :rtype: int
        """
        return self._num_words_repetition

    @num_words_repetition.setter
    def num_words_repetition(self, num_words_repetition):
        """Sets the num_words_repetition of this ProjectQuote.

        The number of repetition source words in the Project.  # noqa: E501

        :param num_words_repetition: The num_words_repetition of this ProjectQuote.  # noqa: E501
        :type: int
        """

        self._num_words_repetition = num_words_repetition

    @property
    def num_segments_repetition(self):
        """Gets the num_segments_repetition of this ProjectQuote.  # noqa: E501

        The number of repetition segments in the Project.  # noqa: E501

        :return: The num_segments_repetition of this ProjectQuote.  # noqa: E501
        :rtype: int
        """
        return self._num_segments_repetition

    @num_segments_repetition.setter
    def num_segments_repetition(self, num_segments_repetition):
        """Sets the num_segments_repetition of this ProjectQuote.

        The number of repetition segments in the Project.  # noqa: E501

        :param num_segments_repetition: The num_segments_repetition of this ProjectQuote.  # noqa: E501
        :type: int
        """

        self._num_segments_repetition = num_segments_repetition

    @property
    def resources(self):
        """Gets the resources of this ProjectQuote.  # noqa: E501

        A list of MatchBand objects that represent translation memory leverage statistics.  # noqa: E501

        :return: The resources of this ProjectQuote.  # noqa: E501
        :rtype: list[MatchBand]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ProjectQuote.

        A list of MatchBand objects that represent translation memory leverage statistics.  # noqa: E501

        :param resources: The resources of this ProjectQuote.  # noqa: E501
        :type: list[MatchBand]
        """

        self._resources = resources

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
        if issubclass(ProjectQuote, dict):
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
        if not isinstance(other, ProjectQuote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other