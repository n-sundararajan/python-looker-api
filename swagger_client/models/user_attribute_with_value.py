# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning)   # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UserAttributeWithValue(object):
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
        'name': 'str',
        'label': 'str',
        'rank': 'int',
        'value': 'str',
        'user_id': 'int',
        'user_can_edit': 'bool',
        'value_is_hidden': 'bool',
        'user_attribute_id': 'int',
        'source': 'str',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'name': 'name',
        'label': 'label',
        'rank': 'rank',
        'value': 'value',
        'user_id': 'user_id',
        'user_can_edit': 'user_can_edit',
        'value_is_hidden': 'value_is_hidden',
        'user_attribute_id': 'user_attribute_id',
        'source': 'source',
        'can': 'can'
    }

    def __init__(self, name=None, label=None, rank=None, value=None, user_id=None, user_can_edit=None, value_is_hidden=None, user_attribute_id=None, source=None, can=None):  # noqa: E501
        """UserAttributeWithValue - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._label = None
        self._rank = None
        self._value = None
        self._user_id = None
        self._user_can_edit = None
        self._value_is_hidden = None
        self._user_attribute_id = None
        self._source = None
        self._can = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if label is not None:
            self.label = label
        if rank is not None:
            self.rank = rank
        if value is not None:
            self.value = value
        if user_id is not None:
            self.user_id = user_id
        if user_can_edit is not None:
            self.user_can_edit = user_can_edit
        if value_is_hidden is not None:
            self.value_is_hidden = value_is_hidden
        if user_attribute_id is not None:
            self.user_attribute_id = user_attribute_id
        if source is not None:
            self.source = source
        if can is not None:
            self.can = can

    @property
    def name(self):
        """Gets the name of this UserAttributeWithValue.  # noqa: E501

        Name of user attribute  # noqa: E501

        :return: The name of this UserAttributeWithValue.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserAttributeWithValue.

        Name of user attribute  # noqa: E501

        :param name: The name of this UserAttributeWithValue.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def label(self):
        """Gets the label of this UserAttributeWithValue.  # noqa: E501

        Human-friendly label for user attribute  # noqa: E501

        :return: The label of this UserAttributeWithValue.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this UserAttributeWithValue.

        Human-friendly label for user attribute  # noqa: E501

        :param label: The label of this UserAttributeWithValue.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def rank(self):
        """Gets the rank of this UserAttributeWithValue.  # noqa: E501

        Precedence for setting value on user (lowest wins)  # noqa: E501

        :return: The rank of this UserAttributeWithValue.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this UserAttributeWithValue.

        Precedence for setting value on user (lowest wins)  # noqa: E501

        :param rank: The rank of this UserAttributeWithValue.  # noqa: E501
        :type: int
        """

        self._rank = rank

    @property
    def value(self):
        """Gets the value of this UserAttributeWithValue.  # noqa: E501

        Value of attribute for user  # noqa: E501

        :return: The value of this UserAttributeWithValue.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this UserAttributeWithValue.

        Value of attribute for user  # noqa: E501

        :param value: The value of this UserAttributeWithValue.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def user_id(self):
        """Gets the user_id of this UserAttributeWithValue.  # noqa: E501

        Id of User  # noqa: E501

        :return: The user_id of this UserAttributeWithValue.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserAttributeWithValue.

        Id of User  # noqa: E501

        :param user_id: The user_id of this UserAttributeWithValue.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def user_can_edit(self):
        """Gets the user_can_edit of this UserAttributeWithValue.  # noqa: E501

        Can the user set this value  # noqa: E501

        :return: The user_can_edit of this UserAttributeWithValue.  # noqa: E501
        :rtype: bool
        """
        return self._user_can_edit

    @user_can_edit.setter
    def user_can_edit(self, user_can_edit):
        """Sets the user_can_edit of this UserAttributeWithValue.

        Can the user set this value  # noqa: E501

        :param user_can_edit: The user_can_edit of this UserAttributeWithValue.  # noqa: E501
        :type: bool
        """

        self._user_can_edit = user_can_edit

    @property
    def value_is_hidden(self):
        """Gets the value_is_hidden of this UserAttributeWithValue.  # noqa: E501

        If true, the \"value\" field will be null, because the attribute settings block access to this value  # noqa: E501

        :return: The value_is_hidden of this UserAttributeWithValue.  # noqa: E501
        :rtype: bool
        """
        return self._value_is_hidden

    @value_is_hidden.setter
    def value_is_hidden(self, value_is_hidden):
        """Sets the value_is_hidden of this UserAttributeWithValue.

        If true, the \"value\" field will be null, because the attribute settings block access to this value  # noqa: E501

        :param value_is_hidden: The value_is_hidden of this UserAttributeWithValue.  # noqa: E501
        :type: bool
        """

        self._value_is_hidden = value_is_hidden

    @property
    def user_attribute_id(self):
        """Gets the user_attribute_id of this UserAttributeWithValue.  # noqa: E501

        Id of User Attribute  # noqa: E501

        :return: The user_attribute_id of this UserAttributeWithValue.  # noqa: E501
        :rtype: int
        """
        return self._user_attribute_id

    @user_attribute_id.setter
    def user_attribute_id(self, user_attribute_id):
        """Sets the user_attribute_id of this UserAttributeWithValue.

        Id of User Attribute  # noqa: E501

        :param user_attribute_id: The user_attribute_id of this UserAttributeWithValue.  # noqa: E501
        :type: int
        """

        self._user_attribute_id = user_attribute_id

    @property
    def source(self):
        """Gets the source of this UserAttributeWithValue.  # noqa: E501

        How user got this value for this attribute  # noqa: E501

        :return: The source of this UserAttributeWithValue.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this UserAttributeWithValue.

        How user got this value for this attribute  # noqa: E501

        :param source: The source of this UserAttributeWithValue.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def can(self):
        """Gets the can of this UserAttributeWithValue.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this UserAttributeWithValue.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this UserAttributeWithValue.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this UserAttributeWithValue.  # noqa: E501
        :type: dict(str, bool)
        """

        self._can = can

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserAttributeWithValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
