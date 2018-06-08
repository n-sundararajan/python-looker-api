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

from swagger_client.models.look_model import LookModel  # noqa: F401,E501
from swagger_client.models.space_base import SpaceBase  # noqa: F401,E501
from swagger_client.models.user_id_only import UserIdOnly  # noqa: F401,E501


class Look(object):
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
        'content_metadata_id': 'int',
        'view_count': 'int',
        'favorite_count': 'int',
        'last_accessed_at': 'datetime',
        'content_favorite_id': 'int',
        'title': 'str',
        'user': 'UserIdOnly',
        'query_id': 'int',
        'description': 'str',
        'short_url': 'str',
        'space': 'SpaceBase',
        'public': 'bool',
        'public_slug': 'str',
        'user_id': 'int',
        'space_id': 'str',
        'model': 'LookModel',
        'public_url': 'str',
        'embed_url': 'str',
        'image_embed_url': 'str',
        'google_spreadsheet_formula': 'str',
        'excel_file_url': 'str',
        'created_at': 'datetime',
        'deleted_at': 'datetime',
        'updated_at': 'datetime',
        'last_updater_id': 'int',
        'deleter_id': 'int',
        'deleted': 'bool',
        'last_viewed_at': 'datetime',
        'is_run_on_load': 'bool',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'id': 'id',
        'content_metadata_id': 'content_metadata_id',
        'view_count': 'view_count',
        'favorite_count': 'favorite_count',
        'last_accessed_at': 'last_accessed_at',
        'content_favorite_id': 'content_favorite_id',
        'title': 'title',
        'user': 'user',
        'query_id': 'query_id',
        'description': 'description',
        'short_url': 'short_url',
        'space': 'space',
        'public': 'public',
        'public_slug': 'public_slug',
        'user_id': 'user_id',
        'space_id': 'space_id',
        'model': 'model',
        'public_url': 'public_url',
        'embed_url': 'embed_url',
        'image_embed_url': 'image_embed_url',
        'google_spreadsheet_formula': 'google_spreadsheet_formula',
        'excel_file_url': 'excel_file_url',
        'created_at': 'created_at',
        'deleted_at': 'deleted_at',
        'updated_at': 'updated_at',
        'last_updater_id': 'last_updater_id',
        'deleter_id': 'deleter_id',
        'deleted': 'deleted',
        'last_viewed_at': 'last_viewed_at',
        'is_run_on_load': 'is_run_on_load',
        'can': 'can'
    }

    def __init__(self, id=None, content_metadata_id=None, view_count=None, favorite_count=None, last_accessed_at=None, content_favorite_id=None, title=None, user=None, query_id=None, description=None, short_url=None, space=None, public=None, public_slug=None, user_id=None, space_id=None, model=None, public_url=None, embed_url=None, image_embed_url=None, google_spreadsheet_formula=None, excel_file_url=None, created_at=None, deleted_at=None, updated_at=None, last_updater_id=None, deleter_id=None, deleted=None, last_viewed_at=None, is_run_on_load=None, can=None):  # noqa: E501
        """Look - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._content_metadata_id = None
        self._view_count = None
        self._favorite_count = None
        self._last_accessed_at = None
        self._content_favorite_id = None
        self._title = None
        self._user = None
        self._query_id = None
        self._description = None
        self._short_url = None
        self._space = None
        self._public = None
        self._public_slug = None
        self._user_id = None
        self._space_id = None
        self._model = None
        self._public_url = None
        self._embed_url = None
        self._image_embed_url = None
        self._google_spreadsheet_formula = None
        self._excel_file_url = None
        self._created_at = None
        self._deleted_at = None
        self._updated_at = None
        self._last_updater_id = None
        self._deleter_id = None
        self._deleted = None
        self._last_viewed_at = None
        self._is_run_on_load = None
        self._can = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if content_metadata_id is not None:
            self.content_metadata_id = content_metadata_id
        if view_count is not None:
            self.view_count = view_count
        if favorite_count is not None:
            self.favorite_count = favorite_count
        if last_accessed_at is not None:
            self.last_accessed_at = last_accessed_at
        if content_favorite_id is not None:
            self.content_favorite_id = content_favorite_id
        if title is not None:
            self.title = title
        if user is not None:
            self.user = user
        if query_id is not None:
            self.query_id = query_id
        if description is not None:
            self.description = description
        if short_url is not None:
            self.short_url = short_url
        if space is not None:
            self.space = space
        if public is not None:
            self.public = public
        if public_slug is not None:
            self.public_slug = public_slug
        if user_id is not None:
            self.user_id = user_id
        if space_id is not None:
            self.space_id = space_id
        if model is not None:
            self.model = model
        if public_url is not None:
            self.public_url = public_url
        if embed_url is not None:
            self.embed_url = embed_url
        if image_embed_url is not None:
            self.image_embed_url = image_embed_url
        if google_spreadsheet_formula is not None:
            self.google_spreadsheet_formula = google_spreadsheet_formula
        if excel_file_url is not None:
            self.excel_file_url = excel_file_url
        if created_at is not None:
            self.created_at = created_at
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if updated_at is not None:
            self.updated_at = updated_at
        if last_updater_id is not None:
            self.last_updater_id = last_updater_id
        if deleter_id is not None:
            self.deleter_id = deleter_id
        if deleted is not None:
            self.deleted = deleted
        if last_viewed_at is not None:
            self.last_viewed_at = last_viewed_at
        if is_run_on_load is not None:
            self.is_run_on_load = is_run_on_load
        if can is not None:
            self.can = can

    @property
    def id(self):
        """Gets the id of this Look.  # noqa: E501

        Unique Id  # noqa: E501

        :return: The id of this Look.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Look.

        Unique Id  # noqa: E501

        :param id: The id of this Look.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def content_metadata_id(self):
        """Gets the content_metadata_id of this Look.  # noqa: E501

        Id of content metadata  # noqa: E501

        :return: The content_metadata_id of this Look.  # noqa: E501
        :rtype: int
        """
        return self._content_metadata_id

    @content_metadata_id.setter
    def content_metadata_id(self, content_metadata_id):
        """Sets the content_metadata_id of this Look.

        Id of content metadata  # noqa: E501

        :param content_metadata_id: The content_metadata_id of this Look.  # noqa: E501
        :type: int
        """

        self._content_metadata_id = content_metadata_id

    @property
    def view_count(self):
        """Gets the view_count of this Look.  # noqa: E501

        Number of times viewed in the Looker web UI  # noqa: E501

        :return: The view_count of this Look.  # noqa: E501
        :rtype: int
        """
        return self._view_count

    @view_count.setter
    def view_count(self, view_count):
        """Sets the view_count of this Look.

        Number of times viewed in the Looker web UI  # noqa: E501

        :param view_count: The view_count of this Look.  # noqa: E501
        :type: int
        """

        self._view_count = view_count

    @property
    def favorite_count(self):
        """Gets the favorite_count of this Look.  # noqa: E501

        Number of times favorited  # noqa: E501

        :return: The favorite_count of this Look.  # noqa: E501
        :rtype: int
        """
        return self._favorite_count

    @favorite_count.setter
    def favorite_count(self, favorite_count):
        """Sets the favorite_count of this Look.

        Number of times favorited  # noqa: E501

        :param favorite_count: The favorite_count of this Look.  # noqa: E501
        :type: int
        """

        self._favorite_count = favorite_count

    @property
    def last_accessed_at(self):
        """Gets the last_accessed_at of this Look.  # noqa: E501

        Time that the Look was last accessed by any user  # noqa: E501

        :return: The last_accessed_at of this Look.  # noqa: E501
        :rtype: datetime
        """
        return self._last_accessed_at

    @last_accessed_at.setter
    def last_accessed_at(self, last_accessed_at):
        """Sets the last_accessed_at of this Look.

        Time that the Look was last accessed by any user  # noqa: E501

        :param last_accessed_at: The last_accessed_at of this Look.  # noqa: E501
        :type: datetime
        """

        self._last_accessed_at = last_accessed_at

    @property
    def content_favorite_id(self):
        """Gets the content_favorite_id of this Look.  # noqa: E501

        Content Favorite Id  # noqa: E501

        :return: The content_favorite_id of this Look.  # noqa: E501
        :rtype: int
        """
        return self._content_favorite_id

    @content_favorite_id.setter
    def content_favorite_id(self, content_favorite_id):
        """Sets the content_favorite_id of this Look.

        Content Favorite Id  # noqa: E501

        :param content_favorite_id: The content_favorite_id of this Look.  # noqa: E501
        :type: int
        """

        self._content_favorite_id = content_favorite_id

    @property
    def title(self):
        """Gets the title of this Look.  # noqa: E501

        Look Title  # noqa: E501

        :return: The title of this Look.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Look.

        Look Title  # noqa: E501

        :param title: The title of this Look.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def user(self):
        """Gets the user of this Look.  # noqa: E501

        User  # noqa: E501

        :return: The user of this Look.  # noqa: E501
        :rtype: UserIdOnly
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Look.

        User  # noqa: E501

        :param user: The user of this Look.  # noqa: E501
        :type: UserIdOnly
        """

        self._user = user

    @property
    def query_id(self):
        """Gets the query_id of this Look.  # noqa: E501

        Query Id  # noqa: E501

        :return: The query_id of this Look.  # noqa: E501
        :rtype: int
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """Sets the query_id of this Look.

        Query Id  # noqa: E501

        :param query_id: The query_id of this Look.  # noqa: E501
        :type: int
        """

        self._query_id = query_id

    @property
    def description(self):
        """Gets the description of this Look.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this Look.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Look.

        Description  # noqa: E501

        :param description: The description of this Look.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def short_url(self):
        """Gets the short_url of this Look.  # noqa: E501

        Short Url  # noqa: E501

        :return: The short_url of this Look.  # noqa: E501
        :rtype: str
        """
        return self._short_url

    @short_url.setter
    def short_url(self, short_url):
        """Sets the short_url of this Look.

        Short Url  # noqa: E501

        :param short_url: The short_url of this Look.  # noqa: E501
        :type: str
        """

        self._short_url = short_url

    @property
    def space(self):
        """Gets the space of this Look.  # noqa: E501

        Space of this Look  # noqa: E501

        :return: The space of this Look.  # noqa: E501
        :rtype: SpaceBase
        """
        return self._space

    @space.setter
    def space(self, space):
        """Sets the space of this Look.

        Space of this Look  # noqa: E501

        :param space: The space of this Look.  # noqa: E501
        :type: SpaceBase
        """

        self._space = space

    @property
    def public(self):
        """Gets the public of this Look.  # noqa: E501

        Is Public  # noqa: E501

        :return: The public of this Look.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this Look.

        Is Public  # noqa: E501

        :param public: The public of this Look.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def public_slug(self):
        """Gets the public_slug of this Look.  # noqa: E501

        Public Slug  # noqa: E501

        :return: The public_slug of this Look.  # noqa: E501
        :rtype: str
        """
        return self._public_slug

    @public_slug.setter
    def public_slug(self, public_slug):
        """Sets the public_slug of this Look.

        Public Slug  # noqa: E501

        :param public_slug: The public_slug of this Look.  # noqa: E501
        :type: str
        """

        self._public_slug = public_slug

    @property
    def user_id(self):
        """Gets the user_id of this Look.  # noqa: E501

        User Id  # noqa: E501

        :return: The user_id of this Look.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Look.

        User Id  # noqa: E501

        :param user_id: The user_id of this Look.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def space_id(self):
        """Gets the space_id of this Look.  # noqa: E501

        Space Id  # noqa: E501

        :return: The space_id of this Look.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this Look.

        Space Id  # noqa: E501

        :param space_id: The space_id of this Look.  # noqa: E501
        :type: str
        """

        self._space_id = space_id

    @property
    def model(self):
        """Gets the model of this Look.  # noqa: E501

        Model  # noqa: E501

        :return: The model of this Look.  # noqa: E501
        :rtype: LookModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this Look.

        Model  # noqa: E501

        :param model: The model of this Look.  # noqa: E501
        :type: LookModel
        """

        self._model = model

    @property
    def public_url(self):
        """Gets the public_url of this Look.  # noqa: E501

        Public Url  # noqa: E501

        :return: The public_url of this Look.  # noqa: E501
        :rtype: str
        """
        return self._public_url

    @public_url.setter
    def public_url(self, public_url):
        """Sets the public_url of this Look.

        Public Url  # noqa: E501

        :param public_url: The public_url of this Look.  # noqa: E501
        :type: str
        """

        self._public_url = public_url

    @property
    def embed_url(self):
        """Gets the embed_url of this Look.  # noqa: E501

        Embed Url  # noqa: E501

        :return: The embed_url of this Look.  # noqa: E501
        :rtype: str
        """
        return self._embed_url

    @embed_url.setter
    def embed_url(self, embed_url):
        """Sets the embed_url of this Look.

        Embed Url  # noqa: E501

        :param embed_url: The embed_url of this Look.  # noqa: E501
        :type: str
        """

        self._embed_url = embed_url

    @property
    def image_embed_url(self):
        """Gets the image_embed_url of this Look.  # noqa: E501

        Image Embed Url  # noqa: E501

        :return: The image_embed_url of this Look.  # noqa: E501
        :rtype: str
        """
        return self._image_embed_url

    @image_embed_url.setter
    def image_embed_url(self, image_embed_url):
        """Sets the image_embed_url of this Look.

        Image Embed Url  # noqa: E501

        :param image_embed_url: The image_embed_url of this Look.  # noqa: E501
        :type: str
        """

        self._image_embed_url = image_embed_url

    @property
    def google_spreadsheet_formula(self):
        """Gets the google_spreadsheet_formula of this Look.  # noqa: E501

        Google Spreadsheet Formula  # noqa: E501

        :return: The google_spreadsheet_formula of this Look.  # noqa: E501
        :rtype: str
        """
        return self._google_spreadsheet_formula

    @google_spreadsheet_formula.setter
    def google_spreadsheet_formula(self, google_spreadsheet_formula):
        """Sets the google_spreadsheet_formula of this Look.

        Google Spreadsheet Formula  # noqa: E501

        :param google_spreadsheet_formula: The google_spreadsheet_formula of this Look.  # noqa: E501
        :type: str
        """

        self._google_spreadsheet_formula = google_spreadsheet_formula

    @property
    def excel_file_url(self):
        """Gets the excel_file_url of this Look.  # noqa: E501

        Excel File Url  # noqa: E501

        :return: The excel_file_url of this Look.  # noqa: E501
        :rtype: str
        """
        return self._excel_file_url

    @excel_file_url.setter
    def excel_file_url(self, excel_file_url):
        """Sets the excel_file_url of this Look.

        Excel File Url  # noqa: E501

        :param excel_file_url: The excel_file_url of this Look.  # noqa: E501
        :type: str
        """

        self._excel_file_url = excel_file_url

    @property
    def created_at(self):
        """Gets the created_at of this Look.  # noqa: E501

        Time that the Look was created.  # noqa: E501

        :return: The created_at of this Look.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Look.

        Time that the Look was created.  # noqa: E501

        :param created_at: The created_at of this Look.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this Look.  # noqa: E501

        Time that the Look was deleted.  # noqa: E501

        :return: The deleted_at of this Look.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this Look.

        Time that the Look was deleted.  # noqa: E501

        :param deleted_at: The deleted_at of this Look.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Look.  # noqa: E501

        Time that the Look was updated.  # noqa: E501

        :return: The updated_at of this Look.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Look.

        Time that the Look was updated.  # noqa: E501

        :param updated_at: The updated_at of this Look.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def last_updater_id(self):
        """Gets the last_updater_id of this Look.  # noqa: E501

        Id of User that last updated the look.  # noqa: E501

        :return: The last_updater_id of this Look.  # noqa: E501
        :rtype: int
        """
        return self._last_updater_id

    @last_updater_id.setter
    def last_updater_id(self, last_updater_id):
        """Sets the last_updater_id of this Look.

        Id of User that last updated the look.  # noqa: E501

        :param last_updater_id: The last_updater_id of this Look.  # noqa: E501
        :type: int
        """

        self._last_updater_id = last_updater_id

    @property
    def deleter_id(self):
        """Gets the deleter_id of this Look.  # noqa: E501

        Id of User that deleted the look.  # noqa: E501

        :return: The deleter_id of this Look.  # noqa: E501
        :rtype: int
        """
        return self._deleter_id

    @deleter_id.setter
    def deleter_id(self, deleter_id):
        """Sets the deleter_id of this Look.

        Id of User that deleted the look.  # noqa: E501

        :param deleter_id: The deleter_id of this Look.  # noqa: E501
        :type: int
        """

        self._deleter_id = deleter_id

    @property
    def deleted(self):
        """Gets the deleted of this Look.  # noqa: E501

        Whether or not a look is deleted.  # noqa: E501

        :return: The deleted of this Look.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Look.

        Whether or not a look is deleted.  # noqa: E501

        :param deleted: The deleted of this Look.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def last_viewed_at(self):
        """Gets the last_viewed_at of this Look.  # noqa: E501

        Time last viewed in the Looker web UI  # noqa: E501

        :return: The last_viewed_at of this Look.  # noqa: E501
        :rtype: datetime
        """
        return self._last_viewed_at

    @last_viewed_at.setter
    def last_viewed_at(self, last_viewed_at):
        """Sets the last_viewed_at of this Look.

        Time last viewed in the Looker web UI  # noqa: E501

        :param last_viewed_at: The last_viewed_at of this Look.  # noqa: E501
        :type: datetime
        """

        self._last_viewed_at = last_viewed_at

    @property
    def is_run_on_load(self):
        """Gets the is_run_on_load of this Look.  # noqa: E501

        auto-run query when Look viewed  # noqa: E501

        :return: The is_run_on_load of this Look.  # noqa: E501
        :rtype: bool
        """
        return self._is_run_on_load

    @is_run_on_load.setter
    def is_run_on_load(self, is_run_on_load):
        """Sets the is_run_on_load of this Look.

        auto-run query when Look viewed  # noqa: E501

        :param is_run_on_load: The is_run_on_load of this Look.  # noqa: E501
        :type: bool
        """

        self._is_run_on_load = is_run_on_load

    @property
    def can(self):
        """Gets the can of this Look.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this Look.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this Look.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this Look.  # noqa: E501
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
        if not isinstance(other, Look):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
