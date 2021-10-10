# Unofficial Pexels APi Client

This Python API for Pexels is a work in progress and by now only works for photos, for use this API you need to have your own secret, and yo can get it here: 
https://www.pexels.com/api/

## Quick Start

### Install

Clone this git and do `pip install .`
### Photos

If you need get only a photo.

    from pexels_api.photos import PhotosClient

    request = (
        PhotosClient
        .create('photos', 'yourSecret')
        .photo_id(4415019)
        .request()
    )

    print(request.data)

    $ {'id': 4415019, 'width': 3817, 'height': 2863...


Search photos:

    from pexels_api.photos import PhotosClient

    request = (
        PhotosClient
        .create('search', 'YourSecret')
        .query('mountains')
        .size('medium')
        .orientation('landscape')
        .request() # This is not optional
    )

    print(request.data.photos[1])

    request2 = request.next_page()

    print(request2.data.photos[1])
    
    $ {'id': 1323550, 'width': 4608, 'height': 2963...
    $ {'id': 167699, 'width': 6000, 'height': 4000...

Curated photos:

    from pexels_api.photos import PhotosClient

    request = (
        PhotosClient
        .create('curated', 'YourSecret')
        .request() # This is not optional
    )

    print(request.data.photos[1])

    request2 = request.next_page()

    print(request2.data.photos[1])
    
    $ {'id': 1323550, 'width': 4608, 'height': 2963...
    $ {'id': 167699, 'width': 6000, 'height': 4000...

Check Pexels API documentation to understand data structure.

https://www.pexels.com/api/documentation