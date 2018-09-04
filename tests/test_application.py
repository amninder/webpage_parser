# -*- coding: utf-8 -*-

from tests.base import BaseTest
from webpage_parser.application import WebpageParserSession


class TestWebpageParserSession(BaseTest):

    def setUp(self):
        super(TestWebpageParserSession, self).setUp()
        self.wps = WebpageParserSession()

    def test_request_count_no_url(self):
        """Test case to return error when no url is passed"""
        actual_result = self.wps.request_count(url=None)
        expected_result = {
            'error': True,
            'message': 'No url recieved.',
            'data': {}
        }
        self.assertDictEqual(expected_result, actual_result)

    def test_request_count_invalid_url(self):
        """Test case to return error when no url is passed"""
        actual_result = self.wps.request_count(url='abc')
        expected_result = {
            'error': True,
            'message': 'abc is not a valid url',
            'data': {}
        }
        self.assertDictEqual(expected_result, actual_result)
