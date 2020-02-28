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


class Memory(object):
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
        'srclang': 'str',
        'trglang': 'str',
        'srclocale': 'str',
        'trglocale': 'str',
        'name': 'str',
        'version': 'int',
        'created_at': 'int',
        'updated_at': 'int',
        'num_segments': 'int',
        'resources': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'srclang': 'srclang',
        'trglang': 'trglang',
        'srclocale': 'srclocale',
        'trglocale': 'trglocale',
        'name': 'name',
        'version': 'version',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'num_segments': 'num_segments',
        'resources': 'resources'
    }

    def __init__(self, id=None, srclang=None, trglang=None, srclocale=None, trglocale=None, name=None, version=None, created_at=None, updated_at=None, num_segments=None, resources=None):  # noqa: E501
        """Memory - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._srclang = None
        self._trglang = None
        self._srclocale = None
        self._trglocale = None
        self._name = None
        self._version = None
        self._created_at = None
        self._updated_at = None
        self._num_segments = None
        self._resources = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if srclang is not None:
            self.srclang = srclang
        if trglang is not None:
            self.trglang = trglang
        if srclocale is not None:
            self.srclocale = srclocale
        if trglocale is not None:
            self.trglocale = trglocale
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if num_segments is not None:
            self.num_segments = num_segments
        if resources is not None:
            self.resources = resources

    @property
    def id(self):
        """Gets the id of this Memory.  # noqa: E501

        A unique number identifying the Memory.  # noqa: E501

        :return: The id of this Memory.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Memory.

        A unique number identifying the Memory.  # noqa: E501

        :param id: The id of this Memory.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def srclang(self):
        """Gets the srclang of this Memory.  # noqa: E501

        An ISO 639-1 language identifier.  # noqa: E501

        :return: The srclang of this Memory.  # noqa: E501
        :rtype: str
        """
        return self._srclang

    @srclang.setter
    def srclang(self, srclang):
        """Sets the srclang of this Memory.

        An ISO 639-1 language identifier.  # noqa: E501

        :param srclang: The srclang of this Memory.  # noqa: E501
        :type: str
        """

        self._srclang = srclang

    @property
    def trglang(self):
        """Gets the trglang of this Memory.  # noqa: E501

        An ISO 639-1 language identifier.  # noqa: E501

        :return: The trglang of this Memory.  # noqa: E501
        :rtype: str
        """
        return self._trglang

    @trglang.setter
    def trglang(self, trglang):
        """Sets the trglang of this Memory.

        An ISO 639-1 language identifier.  # noqa: E501

        :param trglang: The trglang of this Memory.  # noqa: E501
        :type: str
        """

        self._trglang = trglang

    @property
    def srclocale(self):
        """Gets the srclocale of this Memory.  # noqa: E501

        An ISO 639-1 language identifier.  # noqa: E501

        :return: The srclocale of this Memory.  # noqa: E501
        :rtype: str
        """
        return self._srclocale

    @srclocale.setter
    def srclocale(self, srclocale):
        """Sets the srclocale of this Memory.

        An ISO 639-1 language identifier.  # noqa: E501

        :param srclocale: The srclocale of this Memory.  # noqa: E501
        :type: str
        """

        self._srclocale = srclocale

    @property
    def trglocale(self):
        """Gets the trglocale of this Memory.  # noqa: E501

        An ISO 639-1 language identifier.  # noqa: E501

        :return: The trglocale of this Memory.  # noqa: E501
        :rtype: str
        """
        return self._trglocale

    @trglocale.setter
    def trglocale(self, trglocale):
        """Sets the trglocale of this Memory.

        An ISO 639-1 language identifier.  # noqa: E501

        :param trglocale: The trglocale of this Memory.  # noqa: E501
        :type: str
        """

        self._trglocale = trglocale

    @property
    def name(self):
        """Gets the name of this Memory.  # noqa: E501

        A name for the Memory.  # noqa: E501

        :return: The name of this Memory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Memory.

        A name for the Memory.  # noqa: E501

        :param name: The name of this Memory.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this Memory.  # noqa: E501

        The current version of the Memory, which is the number of updates since the memory was created.  # noqa: E501

        :return: The version of this Memory.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Memory.

        The current version of the Memory, which is the number of updates since the memory was created.  # noqa: E501

        :param version: The version of this Memory.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def created_at(self):
        """Gets the created_at of this Memory.  # noqa: E501

        Time at which the object was created. Measured in seconds since the Unix epoch.  # noqa: E501

        :return: The created_at of this Memory.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Memory.

        Time at which the object was created. Measured in seconds since the Unix epoch.  # noqa: E501

        :param created_at: The created_at of this Memory.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Memory.  # noqa: E501

        Time at which the object was created. Measured in seconds since the Unix epoch.  # noqa: E501

        :return: The updated_at of this Memory.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Memory.

        Time at which the object was created. Measured in seconds since the Unix epoch.  # noqa: E501

        :param updated_at: The updated_at of this Memory.  # noqa: E501
        :type: int
        """

        self._updated_at = updated_at

    @property
    def num_segments(self):
        """Gets the num_segments of this Memory.  # noqa: E501

        The number of confirmed Segments incorporated into this Memory.  # noqa: E501

        :return: The num_segments of this Memory.  # noqa: E501
        :rtype: int
        """
        return self._num_segments

    @num_segments.setter
    def num_segments(self, num_segments):
        """Sets the num_segments of this Memory.

        The number of confirmed Segments incorporated into this Memory.  # noqa: E501

        :param num_segments: The num_segments of this Memory.  # noqa: E501
        :type: int
        """

        self._num_segments = num_segments

    @property
    def resources(self):
        """Gets the resources of this Memory.  # noqa: E501

        The resource files (translation memories and termbases) associated with this Memory.  # noqa: E501

        :return: The resources of this Memory.  # noqa: E501
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this Memory.

        The resource files (translation memories and termbases) associated with this Memory.  # noqa: E501

        :param resources: The resources of this Memory.  # noqa: E501
        :type: list[str]
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
        if issubclass(Memory, dict):
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
        if not isinstance(other, Memory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other