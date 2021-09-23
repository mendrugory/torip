from tornado.gen import coroutine

from torip.ipapis import api_factory

__author__ = 'mendrugory'


class Locator:
    """
    Main Class which will be the responsible of locating the IP.
    """

    def __init__(self, api_name=None, **config):
        self.api_name = api_name
        self.config = config

    @coroutine
    def locate(self, address):
        """
        It locates the IP Address / Server Name
        :param address: String IP Address / Server Name
        :return:
        """
        api = api_factory(self.api_name, **self.config)
        result = yield api.locate(address)
        return result
