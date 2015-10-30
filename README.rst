torip
=====

Python library for Tornado web framework to locate IPs or server names.

Torip will provide you information like country, city, zip code or the
url of google maps.

Torip has been developed and tested using Python3.4

Installation
------------

.. code:: console

    $ pip install torip

Available APIs
--------------

Torip supports the following APIs:

`ip-api <http://ip-api.com/>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is also the default API.

.. code:: python

    from torip.locator import Locator
    locator = Locator(api_name='ip-api')

or

.. code:: python

    from torip.locator import Locator
    locator = Locator()  # default API

`freegeoip.net <https://freegeoip.net>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from torip.locator import Locator
    locator = Locator(api_name='freegeoip')

Example
-------

.. code:: python

    import tornado
    from torip.locator import Locator
    ip = ''  # IP or server name
    @tornado.gen.coroutine
    def function():
        try:
            locator = Locator()
            result = yield locator.locate(ip)
            print(result)
        except Exception as e:
            print(str(e))
        finally:
            ioloop.stop()
    ioloop = tornado.ioloop.IOLoop.instance()
    ioloop.add_callback(function)
    ioloop.start()