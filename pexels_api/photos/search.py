import re

import requests
from pexels_api.enums import (ColorEnum, LocaleEnum, OrientationEnum,
                              PhotoUrlParamsEnum, SizeEnum)
from pexels_api.errors import ParamNotExists

from .base_api import BaseApi
from .response_data import ResponseData


class Search(BaseApi):

    def __init__(self, end_point, secret) -> None:
        super().__init__(end_point, secret)

    @staticmethod
    def create(end_point, secret):
        """ Create a new APIPhotos instance. 
        @param end_point {string}: search | curated | photos 
        """
        return Search(end_point, secret)

    def request(self, _url=None, _url_params=None, _secret=None) -> dict:
        self._response = requests.get(
            _url if _url else self._url,
            params=_url_params if _url_params else self._url_params,
            headers={
                'Authorization': _secret if _secret else self._secret,
            }
        )
        self._data = self._response.json()

        self._data_object = ResponseData.create(self._data)

        return self

    def next_page(self):
        if 'next_page' in self._data and self._data['next_page']:
            request = Search(self._endpoint, self._secret)
            request.request(
                _url=self._data['next_page'],
                _secret=self._secret
            )

            return request

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
