# -*- coding: utf-8 -*-
import mock
import unittest

from webpage_parser.utils.parser import (
    HTMLElementCounter,
    parse_xml_string,
    request_page,
)


class TestParser(unittest.TestCase):

    def setUp(self):
        super(TestParser, self).setUp()

    def test_request_page_is_not_string(self):
        """Test cast to raise exception if the url is not string."""
        with self.assertRaises(Exception):
            request_page(12)

    @mock.patch('six.moves.urllib.request.urlopen')
    def test_request_page_valid_http_url(self, mock_urlopen):
        """Test case to request page if the url is valid http."""

        request_page('http://google.com')
        self.assertTrue(mock_urlopen.called)
        mock_urlopen.assert_called_with('http://google.com')

    @mock.patch('six.moves.urllib.request.urlopen')
    def test_request_page_valid_https_url(self, mock_urlopen):
        """Test case to request page if the url is valid https."""

        request_page('https://google.com')
        self.assertTrue(mock_urlopen.called)
        mock_urlopen.assert_called_with('https://google.com')

    @mock.patch('six.moves.urllib.request.urlopen')
    def test_request_page_valid_ip_address(self, mock_urlopen):
        """Test case to request page if the url is valid ip address."""

        request_page('https://10.0.0.1')
        self.assertTrue(mock_urlopen.called)
        mock_urlopen.assert_called_with('https://10.0.0.1')

    @mock.patch('six.moves.urllib.request.urlopen')
    def test_request_page_valid_ip_address_and_port(self, mock_urlopen):
        """Test case to request page if the url is valid ip address and port."""

        request_page('https://10.0.0.1:9090')
        self.assertTrue(mock_urlopen.called)
        mock_urlopen.assert_called_with('https://10.0.0.1:9090')

    def test_parse_xml_string(self):
        """Test case to parse xml string"""
        example_xml = """
        <a>
          <b></b>
          <b>
            <c>
              <d></d>
            </c>
          </b>
        </a>"""
        actual_data = parse_xml_string(example_xml)
        expected_data = {
            'error': False,
            'message': 'xml parse successful',
            'data': {
                'a': 1,
                'b': 2,
                'c': 1,
                'd': 1
            }}

        self.assertDictEqual(expected_data, actual_data)

    def test_parse_xml_string_one_element(self):
        """Test case to xml element with one element"""
        example_xml = """<a></a>"""
        actual_data = parse_xml_string(example_xml)
        expected_data = {
            'error': False,
            'message': 'xml parse successful',
            'data': {'a': 1}
        }
        self.assertDictEqual(expected_data, actual_data)

    def test_parse_xml_string_no_element(self):
        """Test case to xml element with one element"""
        actual_data = parse_xml_string("""""")
        expected_data = {'error': True, 'message': 'Empty XML', 'data': {}}
        self.assertDictEqual(expected_data, actual_data)

    def test_parse_xml_string_html_content(self):
        """Test case to xml element for html content"""
        example_xml = """
        <!DOCTYPE html>
        <html>
            <body>

                <h1>My First Heading</h1>

                <p>My first paragraph.</p>
                <div>
                    <div></div>
                    <ul>
                        <li></li>
                        <li></li>
                        <li></li>
                    </ul>
                </div>

            </body>
        </html>
        """
        actual_data = parse_xml_string(example_xml)
        expected_data = {
            'error': False,
            'message': 'xml parse successful',
            'data': {
                'html': 1,
                'body': 1,
                'h1': 1,
                'p': 1,
                'div': 2,
                'ul': 1,
                'li': 3
            }}
        self.assertDictEqual(expected_data, actual_data)

    def test_parse_xml_string_unstructured_element(self):
        """Test case to xml element with unstructured elements."""
        example_xml = """
        <a>
          <b><b>
          <b>
            <c>
              <d></d>
            </c>
          </b>
        </a>"""
        actual_data = parse_xml_string(example_xml)
        expected_data = {
            'error': True,
            'message': 'Unstructured data',
            'data': {}
        }
        self.assertDictEqual(expected_data, actual_data)

    def test_html_feed(self):
        """Test to parse html page"""
        example_xml = """
        <!DOCTYPE html>
        <html>
            <body>

                <h1>My First Heading</h1>

                <p>My first paragraph.</p>
                <div>
                    <div></div>
                    <ul>
                        <li></li>
                        <li></li>
                        <li></li>
                    </ul>
                </div>

            </body>
        </html>
        """
        parser = HTMLElementCounter()
        parser.feed(example_xml)
        expected_data = {
            'html': 1,
            'body': 1,
            'h1': 1,
            'p': 1,
            'div': 2,
            'ul': 1,
            'li': 3
        }
        self.assertDictEqual(expected_data, parser.element_count)
