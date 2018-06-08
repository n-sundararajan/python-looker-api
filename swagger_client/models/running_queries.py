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

from swagger_client.models.look_basic import LookBasic  # noqa: F401,E501
from swagger_client.models.query import Query  # noqa: F401,E501
from swagger_client.models.sql_query import SqlQuery  # noqa: F401,E501
from swagger_client.models.user_public import UserPublic  # noqa: F401,E501


class RunningQueries(object):
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
        'user': 'UserPublic',
        'query': 'Query',
        'sql_query': 'SqlQuery',
        'look': 'LookBasic',
        'created_at': 'str',
        'completed_at': 'str',
        'query_id': 'str',
        'source': 'str',
        'node_id': 'str',
        'slug': 'str',
        'query_task_id': 'str',
        'cache_key': 'str',
        'connection_name': 'str',
        'dialect': 'str',
        'connection_id': 'str',
        'message': 'str',
        'status': 'str',
        'runtime': 'float',
        'sql': 'str',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'id': 'id',
        'user': 'user',
        'query': 'query',
        'sql_query': 'sql_query',
        'look': 'look',
        'created_at': 'created_at',
        'completed_at': 'completed_at',
        'query_id': 'query_id',
        'source': 'source',
        'node_id': 'node_id',
        'slug': 'slug',
        'query_task_id': 'query_task_id',
        'cache_key': 'cache_key',
        'connection_name': 'connection_name',
        'dialect': 'dialect',
        'connection_id': 'connection_id',
        'message': 'message',
        'status': 'status',
        'runtime': 'runtime',
        'sql': 'sql',
        'can': 'can'
    }

    def __init__(self, id=None, user=None, query=None, sql_query=None, look=None, created_at=None, completed_at=None, query_id=None, source=None, node_id=None, slug=None, query_task_id=None, cache_key=None, connection_name=None, dialect=None, connection_id=None, message=None, status=None, runtime=None, sql=None, can=None):  # noqa: E501
        """RunningQueries - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._user = None
        self._query = None
        self._sql_query = None
        self._look = None
        self._created_at = None
        self._completed_at = None
        self._query_id = None
        self._source = None
        self._node_id = None
        self._slug = None
        self._query_task_id = None
        self._cache_key = None
        self._connection_name = None
        self._dialect = None
        self._connection_id = None
        self._message = None
        self._status = None
        self._runtime = None
        self._sql = None
        self._can = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user is not None:
            self.user = user
        if query is not None:
            self.query = query
        if sql_query is not None:
            self.sql_query = sql_query
        if look is not None:
            self.look = look
        if created_at is not None:
            self.created_at = created_at
        if completed_at is not None:
            self.completed_at = completed_at
        if query_id is not None:
            self.query_id = query_id
        if source is not None:
            self.source = source
        if node_id is not None:
            self.node_id = node_id
        if slug is not None:
            self.slug = slug
        if query_task_id is not None:
            self.query_task_id = query_task_id
        if cache_key is not None:
            self.cache_key = cache_key
        if connection_name is not None:
            self.connection_name = connection_name
        if dialect is not None:
            self.dialect = dialect
        if connection_id is not None:
            self.connection_id = connection_id
        if message is not None:
            self.message = message
        if status is not None:
            self.status = status
        if runtime is not None:
            self.runtime = runtime
        if sql is not None:
            self.sql = sql
        if can is not None:
            self.can = can

    @property
    def id(self):
        """Gets the id of this RunningQueries.  # noqa: E501

        Unique Id  # noqa: E501

        :return: The id of this RunningQueries.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RunningQueries.

        Unique Id  # noqa: E501

        :param id: The id of this RunningQueries.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def user(self):
        """Gets the user of this RunningQueries.  # noqa: E501

        User who initiated the query  # noqa: E501

        :return: The user of this RunningQueries.  # noqa: E501
        :rtype: UserPublic
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this RunningQueries.

        User who initiated the query  # noqa: E501

        :param user: The user of this RunningQueries.  # noqa: E501
        :type: UserPublic
        """

        self._user = user

    @property
    def query(self):
        """Gets the query of this RunningQueries.  # noqa: E501

        Query that was run  # noqa: E501

        :return: The query of this RunningQueries.  # noqa: E501
        :rtype: Query
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this RunningQueries.

        Query that was run  # noqa: E501

        :param query: The query of this RunningQueries.  # noqa: E501
        :type: Query
        """

        self._query = query

    @property
    def sql_query(self):
        """Gets the sql_query of this RunningQueries.  # noqa: E501

        SQL Query that was run  # noqa: E501

        :return: The sql_query of this RunningQueries.  # noqa: E501
        :rtype: SqlQuery
        """
        return self._sql_query

    @sql_query.setter
    def sql_query(self, sql_query):
        """Sets the sql_query of this RunningQueries.

        SQL Query that was run  # noqa: E501

        :param sql_query: The sql_query of this RunningQueries.  # noqa: E501
        :type: SqlQuery
        """

        self._sql_query = sql_query

    @property
    def look(self):
        """Gets the look of this RunningQueries.  # noqa: E501

        Look of query that was run  # noqa: E501

        :return: The look of this RunningQueries.  # noqa: E501
        :rtype: LookBasic
        """
        return self._look

    @look.setter
    def look(self, look):
        """Sets the look of this RunningQueries.

        Look of query that was run  # noqa: E501

        :param look: The look of this RunningQueries.  # noqa: E501
        :type: LookBasic
        """

        self._look = look

    @property
    def created_at(self):
        """Gets the created_at of this RunningQueries.  # noqa: E501

        Date/Time Query was initiated  # noqa: E501

        :return: The created_at of this RunningQueries.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RunningQueries.

        Date/Time Query was initiated  # noqa: E501

        :param created_at: The created_at of this RunningQueries.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def completed_at(self):
        """Gets the completed_at of this RunningQueries.  # noqa: E501

        Date/Time Query was completed  # noqa: E501

        :return: The completed_at of this RunningQueries.  # noqa: E501
        :rtype: str
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        """Sets the completed_at of this RunningQueries.

        Date/Time Query was completed  # noqa: E501

        :param completed_at: The completed_at of this RunningQueries.  # noqa: E501
        :type: str
        """

        self._completed_at = completed_at

    @property
    def query_id(self):
        """Gets the query_id of this RunningQueries.  # noqa: E501

        Query Id  # noqa: E501

        :return: The query_id of this RunningQueries.  # noqa: E501
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """Sets the query_id of this RunningQueries.

        Query Id  # noqa: E501

        :param query_id: The query_id of this RunningQueries.  # noqa: E501
        :type: str
        """

        self._query_id = query_id

    @property
    def source(self):
        """Gets the source of this RunningQueries.  # noqa: E501

        Source (look, dashboard, queryrunner, explore, etc.)  # noqa: E501

        :return: The source of this RunningQueries.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this RunningQueries.

        Source (look, dashboard, queryrunner, explore, etc.)  # noqa: E501

        :param source: The source of this RunningQueries.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def node_id(self):
        """Gets the node_id of this RunningQueries.  # noqa: E501

        Node Id  # noqa: E501

        :return: The node_id of this RunningQueries.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this RunningQueries.

        Node Id  # noqa: E501

        :param node_id: The node_id of this RunningQueries.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def slug(self):
        """Gets the slug of this RunningQueries.  # noqa: E501

        Slug  # noqa: E501

        :return: The slug of this RunningQueries.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this RunningQueries.

        Slug  # noqa: E501

        :param slug: The slug of this RunningQueries.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def query_task_id(self):
        """Gets the query_task_id of this RunningQueries.  # noqa: E501

        ID of a Query Task  # noqa: E501

        :return: The query_task_id of this RunningQueries.  # noqa: E501
        :rtype: str
        """
        return self._query_task_id

    @query_task_id.setter
    def query_task_id(self, query_task_id):
        """Sets the query_task_id of this RunningQueries.

        ID of a Query Task  # noqa: E501

        :param query_task_id: The query_task_id of this RunningQueries.  # noqa: E501
        :type: str
        """

        self._query_task_id = query_task_id

    @property
    def cache_key(self):
        """Gets the cache_key of this RunningQueries.  # noqa: E501

        Cache Key  # noqa: E501

        :return: The cache_key of this RunningQueries.  # noqa: E501
        :rtype: str
        """
        return self._cache_key

    @cache_key.setter
    def cache_key(self, cache_key):
        """Sets the cache_key of this RunningQueries.

        Cache Key  # noqa: E501

        :param cache_key: The cache_key of this RunningQueries.  # noqa: E501
        :type: str
        """

        self._cache_key = cache_key

    @property
    def connection_name(self):
        """Gets the connection_name of this RunningQueries.  # noqa: E501

        Connection  # noqa: E501

        :return: The connection_name of this RunningQueries.  # noqa: E501
        :rtype: str
        """
        return self._connection_name

    @connection_name.setter
    def connection_name(self, connection_name):
        """Sets the connection_name of this RunningQueries.

        Connection  # noqa: E501

        :param connection_name: The connection_name of this RunningQueries.  # noqa: E501
        :type: str
        """

        self._connection_name = connection_name

    @property
    def dialect(self):
        """Gets the dialect of this RunningQueries.  # noqa: E501

        Dialect  # noqa: E501

        :return: The dialect of this RunningQueries.  # noqa: E501
        :rtype: str
        """
        return self._dialect

    @dialect.setter
    def dialect(self, dialect):
        """Sets the dialect of this RunningQueries.

        Dialect  # noqa: E501

        :param dialect: The dialect of this RunningQueries.  # noqa: E501
        :type: str
        """

        self._dialect = dialect

    @property
    def connection_id(self):
        """Gets the connection_id of this RunningQueries.  # noqa: E501

        Connection ID  # noqa: E501

        :return: The connection_id of this RunningQueries.  # noqa: E501
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this RunningQueries.

        Connection ID  # noqa: E501

        :param connection_id: The connection_id of this RunningQueries.  # noqa: E501
        :type: str
        """

        self._connection_id = connection_id

    @property
    def message(self):
        """Gets the message of this RunningQueries.  # noqa: E501

        Additional Information(Error message or verbose status)  # noqa: E501

        :return: The message of this RunningQueries.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this RunningQueries.

        Additional Information(Error message or verbose status)  # noqa: E501

        :param message: The message of this RunningQueries.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def status(self):
        """Gets the status of this RunningQueries.  # noqa: E501

        Status description  # noqa: E501

        :return: The status of this RunningQueries.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RunningQueries.

        Status description  # noqa: E501

        :param status: The status of this RunningQueries.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def runtime(self):
        """Gets the runtime of this RunningQueries.  # noqa: E501

        Number of seconds elapsed running the Query  # noqa: E501

        :return: The runtime of this RunningQueries.  # noqa: E501
        :rtype: float
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this RunningQueries.

        Number of seconds elapsed running the Query  # noqa: E501

        :param runtime: The runtime of this RunningQueries.  # noqa: E501
        :type: float
        """

        self._runtime = runtime

    @property
    def sql(self):
        """Gets the sql of this RunningQueries.  # noqa: E501

        SQL text of the query as run  # noqa: E501

        :return: The sql of this RunningQueries.  # noqa: E501
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        """Sets the sql of this RunningQueries.

        SQL text of the query as run  # noqa: E501

        :param sql: The sql of this RunningQueries.  # noqa: E501
        :type: str
        """

        self._sql = sql

    @property
    def can(self):
        """Gets the can of this RunningQueries.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this RunningQueries.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this RunningQueries.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this RunningQueries.  # noqa: E501
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
        if not isinstance(other, RunningQueries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
