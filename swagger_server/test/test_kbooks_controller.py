# coding: utf-8
"""
Script: test_kbooks_controller.py
Description: Test module.
"""

__author__ = 'aklankdiwakar@gmail.com'

from flask import json

from swagger_server.test import BaseTestCase
from swagger_server.utils.decorator import parse_swagger_yaml


class TestKbooksController(BaseTestCase):
    """KbooksController integration test stubs"""

    @parse_swagger_yaml
    def test_add_artifact_line(self):
        """Test case for add_artifact_line

        Do calculation and generate invoice
        """

        response = self.client.open(
            '/kbooks/{story_number}'.format(story_number=self.story_number),
            method='POST',
            data=json.dumps(self.body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
