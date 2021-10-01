import requests
import re

from pexels_api.enums import PhotoEndpointEnum, PhotoUrlParamsEnum, OrientationEnum, SizeEnum, ColorEnum, LocaleEnum
from pexels_api.errors import EndpointNotExists, ParamNotExists
from .photos_response import PhotosResponse


class PhotosApi:

    _end_point = None
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
        """ Create a new APIPhotos instance. 
        @param end_point {string}: search | curated | photos 
        """
        return PhotosApi(end_point, secret)

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
        self._end_point = end_point
        self._secret = secret

    @property
    def url(self):
        if self._response:
            return self._response.url
        return None

    @property
    def data(self):
        return self._data_object

    def query(self, q=''):
        self._add_param(PhotoUrlParamsEnum.query.value, q)

        return self

    def orientation(self, _orientation):
        if not self._enum_exists(_orientation, OrientationEnum):
            raise ParamNotExists('Orientation', OrientationEnum, _orientation)

        self._add_param(PhotoUrlParamsEnum.orientation.value,
                        OrientationEnum[_orientation].value)

        return self

    def size(self, _size):
        if not self._enum_exists(_size, SizeEnum):
            raise ParamNotExists('Orientation', SizeEnum, _size)

        self._add_param(PhotoUrlParamsEnum.size.value,
                        SizeEnum[_size].value)

        return self

    def color(self, _color):
        if re.match(r'^#\w{4,}', _color):
            self._add_param(PhotoUrlParamsEnum.color.value, _color)

            return self

        if self._enum_exists(_color, ColorEnum):
            self._add_param(PhotoUrlParamsEnum.color.value,
                            ColorEnum[_color].value)
        else:
            raise ParamNotExists('Orientation', ColorEnum, _color)

        return self

    def locale(self, _locale):
        if not self._enum_exists(_locale, LocaleEnum):
            raise ParamNotExists('Orientation', LocaleEnum, _locale)

        self._add_param(PhotoUrlParamsEnum.locale.value,
                        LocaleEnum[_locale].value)

        return self

    def page(self, number=1):
        self._add_param(PhotoUrlParamsEnum.page.value, number)

        return self

    def per_page(self, number=15):
        self._add_param(PhotoUrlParamsEnum.per_page.value, number)

        return self

    def request(self, _url=None, _url_params=None, _secret=None) -> dict:
        self._response = requests.get(
            _url if _url else self._url,
            params=_url_params if _url_params else self._url_params,
            headers={
                'Authorization': _secret if _secret else self._secret,
            }
        )
        self._data = self._response.json()

        self._data_object = PhotosResponse.create(self._data)

        return self

    def next_page(self):
        if 'next_page' in self._data and self._data['next_page']:
            request = PhotosApi(self._end_point, self._secret)
            request.request(
                _url=self._data['next_page'],
                _secret=self._secret
            )

            return request
