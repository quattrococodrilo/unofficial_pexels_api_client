import requests
from pexels_api.errors import IdNotFound

from .base_api import BaseApi


class Photo(BaseApi):

    _photo_id = None

    def __init__(self, end_point, secret) -> None:
        super().__init__(end_point, secret)

    @staticmethod
    def create(end_point, secret):
        """ Create a new APIPhotos instance. 
        @param end_point {string}: search | curated | photos 
        """
        return Photo(end_point, secret)

    def request(self) -> dict:

        if not self._id:
            raise IdNotFound(self._endpoint)

        url = self._url

        if not self._url.endswith('/'):
            url += '/'

        url += self._id

        self._response = requests.get(
            url,
            headers={
                'Authorization': self._secret,
            }
        )

        self._data = self._response.json()

        self._data_object = self._data

        return self

    def photo_id(self, id):
        self._id = str(id)

        return self
