from pexels_api.enums import PhotoEndpointEnum
from pexels_api.errors import EndpointNotExists

from .curated import Curated
from .photo import Photo
from .search import Search


class PhotosClient:

    @staticmethod
    def create(end_point, secret):
        if not end_point in PhotoEndpointEnum.__members__.keys():
            raise EndpointNotExists(end_point, PhotoEndpointEnum)

        if end_point == PhotoEndpointEnum.photos.name:
            return Photo(end_point, secret)

        elif end_point == PhotoEndpointEnum.curated.name:
            return Curated(end_point, secret)

        elif end_point == PhotoEndpointEnum.search.name:
            return Search(end_point, secret)
