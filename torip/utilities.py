__author__ = 'mendrugory'


def get_google_maps_url(data):
    """
    It builds a google map url which will point to your lat lon.
    :param data: dictionary with lat and lon information
    :return:
    """
    return "http://maps.google.com/maps?q=loc:{}+{}".format(data['lat'], data['lon'])
