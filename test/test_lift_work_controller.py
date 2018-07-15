# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.lift_work import LiftWork  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLiftWorkController(BaseTestCase):
    """LiftWorkController integration test stubs"""

    def test_get_lift_location_work_list(self):
        """Test case for get_lift_location_work_list

        
        """
        response = self.client.open(
            '//IntelligentAgent/Liftwork/Location/{LocationId}'.format(LocationId=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_lift_work_list(self):
        """Test case for get_lift_work_list

        
        """
        response = self.client.open(
            '//IntelligentAgent/Liftwork/Lift/{LiftIPV6Id}'.format(LiftIPV6Id=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
