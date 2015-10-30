import unittest
import tornado
from tornado.testing import AsyncTestCase

from torip.ipapis import IpApi, FreeGeoIp, api_factory
from torip import utilities

__author__ = 'mendrugory'


class TestCase(AsyncTestCase):
    def setUp(self):
        self.ip_api = 'ip_api'
        self.freegeoip = 'freegeoip'
        self.ip_api_ip = 'ip-api.com'
        self.ip_freegeoip = 'freegeoip.net'
        self.io_loop = self.get_new_ioloop()

    def test_get_ip_api(self):
        locator = api_factory(self.ip_api)
        self.assertIsInstance(locator, IpApi)

    def test_get_freegeoip(self):
        locator = api_factory(self.freegeoip)
        self.assertIsInstance(locator, FreeGeoIp)

    def test_google_maps_url(self):
        data = {'lat': 0.0, 'lon': 0.0}
        url = utilities.get_google_maps_url(data)
        self.assertEqual('http://maps.google.com/maps?q=loc:0.0+0.0', url)

    @tornado.testing.gen_test
    def test_ip_api(self):
        locator = IpApi(self.io_loop)
        result = yield locator.locate(self.ip_api_ip)
        self.assertEquals('Amsterdam', result['city'])

    @tornado.testing.gen_test
    def test_freegeoip(self):
        locator = FreeGeoIp(self.io_loop)
        result = yield locator.locate(self.ip_freegeoip)
        self.assertEquals('New York', result['city'])


if __name__ == '__main__':
    unittest.main()
