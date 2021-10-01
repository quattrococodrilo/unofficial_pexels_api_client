class PhotosResponse:

    _data = None

    def __init__(self, json) -> None:
        self._data = json

    def create(json):
        return PhotosResponse(json)

    @property
    def photos(self) -> dict:
        return self._data['photos']

    @property
    def page(self) -> int:
        return self._data['page']

    @property
    def per_page(self) -> int:
        return self._data['per_page']

    @property
    def total_results(self):
        return self._data['total_results']

    @property
    def next_page(self):
        return self._data['next_page']
