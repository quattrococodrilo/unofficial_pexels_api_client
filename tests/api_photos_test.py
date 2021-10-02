import unittest
from pexels_api.enums import PhotoUrlParamsEnum

from pexels_api.photos import PhotosClient
from requests.api import request

from .secret import SECRET


class APIPhotosTest(unittest.TestCase):

    def test_search(self):

        request = (
            PhotosClient
            .create('search', secret=SECRET)
            .query('mountains')
            .orientation('landscape')
            .size('medium')
            .color('blue')
            .locale('es')
            .page(1)
            .per_page(5)
            .request()
        )

        self.assertEqual(5, len(request.data.photos))

        request2 = request.next_page()

        self.assertEqual(5, len(request2.data.photos))

        self.assertTrue('page=2' in request2.url)

    def test_curated(self):

        request = (
            PhotosClient
            .create('curated', secret=SECRET)
            .page(1)
            .per_page(5)
            .request()
        )

        self.assertEqual(5, len(request.data.photos))

        request2 = request.next_page()

        self.assertEqual(5, len(request2.data.photos))

        self.assertTrue('page=2' in request2.url)

    def test_photo(self):

        photo_id = 4415019

        request = (
            PhotosClient
            .create('photos', secret=SECRET)
            .photo_id(photo_id)
            .request()
        )

        self.assertEqual(photo_id, request.data['id'])


if __name__ == '__main__':
    unittest.main()
