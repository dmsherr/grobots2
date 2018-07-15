# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.lift_info import LiftInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestScheduleController(BaseTestCase):
    """ScheduleController integration test stubs"""

    def test_get_scheduled_starts(self):
        """Test case for get_scheduled_starts

        
        """
        response = self.client.open(
            '//IntelligentAgent/starts',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
