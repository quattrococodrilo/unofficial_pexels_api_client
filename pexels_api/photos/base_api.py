from pexels_api.enums import PhotoEndpointEnum
from pexels_api.errors import EndpointNotExists


class BaseApi:

    _endpoint = None
    _response = None
    _data_object = None
    _data = {}
    _secret = None
    _url = None
    _url_params = {}

    def __init__(self, end_point, secret) -> None:
        self._end_point(end_point, secret)

    @staticmethod
    def create(end_point, secret):
        pass

    def _add_param(self, key='', value='') -> None:
        self._url_params[key] = value

    def _enum_exists(self, param, _enum):
        if param in _enum.__members__.keys():
            return True

        return False

    def _end_point(self, end_point, secret):
        if not end_point in PhotoEndpointEnum.__members__.keys():
            raise EndpointNotExists(end_point, PhotoEndpointEnum)

        self._url = PhotoEndpointEnum[end_point].url()
        self._endpoint = end_point
        self._secret = secret

    @property
    def url(self):
        if self._response:
            return self._response.url
        return None

    @property
    def data(self):
        return self._data_object

    def request(self, _url=None, _url_params=None, _secret=None):
        pass
