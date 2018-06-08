# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning)   # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.homepage_api import HomepageApi  # noqa: E501
from swagger_client.rest import ApiException


class TestHomepageApi(unittest.TestCase):
    """HomepageApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.homepage_api.HomepageApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_all_homepage_items(self):
        """Test case for all_homepage_items

        Get All Homepage Items  # noqa: E501
        """
        pass

    def test_all_homepage_sections(self):
        """Test case for all_homepage_sections

        Get All Homepage sections  # noqa: E501
        """
        pass

    def test_create_homepage_item(self):
        """Test case for create_homepage_item

        Create Homepage Item  # noqa: E501
        """
        pass

    def test_create_homepage_section(self):
        """Test case for create_homepage_section

        Create Homepage section  # noqa: E501
        """
        pass

    def test_delete_homepage_item(self):
        """Test case for delete_homepage_item

        Delete Homepage Item  # noqa: E501
        """
        pass

    def test_delete_homepage_section(self):
        """Test case for delete_homepage_section

        Delete Homepage section  # noqa: E501
        """
        pass

    def test_homepage_item(self):
        """Test case for homepage_item

        Get Homepage Item  # noqa: E501
        """
        pass

    def test_homepage_section(self):
        """Test case for homepage_section

        Get Homepage section  # noqa: E501
        """
        pass

    def test_update_homepage_item(self):
        """Test case for update_homepage_item

        Update Homepage Item  # noqa: E501
        """
        pass

    def test_update_homepage_section(self):
        """Test case for update_homepage_section

        Update Homepage section  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
