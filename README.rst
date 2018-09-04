==============
Webpage Parser
==============


This is a small application for publishing and receiving messages over **Observer Pattern** architecture. On the website you are presented with the text field and a button.
Each client is connected to the same message router and listens for the events to be publshed. Upon loading the webpage, the event is broadcasted over the network and all the clients
connected that are subscribed to the same subscription key receive the object.

Upon requesting the webpage data, the system returns the element count in ``JSON``.

The expected url pattern is as follows:

.. code::

   <protocol>://<domain name>.<something>


Current accept protocols are:

1. ``http``
2. ``https``


Any message that falls outside this pattern will be rejected. The structure of the message that are distributed amoung client and server is as follow:

.. code:: json

   {
     "error": false,
     "message": "Webpage parsed",
     "data": {
         "html": 1,
         "body": 1
     }
   }


Examples:

.. code::

    http://google.com
    https://google.com

How to run
----------

.. code:: sh

    >>> docker-compose up


Open: **localhost:8081/**


Python Requirements
-------------------

I am using `pipenv` for package manager. Following are the steps for activate the shell

.. code:: sh

   >>> pip install pipenv
   >>> pipenv install --dev
   >>> pipenv shell


Tests
-----

Even though I have developed this application on ``python37``, the code is also compatible with ``py27``. In order to run tests in current environment, run the following command:

.. code:: sh

   >>> pipenv shell
   >>> make test


This will also give you the full coverage of the source code. To run tests under different python versions run the following:

.. code:: sh

   >>> make test-all


Docs
----

.. code:: sh

   >>> pipenv shell
   >>> make docs


Versioning
----------

Following are the commands to bump up the version

.. code:: bash

   >>> pipenv shell
   >>> make major
   >>> make minor
   >>> make patch
