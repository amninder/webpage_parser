# -*- coding: utf-8 -*-
import logging
import re

from twisted.internet.defer import inlineCallbacks
from autobahn import wamp
from autobahn.twisted.wamp import ApplicationSession

from webpage_parser.config.constants import (
    BROADCAST_COUNT_EVENT,
    REQUEST_COUNT_EVENT,
)
from webpage_parser.config.regex_config import regex
from webpage_parser.utils.parser import (
    HTMLElementCounter,
    request_page,
)

logging.basicConfig(level=logging.INFO)


class WebpageParserSession(ApplicationSession):

    @inlineCallbacks
    def onJoin(self, details):
        """
        This method is triggered when the client joines the crossbario session.

        Args:
            details (autobahn.wamp.types.SessionDetails): details of the session joined.
        """
        logging.info('session joined with details: {}'.format(details))
        yield self.register(self)

    @wamp.register(REQUEST_COUNT_EVENT)
    def request_count(self, url):
        """
        This endpoint is provided to return the element counts of the webpage.

        Args:
            url (str): url of website to count the elements.

        Returns:
            result (dict): dictionary result
        """
        logging.info('request_count() fired with: {}'.format(url))
        result = {'error': True, 'message': '', 'data': {}}
        if not url:
            logging.error('No url passed')
            result.update({'error': True, 'message': 'No url recieved.'})
            return result

        if not re.match(regex, url):
            message = '{} is not a valid url'.format(url)
            logging.error(message)
            result.update({
                'error': True,
                'message': message,
                'data': {}
            })
            return result

        try:
            html = request_page(url)
            parser = HTMLElementCounter()
            parser.feed(html)
            data = parser.element_count
            result.update({
                'error': False,
                'message': 'Webpage parsed',
                'data': data
            })
            self.publish(BROADCAST_COUNT_EVENT, result)
            logging.info('Broadcasted {}'.format(result))
        except Exception as e:
            result.update({
                'error': True,
                'message': 'Exception: {}'.format(e),
                'data': {}
            })
        return result
