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


class DialectInfoOptions(object):
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
        'timezone': 'bool',
        'schema': 'bool',
        'ssl': 'bool',
        'auth': 'bool',
        'host': 'bool',
        'tmp_table': 'bool',
        'project_name': 'bool',
        'oauth_credentials': 'bool',
        'additional_params': 'bool',
        'username_required': 'bool',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'timezone': 'timezone',
        'schema': 'schema',
        'ssl': 'ssl',
        'auth': 'auth',
        'host': 'host',
        'tmp_table': 'tmp_table',
        'project_name': 'project_name',
        'oauth_credentials': 'oauth_credentials',
        'additional_params': 'additional_params',
        'username_required': 'username_required',
        'can': 'can'
    }

    def __init__(self, timezone=None, schema=None, ssl=None, auth=None, host=None, tmp_table=None, project_name=None, oauth_credentials=None, additional_params=None, username_required=None, can=None):  # noqa: E501
        """DialectInfoOptions - a model defined in Swagger"""  # noqa: E501

        self._timezone = None
        self._schema = None
        self._ssl = None
        self._auth = None
        self._host = None
        self._tmp_table = None
        self._project_name = None
        self._oauth_credentials = None
        self._additional_params = None
        self._username_required = None
        self._can = None
        self.discriminator = None

        if timezone is not None:
            self.timezone = timezone
        if schema is not None:
            self.schema = schema
        if ssl is not None:
            self.ssl = ssl
        if auth is not None:
            self.auth = auth
        if host is not None:
            self.host = host
        if tmp_table is not None:
            self.tmp_table = tmp_table
        if project_name is not None:
            self.project_name = project_name
        if oauth_credentials is not None:
            self.oauth_credentials = oauth_credentials
        if additional_params is not None:
            self.additional_params = additional_params
        if username_required is not None:
            self.username_required = username_required
        if can is not None:
            self.can = can

    @property
    def timezone(self):
        """Gets the timezone of this DialectInfoOptions.  # noqa: E501

        Has timezone support  # noqa: E501

        :return: The timezone of this DialectInfoOptions.  # noqa: E501
        :rtype: bool
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this DialectInfoOptions.

        Has timezone support  # noqa: E501

        :param timezone: The timezone of this DialectInfoOptions.  # noqa: E501
        :type: bool
        """

        self._timezone = timezone

    @property
    def schema(self):
        """Gets the schema of this DialectInfoOptions.  # noqa: E501

        Has schema support  # noqa: E501

        :return: The schema of this DialectInfoOptions.  # noqa: E501
        :rtype: bool
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this DialectInfoOptions.

        Has schema support  # noqa: E501

        :param schema: The schema of this DialectInfoOptions.  # noqa: E501
        :type: bool
        """

        self._schema = schema

    @property
    def ssl(self):
        """Gets the ssl of this DialectInfoOptions.  # noqa: E501

        Has SSL support  # noqa: E501

        :return: The ssl of this DialectInfoOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ssl

    @ssl.setter
    def ssl(self, ssl):
        """Sets the ssl of this DialectInfoOptions.

        Has SSL support  # noqa: E501

        :param ssl: The ssl of this DialectInfoOptions.  # noqa: E501
        :type: bool
        """

        self._ssl = ssl

    @property
    def auth(self):
        """Gets the auth of this DialectInfoOptions.  # noqa: E501

        Has auth support  # noqa: E501

        :return: The auth of this DialectInfoOptions.  # noqa: E501
        :rtype: bool
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this DialectInfoOptions.

        Has auth support  # noqa: E501

        :param auth: The auth of this DialectInfoOptions.  # noqa: E501
        :type: bool
        """

        self._auth = auth

    @property
    def host(self):
        """Gets the host of this DialectInfoOptions.  # noqa: E501

        Has host support  # noqa: E501

        :return: The host of this DialectInfoOptions.  # noqa: E501
        :rtype: bool
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this DialectInfoOptions.

        Has host support  # noqa: E501

        :param host: The host of this DialectInfoOptions.  # noqa: E501
        :type: bool
        """

        self._host = host

    @property
    def tmp_table(self):
        """Gets the tmp_table of this DialectInfoOptions.  # noqa: E501

        Has tmp table support  # noqa: E501

        :return: The tmp_table of this DialectInfoOptions.  # noqa: E501
        :rtype: bool
        """
        return self._tmp_table

    @tmp_table.setter
    def tmp_table(self, tmp_table):
        """Sets the tmp_table of this DialectInfoOptions.

        Has tmp table support  # noqa: E501

        :param tmp_table: The tmp_table of this DialectInfoOptions.  # noqa: E501
        :type: bool
        """

        self._tmp_table = tmp_table

    @property
    def project_name(self):
        """Gets the project_name of this DialectInfoOptions.  # noqa: E501

        Has project name support  # noqa: E501

        :return: The project_name of this DialectInfoOptions.  # noqa: E501
        :rtype: bool
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DialectInfoOptions.

        Has project name support  # noqa: E501

        :param project_name: The project_name of this DialectInfoOptions.  # noqa: E501
        :type: bool
        """

        self._project_name = project_name

    @property
    def oauth_credentials(self):
        """Gets the oauth_credentials of this DialectInfoOptions.  # noqa: E501

        Has OAuth support  # noqa: E501

        :return: The oauth_credentials of this DialectInfoOptions.  # noqa: E501
        :rtype: bool
        """
        return self._oauth_credentials

    @oauth_credentials.setter
    def oauth_credentials(self, oauth_credentials):
        """Sets the oauth_credentials of this DialectInfoOptions.

        Has OAuth support  # noqa: E501

        :param oauth_credentials: The oauth_credentials of this DialectInfoOptions.  # noqa: E501
        :type: bool
        """

        self._oauth_credentials = oauth_credentials

    @property
    def additional_params(self):
        """Gets the additional_params of this DialectInfoOptions.  # noqa: E501

        Has additional params support  # noqa: E501

        :return: The additional_params of this DialectInfoOptions.  # noqa: E501
        :rtype: bool
        """
        return self._additional_params

    @additional_params.setter
    def additional_params(self, additional_params):
        """Sets the additional_params of this DialectInfoOptions.

        Has additional params support  # noqa: E501

        :param additional_params: The additional_params of this DialectInfoOptions.  # noqa: E501
        :type: bool
        """

        self._additional_params = additional_params

    @property
    def username_required(self):
        """Gets the username_required of this DialectInfoOptions.  # noqa: E501

        Username is required  # noqa: E501

        :return: The username_required of this DialectInfoOptions.  # noqa: E501
        :rtype: bool
        """
        return self._username_required

    @username_required.setter
    def username_required(self, username_required):
        """Sets the username_required of this DialectInfoOptions.

        Username is required  # noqa: E501

        :param username_required: The username_required of this DialectInfoOptions.  # noqa: E501
        :type: bool
        """

        self._username_required = username_required

    @property
    def can(self):
        """Gets the can of this DialectInfoOptions.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this DialectInfoOptions.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this DialectInfoOptions.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this DialectInfoOptions.  # noqa: E501
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
        if not isinstance(other, DialectInfoOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
