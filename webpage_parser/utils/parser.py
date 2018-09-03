# -*- coding: utf-8 -*-
from collections import defaultdict
import logging
import re
from xml.etree import ElementTree
from xml.etree.ElementTree import (
    XMLParser,
    ParseError,
)

import six
from six.moves import urllib
from six.moves.html_parser import HTMLParser

from webpage_parser.config.regex_config import regex


logging.basicConfig(level=logging.INFO)


class HTMLElementCounter(HTMLParser):

    """
    Class to parse HTML Element and maintain the count. This class inherits
    from :class:`~html.parser.HTMLParser`.
    """

    def __init__(self):
        self.root = None
        self.tree = []
        self.element_count = defaultdict(lambda: 0)
        HTMLParser.__init__(self)

    def feed(self, data):
        """
        This is the entry point of the class.

        Args:

            data (str): stringify xml
        """
        HTMLParser.feed(self, data)
        return self.root

    def handle_starttag(self, tag, attrs):
        """This method handles the start tag.

        Args:

            tag (str): xml tag name.
            attrs (str): attribute of the xml element
        """
        self.element_count[tag] += 1
        if len(self.tree) == 0:
            element = ElementTree.Element(tag, dict(self.__filter_attrs(attrs)))
            self.tree.append(element)
            self.root = element
        else:
            element = ElementTree.SubElement(self.tree[-1], tag, dict(self.__filter_attrs(attrs)))
            self.tree.pop()

    def handle_endtag(self, tag):
        """
        This method handles the ending tag of the current element

        Args:

            tag (str): Element to pop out.
        """
        if self.tree:
            self.tree.pop()

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_data(self, data):
        if self.tree:
            self.tree[-1].text = data

    def get_root_element(self):
        return self.root

    def __filter_attrs(self, attrs):
        return filter(lambda x: x[0] and x[1], attrs) if attrs else []


def request_page(url):
    """
    This method requests the url and counts the number of elements.

    Args:

        url(str): url of the website to be requested.

    Returns:
        (str): contents of the webpage
    """

    if re.match(regex, url) is None:
        raise Exception('{} is not a valid url')
    page = urllib.request.urlopen(url)
    data = page.read()
    if isinstance(data, six.binary_type):
        data = str(data)
    return data


def parse_xml_string(data):
    """
    This method parses through the xml string and counts the number of
    occurence of the xml tag.

    Args:

        data (str): Stringify data of xml

    Returns:
        ELEMENT_COUNT (dict): dictionary of values containing counts of elements
    """
    class ElementCounter:
        """Class to get count of Element occurance."""
        ELEMENT_COUNT = defaultdict(lambda: 0)

        def start(self, tag, attrib):
            self.ELEMENT_COUNT[tag] += 1

        def end(self, tag):
            pass

        def data(self, data):
            pass

        def close(self):
            pass
    result = {'error': True, 'data': {}, 'message': 'Unstructured XML'}
    target = ElementCounter()
    parser = XMLParser(target=target)
    try:
        parser.feed(data)
    except ParseError as e:
        result.update({'error': True, 'message': 'Unstructured data'})
        return result
    except Exception as e:
        result.update({'error': True, 'message': '{}'.format(e)})
        return result

    try:
        parser.close()
    except ParseError as e:
        result.update({'error': True, 'message': 'Empty XML'})
        return result
    except Exception as e:
        result.update({'error': True, 'message': '{}'.format(e)})
        return result
    result.update({
        'error': False,
        'message': 'xml parse successful',
        'data': dict(target.ELEMENT_COUNT)})
    return result
