# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.lift_info import LiftInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLiftInfoController(BaseTestCase):
    """LiftInfoController integration test stubs"""

    def test_updateliftinfo(self):
        """Test case for updateliftinfo

        
        """
        response = self.client.open(
            '//IntelligentAgent/updateliftinfo/{LiftIPV6Id}'.format(LiftIPV6Id='LiftIPV6Id_example'),
            method='POST',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
