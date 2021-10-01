import unittest

from pexels_api.photos import PhotosApi
from .secret import SECRET


class APIPhotosTest(unittest.TestCase):

    def test_search(self):

        request = (
            PhotosApi.create(
                'search', secret=SECRET)
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


if __name__ == '__main__':
    unittest.main()
