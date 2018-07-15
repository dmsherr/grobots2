# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.o_auth_token import OAuthToken  # noqa: E501
from swagger_server.models.success import Success  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAccessControlController(BaseTestCase):
    """AccessControlController integration test stubs"""

    def test_get_auth_code(self):
        """Test case for get_auth_code

        
        """
        query_string = [('grant_type', 'grant_type_example'),
                        ('client_id', 'client_id_example'),
                        ('redirect_uri', 'redirect_uri_example')]
        response = self.client.open(
            '//IntelligentAgent/oauth20/authorize',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_token_request(self):
        """Test case for get_token_request

        
        """
        query_string = [('grant_type', 'grant_type_example'),
                        ('client_id', 'client_id_example'),
                        ('client_secret', 'client_secret_example')]
        response = self.client.open(
            '//IntelligentAgent/oauth20/token',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_token_request(self):
        """Test case for post_token_request

        
        """
        response = self.client.open(
            '//IntelligentAgent/oauth20/token',
            method='POST',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
