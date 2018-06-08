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

from swagger_client.models.group import Group  # noqa: F401,E501
from swagger_client.models.role import Role  # noqa: F401,E501
from swagger_client.models.saml_group_read import SamlGroupRead  # noqa: F401,E501
from swagger_client.models.saml_group_write import SamlGroupWrite  # noqa: F401,E501
from swagger_client.models.saml_user_attribute_read import SamlUserAttributeRead  # noqa: F401,E501
from swagger_client.models.saml_user_attribute_write import SamlUserAttributeWrite  # noqa: F401,E501


class SamlConfig(object):
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
        'enabled': 'bool',
        'idp_cert': 'str',
        'idp_url': 'str',
        'idp_issuer': 'str',
        'idp_audience': 'str',
        'allowed_clock_drift': 'int',
        'user_attribute_map_email': 'str',
        'user_attribute_map_first_name': 'str',
        'user_attribute_map_last_name': 'str',
        'new_user_migration_types': 'str',
        'alternate_email_login_allowed': 'bool',
        'test_slug': 'str',
        'modified_at': 'str',
        'modified_by': 'str',
        'default_new_user_roles': 'list[Role]',
        'default_new_user_groups': 'list[Group]',
        'default_new_user_role_ids': 'list[int]',
        'default_new_user_group_ids': 'list[int]',
        'set_roles_from_groups': 'bool',
        'groups_attribute': 'str',
        'groups': 'list[SamlGroupRead]',
        'groups_with_role_ids': 'list[SamlGroupWrite]',
        'auth_requires_role': 'bool',
        'user_attributes': 'list[SamlUserAttributeRead]',
        'user_attributes_with_ids': 'list[SamlUserAttributeWrite]',
        'groups_finder_type': 'str',
        'groups_member_value': 'str',
        'bypass_login_page': 'bool',
        'url': 'str',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'enabled': 'enabled',
        'idp_cert': 'idp_cert',
        'idp_url': 'idp_url',
        'idp_issuer': 'idp_issuer',
        'idp_audience': 'idp_audience',
        'allowed_clock_drift': 'allowed_clock_drift',
        'user_attribute_map_email': 'user_attribute_map_email',
        'user_attribute_map_first_name': 'user_attribute_map_first_name',
        'user_attribute_map_last_name': 'user_attribute_map_last_name',
        'new_user_migration_types': 'new_user_migration_types',
        'alternate_email_login_allowed': 'alternate_email_login_allowed',
        'test_slug': 'test_slug',
        'modified_at': 'modified_at',
        'modified_by': 'modified_by',
        'default_new_user_roles': 'default_new_user_roles',
        'default_new_user_groups': 'default_new_user_groups',
        'default_new_user_role_ids': 'default_new_user_role_ids',
        'default_new_user_group_ids': 'default_new_user_group_ids',
        'set_roles_from_groups': 'set_roles_from_groups',
        'groups_attribute': 'groups_attribute',
        'groups': 'groups',
        'groups_with_role_ids': 'groups_with_role_ids',
        'auth_requires_role': 'auth_requires_role',
        'user_attributes': 'user_attributes',
        'user_attributes_with_ids': 'user_attributes_with_ids',
        'groups_finder_type': 'groups_finder_type',
        'groups_member_value': 'groups_member_value',
        'bypass_login_page': 'bypass_login_page',
        'url': 'url',
        'can': 'can'
    }

    def __init__(self, enabled=None, idp_cert=None, idp_url=None, idp_issuer=None, idp_audience=None, allowed_clock_drift=None, user_attribute_map_email=None, user_attribute_map_first_name=None, user_attribute_map_last_name=None, new_user_migration_types=None, alternate_email_login_allowed=None, test_slug=None, modified_at=None, modified_by=None, default_new_user_roles=None, default_new_user_groups=None, default_new_user_role_ids=None, default_new_user_group_ids=None, set_roles_from_groups=None, groups_attribute=None, groups=None, groups_with_role_ids=None, auth_requires_role=None, user_attributes=None, user_attributes_with_ids=None, groups_finder_type=None, groups_member_value=None, bypass_login_page=None, url=None, can=None):  # noqa: E501
        """SamlConfig - a model defined in Swagger"""  # noqa: E501

        self._enabled = None
        self._idp_cert = None
        self._idp_url = None
        self._idp_issuer = None
        self._idp_audience = None
        self._allowed_clock_drift = None
        self._user_attribute_map_email = None
        self._user_attribute_map_first_name = None
        self._user_attribute_map_last_name = None
        self._new_user_migration_types = None
        self._alternate_email_login_allowed = None
        self._test_slug = None
        self._modified_at = None
        self._modified_by = None
        self._default_new_user_roles = None
        self._default_new_user_groups = None
        self._default_new_user_role_ids = None
        self._default_new_user_group_ids = None
        self._set_roles_from_groups = None
        self._groups_attribute = None
        self._groups = None
        self._groups_with_role_ids = None
        self._auth_requires_role = None
        self._user_attributes = None
        self._user_attributes_with_ids = None
        self._groups_finder_type = None
        self._groups_member_value = None
        self._bypass_login_page = None
        self._url = None
        self._can = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if idp_cert is not None:
            self.idp_cert = idp_cert
        if idp_url is not None:
            self.idp_url = idp_url
        if idp_issuer is not None:
            self.idp_issuer = idp_issuer
        if idp_audience is not None:
            self.idp_audience = idp_audience
        if allowed_clock_drift is not None:
            self.allowed_clock_drift = allowed_clock_drift
        if user_attribute_map_email is not None:
            self.user_attribute_map_email = user_attribute_map_email
        if user_attribute_map_first_name is not None:
            self.user_attribute_map_first_name = user_attribute_map_first_name
        if user_attribute_map_last_name is not None:
            self.user_attribute_map_last_name = user_attribute_map_last_name
        if new_user_migration_types is not None:
            self.new_user_migration_types = new_user_migration_types
        if alternate_email_login_allowed is not None:
            self.alternate_email_login_allowed = alternate_email_login_allowed
        if test_slug is not None:
            self.test_slug = test_slug
        if modified_at is not None:
            self.modified_at = modified_at
        if modified_by is not None:
            self.modified_by = modified_by
        if default_new_user_roles is not None:
            self.default_new_user_roles = default_new_user_roles
        if default_new_user_groups is not None:
            self.default_new_user_groups = default_new_user_groups
        if default_new_user_role_ids is not None:
            self.default_new_user_role_ids = default_new_user_role_ids
        if default_new_user_group_ids is not None:
            self.default_new_user_group_ids = default_new_user_group_ids
        if set_roles_from_groups is not None:
            self.set_roles_from_groups = set_roles_from_groups
        if groups_attribute is not None:
            self.groups_attribute = groups_attribute
        if groups is not None:
            self.groups = groups
        if groups_with_role_ids is not None:
            self.groups_with_role_ids = groups_with_role_ids
        if auth_requires_role is not None:
            self.auth_requires_role = auth_requires_role
        if user_attributes is not None:
            self.user_attributes = user_attributes
        if user_attributes_with_ids is not None:
            self.user_attributes_with_ids = user_attributes_with_ids
        if groups_finder_type is not None:
            self.groups_finder_type = groups_finder_type
        if groups_member_value is not None:
            self.groups_member_value = groups_member_value
        if bypass_login_page is not None:
            self.bypass_login_page = bypass_login_page
        if url is not None:
            self.url = url
        if can is not None:
            self.can = can

    @property
    def enabled(self):
        """Gets the enabled of this SamlConfig.  # noqa: E501

        Enable/Disable Saml authentication for the server  # noqa: E501

        :return: The enabled of this SamlConfig.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this SamlConfig.

        Enable/Disable Saml authentication for the server  # noqa: E501

        :param enabled: The enabled of this SamlConfig.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def idp_cert(self):
        """Gets the idp_cert of this SamlConfig.  # noqa: E501

        Identity Provider Certificate (provided by IdP)  # noqa: E501

        :return: The idp_cert of this SamlConfig.  # noqa: E501
        :rtype: str
        """
        return self._idp_cert

    @idp_cert.setter
    def idp_cert(self, idp_cert):
        """Sets the idp_cert of this SamlConfig.

        Identity Provider Certificate (provided by IdP)  # noqa: E501

        :param idp_cert: The idp_cert of this SamlConfig.  # noqa: E501
        :type: str
        """

        self._idp_cert = idp_cert

    @property
    def idp_url(self):
        """Gets the idp_url of this SamlConfig.  # noqa: E501

        Identity Provider Url (provided by IdP)  # noqa: E501

        :return: The idp_url of this SamlConfig.  # noqa: E501
        :rtype: str
        """
        return self._idp_url

    @idp_url.setter
    def idp_url(self, idp_url):
        """Sets the idp_url of this SamlConfig.

        Identity Provider Url (provided by IdP)  # noqa: E501

        :param idp_url: The idp_url of this SamlConfig.  # noqa: E501
        :type: str
        """

        self._idp_url = idp_url

    @property
    def idp_issuer(self):
        """Gets the idp_issuer of this SamlConfig.  # noqa: E501

        Identity Provider Issuer (provided by IdP)  # noqa: E501

        :return: The idp_issuer of this SamlConfig.  # noqa: E501
        :rtype: str
        """
        return self._idp_issuer

    @idp_issuer.setter
    def idp_issuer(self, idp_issuer):
        """Sets the idp_issuer of this SamlConfig.

        Identity Provider Issuer (provided by IdP)  # noqa: E501

        :param idp_issuer: The idp_issuer of this SamlConfig.  # noqa: E501
        :type: str
        """

        self._idp_issuer = idp_issuer

    @property
    def idp_audience(self):
        """Gets the idp_audience of this SamlConfig.  # noqa: E501

        Identity Provider Audience (set in IdP config). Optional in Looker. Set this only if you want Looker to validate the audience value returned by the IdP.  # noqa: E501

        :return: The idp_audience of this SamlConfig.  # noqa: E501
        :rtype: str
        """
        return self._idp_audience

    @idp_audience.setter
    def idp_audience(self, idp_audience):
        """Sets the idp_audience of this SamlConfig.

        Identity Provider Audience (set in IdP config). Optional in Looker. Set this only if you want Looker to validate the audience value returned by the IdP.  # noqa: E501

        :param idp_audience: The idp_audience of this SamlConfig.  # noqa: E501
        :type: str
        """

        self._idp_audience = idp_audience

    @property
    def allowed_clock_drift(self):
        """Gets the allowed_clock_drift of this SamlConfig.  # noqa: E501

        Count of seconds of clock drift to allow when validating timestamps of assertions.  # noqa: E501

        :return: The allowed_clock_drift of this SamlConfig.  # noqa: E501
        :rtype: int
        """
        return self._allowed_clock_drift

    @allowed_clock_drift.setter
    def allowed_clock_drift(self, allowed_clock_drift):
        """Sets the allowed_clock_drift of this SamlConfig.

        Count of seconds of clock drift to allow when validating timestamps of assertions.  # noqa: E501

        :param allowed_clock_drift: The allowed_clock_drift of this SamlConfig.  # noqa: E501
        :type: int
        """

        self._allowed_clock_drift = allowed_clock_drift

    @property
    def user_attribute_map_email(self):
        """Gets the user_attribute_map_email of this SamlConfig.  # noqa: E501

        Name of user record attributes used to indicate email address field  # noqa: E501

        :return: The user_attribute_map_email of this SamlConfig.  # noqa: E501
        :rtype: str
        """
        return self._user_attribute_map_email

    @user_attribute_map_email.setter
    def user_attribute_map_email(self, user_attribute_map_email):
        """Sets the user_attribute_map_email of this SamlConfig.

        Name of user record attributes used to indicate email address field  # noqa: E501

        :param user_attribute_map_email: The user_attribute_map_email of this SamlConfig.  # noqa: E501
        :type: str
        """

        self._user_attribute_map_email = user_attribute_map_email

    @property
    def user_attribute_map_first_name(self):
        """Gets the user_attribute_map_first_name of this SamlConfig.  # noqa: E501

        Name of user record attributes used to indicate first name  # noqa: E501

        :return: The user_attribute_map_first_name of this SamlConfig.  # noqa: E501
        :rtype: str
        """
        return self._user_attribute_map_first_name

    @user_attribute_map_first_name.setter
    def user_attribute_map_first_name(self, user_attribute_map_first_name):
        """Sets the user_attribute_map_first_name of this SamlConfig.

        Name of user record attributes used to indicate first name  # noqa: E501

        :param user_attribute_map_first_name: The user_attribute_map_first_name of this SamlConfig.  # noqa: E501
        :type: str
        """

        self._user_attribute_map_first_name = user_attribute_map_first_name

    @property
    def user_attribute_map_last_name(self):
        """Gets the user_attribute_map_last_name of this SamlConfig.  # noqa: E501

        Name of user record attributes used to indicate last name  # noqa: E501

        :return: The user_attribute_map_last_name of this SamlConfig.  # noqa: E501
        :rtype: str
        """
        return self._user_attribute_map_last_name

    @user_attribute_map_last_name.setter
    def user_attribute_map_last_name(self, user_attribute_map_last_name):
        """Sets the user_attribute_map_last_name of this SamlConfig.

        Name of user record attributes used to indicate last name  # noqa: E501

        :param user_attribute_map_last_name: The user_attribute_map_last_name of this SamlConfig.  # noqa: E501
        :type: str
        """

        self._user_attribute_map_last_name = user_attribute_map_last_name

    @property
    def new_user_migration_types(self):
        """Gets the new_user_migration_types of this SamlConfig.  # noqa: E501

        Merge first-time saml login to existing user account by email addresses. When a user logs in for the first time via saml this option will connect this user into their existing account by finding the account with a matching email address by testing the given types of credentials for existing users. Otherwise a new user account will be created for the user. This list (if provided) must be a comma separated list of string like 'email,ldap,google'  # noqa: E501

        :return: The new_user_migration_types of this SamlConfig.  # noqa: E501
        :rtype: str
        """
        return self._new_user_migration_types

    @new_user_migration_types.setter
    def new_user_migration_types(self, new_user_migration_types):
        """Sets the new_user_migration_types of this SamlConfig.

        Merge first-time saml login to existing user account by email addresses. When a user logs in for the first time via saml this option will connect this user into their existing account by finding the account with a matching email address by testing the given types of credentials for existing users. Otherwise a new user account will be created for the user. This list (if provided) must be a comma separated list of string like 'email,ldap,google'  # noqa: E501

        :param new_user_migration_types: The new_user_migration_types of this SamlConfig.  # noqa: E501
        :type: str
        """

        self._new_user_migration_types = new_user_migration_types

    @property
    def alternate_email_login_allowed(self):
        """Gets the alternate_email_login_allowed of this SamlConfig.  # noqa: E501

        Allow alternate email-based login via '/login/email' for admins and for specified users with the 'login_special_email' permission. This option is useful as a fallback during ldap setup, if ldap config problems occur later, or if you need to support some users who are not in your ldap directory. Looker email/password logins are always disabled for regular users when ldap is enabled.  # noqa: E501

        :return: The alternate_email_login_allowed of this SamlConfig.  # noqa: E501
        :rtype: bool
        """
        return self._alternate_email_login_allowed

    @alternate_email_login_allowed.setter
    def alternate_email_login_allowed(self, alternate_email_login_allowed):
        """Sets the alternate_email_login_allowed of this SamlConfig.

        Allow alternate email-based login via '/login/email' for admins and for specified users with the 'login_special_email' permission. This option is useful as a fallback during ldap setup, if ldap config problems occur later, or if you need to support some users who are not in your ldap directory. Looker email/password logins are always disabled for regular users when ldap is enabled.  # noqa: E501

        :param alternate_email_login_allowed: The alternate_email_login_allowed of this SamlConfig.  # noqa: E501
        :type: bool
        """

        self._alternate_email_login_allowed = alternate_email_login_allowed

    @property
    def test_slug(self):
        """Gets the test_slug of this SamlConfig.  # noqa: E501

        Slug to identify configurations that are created in order to run a Saml config test  # noqa: E501

        :return: The test_slug of this SamlConfig.  # noqa: E501
        :rtype: str
        """
        return self._test_slug

    @test_slug.setter
    def test_slug(self, test_slug):
        """Sets the test_slug of this SamlConfig.

        Slug to identify configurations that are created in order to run a Saml config test  # noqa: E501

        :param test_slug: The test_slug of this SamlConfig.  # noqa: E501
        :type: str
        """

        self._test_slug = test_slug

    @property
    def modified_at(self):
        """Gets the modified_at of this SamlConfig.  # noqa: E501

        When this config was last modified  # noqa: E501

        :return: The modified_at of this SamlConfig.  # noqa: E501
        :rtype: str
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this SamlConfig.

        When this config was last modified  # noqa: E501

        :param modified_at: The modified_at of this SamlConfig.  # noqa: E501
        :type: str
        """

        self._modified_at = modified_at

    @property
    def modified_by(self):
        """Gets the modified_by of this SamlConfig.  # noqa: E501

        User id of user who last modified this config  # noqa: E501

        :return: The modified_by of this SamlConfig.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this SamlConfig.

        User id of user who last modified this config  # noqa: E501

        :param modified_by: The modified_by of this SamlConfig.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def default_new_user_roles(self):
        """Gets the default_new_user_roles of this SamlConfig.  # noqa: E501

        (Read-only) Roles that will be applied to new users the first time they login via Saml  # noqa: E501

        :return: The default_new_user_roles of this SamlConfig.  # noqa: E501
        :rtype: list[Role]
        """
        return self._default_new_user_roles

    @default_new_user_roles.setter
    def default_new_user_roles(self, default_new_user_roles):
        """Sets the default_new_user_roles of this SamlConfig.

        (Read-only) Roles that will be applied to new users the first time they login via Saml  # noqa: E501

        :param default_new_user_roles: The default_new_user_roles of this SamlConfig.  # noqa: E501
        :type: list[Role]
        """

        self._default_new_user_roles = default_new_user_roles

    @property
    def default_new_user_groups(self):
        """Gets the default_new_user_groups of this SamlConfig.  # noqa: E501

        (Read-only) Groups that will be applied to new users the first time they login via Saml  # noqa: E501

        :return: The default_new_user_groups of this SamlConfig.  # noqa: E501
        :rtype: list[Group]
        """
        return self._default_new_user_groups

    @default_new_user_groups.setter
    def default_new_user_groups(self, default_new_user_groups):
        """Sets the default_new_user_groups of this SamlConfig.

        (Read-only) Groups that will be applied to new users the first time they login via Saml  # noqa: E501

        :param default_new_user_groups: The default_new_user_groups of this SamlConfig.  # noqa: E501
        :type: list[Group]
        """

        self._default_new_user_groups = default_new_user_groups

    @property
    def default_new_user_role_ids(self):
        """Gets the default_new_user_role_ids of this SamlConfig.  # noqa: E501

        (Write-Only) Array of ids of roles that will be applied to new users the first time they login via Saml  # noqa: E501

        :return: The default_new_user_role_ids of this SamlConfig.  # noqa: E501
        :rtype: list[int]
        """
        return self._default_new_user_role_ids

    @default_new_user_role_ids.setter
    def default_new_user_role_ids(self, default_new_user_role_ids):
        """Sets the default_new_user_role_ids of this SamlConfig.

        (Write-Only) Array of ids of roles that will be applied to new users the first time they login via Saml  # noqa: E501

        :param default_new_user_role_ids: The default_new_user_role_ids of this SamlConfig.  # noqa: E501
        :type: list[int]
        """

        self._default_new_user_role_ids = default_new_user_role_ids

    @property
    def default_new_user_group_ids(self):
        """Gets the default_new_user_group_ids of this SamlConfig.  # noqa: E501

        (Write-Only) Array of ids of groups that will be applied to new users the first time they login via Saml  # noqa: E501

        :return: The default_new_user_group_ids of this SamlConfig.  # noqa: E501
        :rtype: list[int]
        """
        return self._default_new_user_group_ids

    @default_new_user_group_ids.setter
    def default_new_user_group_ids(self, default_new_user_group_ids):
        """Sets the default_new_user_group_ids of this SamlConfig.

        (Write-Only) Array of ids of groups that will be applied to new users the first time they login via Saml  # noqa: E501

        :param default_new_user_group_ids: The default_new_user_group_ids of this SamlConfig.  # noqa: E501
        :type: list[int]
        """

        self._default_new_user_group_ids = default_new_user_group_ids

    @property
    def set_roles_from_groups(self):
        """Gets the set_roles_from_groups of this SamlConfig.  # noqa: E501

        Set user roles in Looker based on groups from Saml  # noqa: E501

        :return: The set_roles_from_groups of this SamlConfig.  # noqa: E501
        :rtype: bool
        """
        return self._set_roles_from_groups

    @set_roles_from_groups.setter
    def set_roles_from_groups(self, set_roles_from_groups):
        """Sets the set_roles_from_groups of this SamlConfig.

        Set user roles in Looker based on groups from Saml  # noqa: E501

        :param set_roles_from_groups: The set_roles_from_groups of this SamlConfig.  # noqa: E501
        :type: bool
        """

        self._set_roles_from_groups = set_roles_from_groups

    @property
    def groups_attribute(self):
        """Gets the groups_attribute of this SamlConfig.  # noqa: E501

        Name of user record attributes used to indicate groups. Used when 'groups_finder_type' is set to 'grouped_attribute_values'  # noqa: E501

        :return: The groups_attribute of this SamlConfig.  # noqa: E501
        :rtype: str
        """
        return self._groups_attribute

    @groups_attribute.setter
    def groups_attribute(self, groups_attribute):
        """Sets the groups_attribute of this SamlConfig.

        Name of user record attributes used to indicate groups. Used when 'groups_finder_type' is set to 'grouped_attribute_values'  # noqa: E501

        :param groups_attribute: The groups_attribute of this SamlConfig.  # noqa: E501
        :type: str
        """

        self._groups_attribute = groups_attribute

    @property
    def groups(self):
        """Gets the groups of this SamlConfig.  # noqa: E501

        (Read-only) Array of mappings between Saml Groups and Looker Roles  # noqa: E501

        :return: The groups of this SamlConfig.  # noqa: E501
        :rtype: list[SamlGroupRead]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this SamlConfig.

        (Read-only) Array of mappings between Saml Groups and Looker Roles  # noqa: E501

        :param groups: The groups of this SamlConfig.  # noqa: E501
        :type: list[SamlGroupRead]
        """

        self._groups = groups

    @property
    def groups_with_role_ids(self):
        """Gets the groups_with_role_ids of this SamlConfig.  # noqa: E501

        (Read/Write) Array of mappings between Saml Groups and arrays of Looker Role ids  # noqa: E501

        :return: The groups_with_role_ids of this SamlConfig.  # noqa: E501
        :rtype: list[SamlGroupWrite]
        """
        return self._groups_with_role_ids

    @groups_with_role_ids.setter
    def groups_with_role_ids(self, groups_with_role_ids):
        """Sets the groups_with_role_ids of this SamlConfig.

        (Read/Write) Array of mappings between Saml Groups and arrays of Looker Role ids  # noqa: E501

        :param groups_with_role_ids: The groups_with_role_ids of this SamlConfig.  # noqa: E501
        :type: list[SamlGroupWrite]
        """

        self._groups_with_role_ids = groups_with_role_ids

    @property
    def auth_requires_role(self):
        """Gets the auth_requires_role of this SamlConfig.  # noqa: E501

        Users will not be allowed to login at all unless a role for them is found in Saml if set to true  # noqa: E501

        :return: The auth_requires_role of this SamlConfig.  # noqa: E501
        :rtype: bool
        """
        return self._auth_requires_role

    @auth_requires_role.setter
    def auth_requires_role(self, auth_requires_role):
        """Sets the auth_requires_role of this SamlConfig.

        Users will not be allowed to login at all unless a role for them is found in Saml if set to true  # noqa: E501

        :param auth_requires_role: The auth_requires_role of this SamlConfig.  # noqa: E501
        :type: bool
        """

        self._auth_requires_role = auth_requires_role

    @property
    def user_attributes(self):
        """Gets the user_attributes of this SamlConfig.  # noqa: E501

        (Read-only) Array of mappings between Saml User Attributes and Looker User Attributes  # noqa: E501

        :return: The user_attributes of this SamlConfig.  # noqa: E501
        :rtype: list[SamlUserAttributeRead]
        """
        return self._user_attributes

    @user_attributes.setter
    def user_attributes(self, user_attributes):
        """Sets the user_attributes of this SamlConfig.

        (Read-only) Array of mappings between Saml User Attributes and Looker User Attributes  # noqa: E501

        :param user_attributes: The user_attributes of this SamlConfig.  # noqa: E501
        :type: list[SamlUserAttributeRead]
        """

        self._user_attributes = user_attributes

    @property
    def user_attributes_with_ids(self):
        """Gets the user_attributes_with_ids of this SamlConfig.  # noqa: E501

        (Read/Write) Array of mappings between Saml User Attributes and arrays of Looker User Attribute ids  # noqa: E501

        :return: The user_attributes_with_ids of this SamlConfig.  # noqa: E501
        :rtype: list[SamlUserAttributeWrite]
        """
        return self._user_attributes_with_ids

    @user_attributes_with_ids.setter
    def user_attributes_with_ids(self, user_attributes_with_ids):
        """Sets the user_attributes_with_ids of this SamlConfig.

        (Read/Write) Array of mappings between Saml User Attributes and arrays of Looker User Attribute ids  # noqa: E501

        :param user_attributes_with_ids: The user_attributes_with_ids of this SamlConfig.  # noqa: E501
        :type: list[SamlUserAttributeWrite]
        """

        self._user_attributes_with_ids = user_attributes_with_ids

    @property
    def groups_finder_type(self):
        """Gets the groups_finder_type of this SamlConfig.  # noqa: E501

        Identifier for a strategy for how Looker will find groups in the SAML response. One of ['grouped_attribute_values', 'individual_attributes']  # noqa: E501

        :return: The groups_finder_type of this SamlConfig.  # noqa: E501
        :rtype: str
        """
        return self._groups_finder_type

    @groups_finder_type.setter
    def groups_finder_type(self, groups_finder_type):
        """Sets the groups_finder_type of this SamlConfig.

        Identifier for a strategy for how Looker will find groups in the SAML response. One of ['grouped_attribute_values', 'individual_attributes']  # noqa: E501

        :param groups_finder_type: The groups_finder_type of this SamlConfig.  # noqa: E501
        :type: str
        """

        self._groups_finder_type = groups_finder_type

    @property
    def groups_member_value(self):
        """Gets the groups_member_value of this SamlConfig.  # noqa: E501

        Value for group attribute used to indicate membership. Used when 'groups_finder_type' is set to 'individual_attributes'  # noqa: E501

        :return: The groups_member_value of this SamlConfig.  # noqa: E501
        :rtype: str
        """
        return self._groups_member_value

    @groups_member_value.setter
    def groups_member_value(self, groups_member_value):
        """Sets the groups_member_value of this SamlConfig.

        Value for group attribute used to indicate membership. Used when 'groups_finder_type' is set to 'individual_attributes'  # noqa: E501

        :param groups_member_value: The groups_member_value of this SamlConfig.  # noqa: E501
        :type: str
        """

        self._groups_member_value = groups_member_value

    @property
    def bypass_login_page(self):
        """Gets the bypass_login_page of this SamlConfig.  # noqa: E501

        Bypass the login page when user authentication is required. Redirect to IdP immediately instead.  # noqa: E501

        :return: The bypass_login_page of this SamlConfig.  # noqa: E501
        :rtype: bool
        """
        return self._bypass_login_page

    @bypass_login_page.setter
    def bypass_login_page(self, bypass_login_page):
        """Sets the bypass_login_page of this SamlConfig.

        Bypass the login page when user authentication is required. Redirect to IdP immediately instead.  # noqa: E501

        :param bypass_login_page: The bypass_login_page of this SamlConfig.  # noqa: E501
        :type: bool
        """

        self._bypass_login_page = bypass_login_page

    @property
    def url(self):
        """Gets the url of this SamlConfig.  # noqa: E501

        Link to get this item  # noqa: E501

        :return: The url of this SamlConfig.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SamlConfig.

        Link to get this item  # noqa: E501

        :param url: The url of this SamlConfig.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def can(self):
        """Gets the can of this SamlConfig.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this SamlConfig.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this SamlConfig.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this SamlConfig.  # noqa: E501
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
        if not isinstance(other, SamlConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
