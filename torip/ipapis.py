import json
from tornado import httpclient
from tornado.gen import coroutine

__author__ = 'mendrugory'


def api_factory(api_name):
    """
    Factory function which will return a IpLocateApi class. The default is IpApi()
    :param api_name:
    :return:
    """
    if api_name == 'freegeoip':
        return FreeGeoIp()
    else:
        return IpApi()  # ip-api


class LocateApi:
    def __init__(self):
        self.url = None
        self.original_url = None

    @coroutine
    def locate(self, ip):
        self.build_url(ip)
        data = yield self.fetch_data()
        result = None
        if data:
            result = self.adapt(data)
        return result

    @coroutine
    def fetch_data(self):
        http_client = httpclient.AsyncHTTPClient()
        try:
            response = yield http_client.fetch(self.url)
            data = json.loads(response.body.decode('utf-8'))
        finally:
            http_client.close()
        return data

    def build_url(self, ip):
        self.url = self.original_url.format(ip)

    def adapt(self, data):
        return data


class IpApi(LocateApi):
    """
    IpLocateApi for the api of ip-api.com
    """

    def __init__(self):
        super().__init__()
        self.original_url = 'http://ip-api.com/json/{}'

    def build_url(self, ip):
        self.url = self.original_url.format(ip)

    def adapt(self, data):
        return {
            'region_name': data['regionName'],
            'region_code': data['region'],
            'isp': data['isp'],
            'country_name': data['country'],
            'country_code': data['countryCode'],
            'city': data['city'],
            'lat': data['lat'],
            'lon': data['lon'],
            'address': data['query'],
            'time_zone': data['timezone'],
            'zip_code': data['zip']
        }


class FreeGeoIp(LocateApi):
    """
    IpLocateApi for the api of ip-api.com
    """

    def __init__(self):
        super().__init__()
        self.original_url = 'https://freegeoip.net/json/{}'

    def adapt(self, data):
        return {
            'region_name': data['region_name'],
            'region_code': data['region_code'],
            'country_name': data['country_name'],
            'country_code': data['country_code'],
            'city': data['city'],
            'lat': data['latitude'],
            'lon': data['longitude'],
            'address': data['ip'],
            'time_zone': data['time_zone'],
            'zip_code': data['zip_code']
        }
