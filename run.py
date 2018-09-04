# -*- coding: utf-8 -*-
import sys
from os import environ

from twisted.python import log

from webpage_parser.application import WebpageParserSession
from autobahn.twisted.wamp import ApplicationRunner


def main():
    log.startLogging(sys.stdout)

    realm = 'realm1'

    runner = ApplicationRunner(
        environ.get('AUTOBAHN_DEMO_ROUTER', u'ws://127.0.0.1:8080/ws'),
        realm
    )
    runner.run(WebpageParserSession)


if __name__ == "__main__":
    main()
