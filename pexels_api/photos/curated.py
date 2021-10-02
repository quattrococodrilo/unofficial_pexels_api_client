import requests

from pexels_api.enums import PhotoUrlParamsEnum
from .response_data import ResponseData
from .base_api import BaseApi


class Curated(BaseApi):

    def __init__(self, end_point, secret) -> None:
        super().__init__(end_point, secret)

    @staticmethod
    def create(end_point, secret):
        """ Create a new APIPhotos instance. 
        @param end_point {string}: search | curated | photos 
        """
        return Curated(end_point, secret)

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
            request = Curated(self._endpoint, self._secret)
            request.request(
                _url=self._data['next_page'],
                _secret=self._secret
            )

            return request

    def page(self, number=1):
        self._add_param(PhotoUrlParamsEnum.page.value, number)

        return self

    def per_page(self, number=15):
        self._add_param(PhotoUrlParamsEnum.per_page.value, number)

        return self
