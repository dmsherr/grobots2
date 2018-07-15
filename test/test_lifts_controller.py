# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.lift_info import LiftInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLiftsController(BaseTestCase):
    """LiftsController integration test stubs"""

    def test_get_lift_locations(self):
        """Test case for get_lift_locations

        
        """
        response = self.client.open(
            '//IntelligentAgent/LiftLocations/{STATUS}'.format(STATUS=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_starts(self):
        """Test case for get_starts

        
        """
        response = self.client.open(
            '//IntelligentAgent/starts/{LOCATION}'.format(LOCATION='LOCATION_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getlifts(self):
        """Test case for getlifts

        
        """
        response = self.client.open(
            '//IntelligentAgent/lifts',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
