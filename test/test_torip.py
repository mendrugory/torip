import os
import unittest
import tornado
from tornado.testing import AsyncTestCase

from torip.ipapis import IpApi, AbstractApi, api_factory
from torip import utilities
from torip.exceptions import ToripException

__author__ = 'mendrugory'


class TestCase(AsyncTestCase):
    def setUp(self):
        self.abstractapi_token = os.getenv('ABSTRACTAPI_TOKEN')
        self.ip_api = 'ip-api'
        self.google_dns = '8.8.8.8'
        self.ip_api_ip = 'ip-api.com'
        self.abstractapi_ip = 'ipgeolocation.abstractapi.com'
        self.io_loop = self.get_new_ioloop()

    def test_get_ip_api(self):
        locator = api_factory(self.ip_api)
        self.assertIsInstance(locator, IpApi)

    def test_google_maps_url(self):
        data = {'lat': 0.0, 'lon': 0.0}
        url = utilities.get_google_maps_url(data)
        self.assertEqual('http://maps.google.com/maps?q=loc:0.0+0.0', url)

    @tornado.testing.gen_test
    def test_ip_api(self):
        locator = IpApi(self.io_loop)
        result = yield locator.locate(self.ip_api_ip)
        self.assertEqual('Ashburn', result['city'])

    @tornado.testing.gen_test
    def test_ip_api_private_address(self):
        address = '192.168.1.1'
        locator = IpApi(self.io_loop)
        with self.assertRaises(ToripException) as context:
            yield locator.locate(address)
        self.assertIsInstance(context.exception, ToripException)

    @tornado.testing.gen_test
    def test_abstract_ip(self):
        locator = AbstractApi(api_token=self.abstractapi_token, ioloop=self.io_loop)
        result = yield locator.locate(self.google_dns)
        self.assertEqual(self.google_dns, result['address'])

    @tornado.testing.gen_test
    def test_abstract_ip_private_address(self):
        address = '192.168.1.1'
        locator = AbstractApi(api_token=self.abstractapi_token, ioloop=self.io_loop)
        with self.assertRaises(ToripException) as context:
            yield locator.locate(address)
        self.assertIsInstance(context.exception, ToripException)


if __name__ == '__main__':
    unittest.main()
