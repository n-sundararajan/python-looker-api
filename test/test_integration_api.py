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
from swagger_client.api.integration_api import IntegrationApi  # noqa: E501
from swagger_client.rest import ApiException


class TestIntegrationApi(unittest.TestCase):
    """IntegrationApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.integration_api.IntegrationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_accept_integration_hub_legal_agreement(self):
        """Test case for accept_integration_hub_legal_agreement

        Accept Integration Hub Legal Agreement  # noqa: E501
        """
        pass

    def test_all_integration_hubs(self):
        """Test case for all_integration_hubs

        Get All Integration Hubs  # noqa: E501
        """
        pass

    def test_all_integrations(self):
        """Test case for all_integrations

        Get All Integrations  # noqa: E501
        """
        pass

    def test_create_integration_hub(self):
        """Test case for create_integration_hub

        Create Integration Hub  # noqa: E501
        """
        pass

    def test_delete_integration_hub(self):
        """Test case for delete_integration_hub

        Delete Integration Hub  # noqa: E501
        """
        pass

    def test_fetch_integration_form(self):
        """Test case for fetch_integration_form

        Fetch Remote Integration Form  # noqa: E501
        """
        pass

    def test_integration(self):
        """Test case for integration

        Get Integration  # noqa: E501
        """
        pass

    def test_integration_hub(self):
        """Test case for integration_hub

        Get Integration Hub  # noqa: E501
        """
        pass

    def test_update_integration(self):
        """Test case for update_integration

        Update Integration  # noqa: E501
        """
        pass

    def test_update_integration_hub(self):
        """Test case for update_integration_hub

        Update Integration Hub  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
