import json
import re
from tornado import httpclient
from tornado.gen import coroutine

from torip import utilities
from torip.exceptions import ToripException

__author__ = 'mendrugory'

IPV4_REGEX_PATTERN = '^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'

def api_factory(api_name, **config):
    """
    Factory function which will return a IpLocateApi class. The default is AbstractApi()
    :param api_name:
    :return:
    """
    if api_name == 'ip-api':
        return IpApi(**config)
    else:
        return AbstractApi(**config)

def is_ipv4(ip):
    return re.match(IPV4_REGEX_PATTERN, ip) is not None

class LocateApi:
    def __init__(self, api_token=None, ioloop=None):
        self.url = None
        self.original_url = None
        self.ioloop = ioloop
        self.api_token=api_token

    @coroutine
    def locate(self, ip):
        """
        Main function of the class whose output will be a dictionary with the information
        provided by the selected API.
        :param ip: IP or server name (String)
        :return: dict()
        """
        err = self.check_address(ip)
        if err is not None:
            raise ToripException(f"{err}")
        url = self.build_url(ip)
        data = yield self.fetch_data(url)
        result = None
        if data:
            result = LocateApi.enrich(self.adapt(data))
        return result

    @coroutine
    def fetch_data(self, url):
        """
        It fetches the data from the self.url
        :return: dict()
        """
        http_client = self.get_http_client()
        try:
            response = yield http_client.fetch(url)
            data = json.loads(response.body.decode('utf-8'))
        finally:
            http_client.close()
        return data

    def get_http_client(self):
        """
        It creates an instance of AsyncHTTPClient. You can pass the ioloop (prepared for testing).
        :return:
        """
        return httpclient.AsyncHTTPClient(self.ioloop) if self.ioloop else httpclient.AsyncHTTPClient()

    def check_address(self, ip):
        return None

    def build_url(self, ip):
        """
        It fetches the data from the self.url
        :return: dict()
        """
        pass

    def adapt(self, data):
        """
        It adapt the output of the data
        :param data: dictionary with the data from the API
        :return: dict()
        """
        return data

    @staticmethod
    def enrich(data):
        """
        It enrich the received data with the utilities functions
        :param data: dict()
        :return: dict()
        """
        data['google_maps'] = utilities.get_google_maps_url(data)
        return data


class IpApi(LocateApi):
    """
    IpLocateApi for the api of ip-api.com
    """

    def __init__(self, api_token=None, ioloop=None):
        super().__init__(api_token=api_token, ioloop=ioloop)
        self.original_url = 'http://ip-api.com/json/{}'

    def build_url(self, ip):
        return self.original_url.format(ip)

    def adapt(self, data):
        if data.get('status') == 'fail':
            raise ToripException('Error: {}'.format(data['message']))
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


class AbstractApi(LocateApi):
    """
    IpLocateApi for the api of abstractapi.com
    """

    def __init__(self, api_token=None, ioloop=None):
        super().__init__(api_token=api_token, ioloop=ioloop)
        self.original_url = 'https://ipgeolocation.abstractapi.com/v1/?ip_address={}&api_key={}'

    def check_address(self, ip):
        if not is_ipv4(ip):
            return "Error: Locator AbstractApi only accepts IPs"

    def build_url(self, ip):
        return self.original_url.format(ip, self.api_token)

    def adapt(self, data):
        if data and 'connection' not in data:
            raise ToripException(f"Error locating address {data['ip_address']}")
        return {
            'region_name': data['region'],
            'region_code': data['region_iso_code'],
            'isp': data['connection']['isp_name'],
            'country_name': data['country'],
            'country_code': data['country_code'],
            'city': data['city'],
            'lat': data['latitude'],
            'lon': data['longitude'],
            'address': data['ip_address'],
            'time_zone': data['timezone']['name'],
            'zip_code': data['postal_code']
        }
