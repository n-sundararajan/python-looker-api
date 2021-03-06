# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning)   # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DashboardApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def all_dashboards(self, **kwargs):  # noqa: E501
        """Get All Dashboards  # noqa: E501

        Get information about all dashboards.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.all_dashboards(async=True)
        >>> result = thread.get()

        :param async bool
        :param str fields: Requested fields.
        :return: list[DashboardBase]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.all_dashboards_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.all_dashboards_with_http_info(**kwargs)  # noqa: E501
            return data

    def all_dashboards_with_http_info(self, **kwargs):  # noqa: E501
        """Get All Dashboards  # noqa: E501

        Get information about all dashboards.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.all_dashboards_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str fields: Requested fields.
        :return: list[DashboardBase]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method all_dashboards" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/dashboards', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DashboardBase]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_dashboard(self, **kwargs):  # noqa: E501
        """Create Dashboard  # noqa: E501

        ### Create a dashboard with specified information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_dashboard(async=True)
        >>> result = thread.get()

        :param async bool
        :param Dashboard body: Dashboard
        :return: Dashboard
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_dashboard_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_dashboard_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_dashboard_with_http_info(self, **kwargs):  # noqa: E501
        """Create Dashboard  # noqa: E501

        ### Create a dashboard with specified information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_dashboard_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param Dashboard body: Dashboard
        :return: Dashboard
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_dashboard" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/dashboards', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Dashboard',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_dashboard_prefetch(self, dashboard_id, **kwargs):  # noqa: E501
        """Create Dashboard Prefetch  # noqa: E501

        ### Create a prefetch for a dashboard with the specified information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_dashboard_prefetch(dashboard_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dashboard_id: Id of dashboard (required)
        :param PrefetchDashboardRequest body: Parameters for prefetch request
        :return: PrefetchDashboardRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_dashboard_prefetch_with_http_info(dashboard_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_dashboard_prefetch_with_http_info(dashboard_id, **kwargs)  # noqa: E501
            return data

    def create_dashboard_prefetch_with_http_info(self, dashboard_id, **kwargs):  # noqa: E501
        """Create Dashboard Prefetch  # noqa: E501

        ### Create a prefetch for a dashboard with the specified information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_dashboard_prefetch_with_http_info(dashboard_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dashboard_id: Id of dashboard (required)
        :param PrefetchDashboardRequest body: Parameters for prefetch request
        :return: PrefetchDashboardRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_dashboard_prefetch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params or
                params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `create_dashboard_prefetch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboard_id'] = params['dashboard_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/dashboards/{dashboard_id}/prefetch', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PrefetchDashboardRequest',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def dashboard(self, dashboard_id, **kwargs):  # noqa: E501
        """Get Dashboard  # noqa: E501

        ### Get information about the dashboard with a specific id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.dashboard(dashboard_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dashboard_id: Id of dashboard (required)
        :param str fields: Requested fields.
        :return: Dashboard
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.dashboard_with_http_info(dashboard_id, **kwargs)  # noqa: E501
        else:
            (data) = self.dashboard_with_http_info(dashboard_id, **kwargs)  # noqa: E501
            return data

    def dashboard_with_http_info(self, dashboard_id, **kwargs):  # noqa: E501
        """Get Dashboard  # noqa: E501

        ### Get information about the dashboard with a specific id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.dashboard_with_http_info(dashboard_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dashboard_id: Id of dashboard (required)
        :param str fields: Requested fields.
        :return: Dashboard
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_id', 'fields']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dashboard" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params or
                params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `dashboard`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboard_id'] = params['dashboard_id']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/dashboards/{dashboard_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Dashboard',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def dashboard_prefetch(self, dashboard_id, **kwargs):  # noqa: E501
        """Get Dashboard Prefetch  # noqa: E501

        ### Get a prefetch for a dashboard with the specified information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.dashboard_prefetch(dashboard_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dashboard_id: Id of dashboard (required)
        :param list[PrefetchDashboardFilterValue] dashboard_filters: JSON encoded string of Dashboard filters that were applied to prefetch
        :return: Prefetch
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.dashboard_prefetch_with_http_info(dashboard_id, **kwargs)  # noqa: E501
        else:
            (data) = self.dashboard_prefetch_with_http_info(dashboard_id, **kwargs)  # noqa: E501
            return data

    def dashboard_prefetch_with_http_info(self, dashboard_id, **kwargs):  # noqa: E501
        """Get Dashboard Prefetch  # noqa: E501

        ### Get a prefetch for a dashboard with the specified information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.dashboard_prefetch_with_http_info(dashboard_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dashboard_id: Id of dashboard (required)
        :param list[PrefetchDashboardFilterValue] dashboard_filters: JSON encoded string of Dashboard filters that were applied to prefetch
        :return: Prefetch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_id', 'dashboard_filters']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dashboard_prefetch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params or
                params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `dashboard_prefetch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboard_id'] = params['dashboard_id']  # noqa: E501

        query_params = []
        if 'dashboard_filters' in params:
            query_params.append(('dashboard_filters', params['dashboard_filters']))  # noqa: E501
            collection_formats['dashboard_filters'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/dashboards/{dashboard_id}/prefetch', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Prefetch',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_dashboard(self, dashboard_id, **kwargs):  # noqa: E501
        """Delete Dashboard  # noqa: E501

        ### Delete the dashboard with a specific id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_dashboard(dashboard_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dashboard_id: Id of dashboard (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_dashboard_with_http_info(dashboard_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_dashboard_with_http_info(dashboard_id, **kwargs)  # noqa: E501
            return data

    def delete_dashboard_with_http_info(self, dashboard_id, **kwargs):  # noqa: E501
        """Delete Dashboard  # noqa: E501

        ### Delete the dashboard with a specific id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_dashboard_with_http_info(dashboard_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dashboard_id: Id of dashboard (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_dashboard" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params or
                params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `delete_dashboard`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboard_id'] = params['dashboard_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/dashboards/{dashboard_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_dashboards(self, **kwargs):  # noqa: E501
        """Search Dashboards  # noqa: E501

        Get information about all dashboards.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_dashboards(async=True)
        >>> result = thread.get()

        :param async bool
        :param str fields: Requested fields.
        :param int id: Match dashboard id.
        :param int page: Requested page.
        :param int per_page: Results per page.
        :param int limit: Number of results to return. (used with offset and takes priority over page and per_page)
        :param int offset: Number of results to skip before returning any. (used with limit and takes priority over page and per_page)
        :param str sorts: Fields to sort by.
        :param str title: Match Dashboard title.
        :param str description: Match Dashboard description.
        :param int content_favorite_id: Filter on a content favorite id.
        :param str space_id: Filter on a particular space.
        :param str deleted: Filter on dashboards deleted status.
        :param str user_id: Filter on dashboards created by a particular user.
        :param str view_count: Filter on a particular value of view_count
        :return: list[Dashboard]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.search_dashboards_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_dashboards_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_dashboards_with_http_info(self, **kwargs):  # noqa: E501
        """Search Dashboards  # noqa: E501

        Get information about all dashboards.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_dashboards_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str fields: Requested fields.
        :param int id: Match dashboard id.
        :param int page: Requested page.
        :param int per_page: Results per page.
        :param int limit: Number of results to return. (used with offset and takes priority over page and per_page)
        :param int offset: Number of results to skip before returning any. (used with limit and takes priority over page and per_page)
        :param str sorts: Fields to sort by.
        :param str title: Match Dashboard title.
        :param str description: Match Dashboard description.
        :param int content_favorite_id: Filter on a content favorite id.
        :param str space_id: Filter on a particular space.
        :param str deleted: Filter on dashboards deleted status.
        :param str user_id: Filter on dashboards created by a particular user.
        :param str view_count: Filter on a particular value of view_count
        :return: list[Dashboard]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields', 'id', 'page', 'per_page', 'limit', 'offset', 'sorts', 'title', 'description', 'content_favorite_id', 'space_id', 'deleted', 'user_id', 'view_count']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_dashboards" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'sorts' in params:
            query_params.append(('sorts', params['sorts']))  # noqa: E501
        if 'title' in params:
            query_params.append(('title', params['title']))  # noqa: E501
        if 'description' in params:
            query_params.append(('description', params['description']))  # noqa: E501
        if 'content_favorite_id' in params:
            query_params.append(('content_favorite_id', params['content_favorite_id']))  # noqa: E501
        if 'space_id' in params:
            query_params.append(('space_id', params['space_id']))  # noqa: E501
        if 'deleted' in params:
            query_params.append(('deleted', params['deleted']))  # noqa: E501
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'view_count' in params:
            query_params.append(('view_count', params['view_count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/dashboards/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Dashboard]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_dashboard(self, dashboard_id, body, **kwargs):  # noqa: E501
        """Update Dashboard  # noqa: E501

        ### Update the dashboard with a specific id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_dashboard(dashboard_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dashboard_id: Id of dashboard (required)
        :param Dashboard body: Dashboard (required)
        :return: Dashboard
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_dashboard_with_http_info(dashboard_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_dashboard_with_http_info(dashboard_id, body, **kwargs)  # noqa: E501
            return data

    def update_dashboard_with_http_info(self, dashboard_id, body, **kwargs):  # noqa: E501
        """Update Dashboard  # noqa: E501

        ### Update the dashboard with a specific id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_dashboard_with_http_info(dashboard_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dashboard_id: Id of dashboard (required)
        :param Dashboard body: Dashboard (required)
        :return: Dashboard
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_dashboard" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params or
                params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `update_dashboard`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_dashboard`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboard_id'] = params['dashboard_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/dashboards/{dashboard_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Dashboard',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
