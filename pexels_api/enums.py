from enum import Enum
from .settings import BASE_URL


class HeaderEnum(Enum):
    """ Default headers in Pexels response. """

    limit = 'X-Ratelimit-Limit'
    remaining = 'X-Ratelimit-Remaining'
    reset = 'X-Ratelimit-Reset'


class PhotoEndpointEnum(Enum):
    search = 'v1/search'
    curated = 'v1/curated'
    photos = 'v1/photos'

    def __str__(self) -> str:
        return self.name

    def url(self) -> str:
        """ Return URL """

        url = BASE_URL

        if not BASE_URL.endswith('/'):
            url = BASE_URL + '/'

        return f'{url}{self.value}'


class PhotoUrlParamsEnum(Enum):
    query = 'query'
    orientation = 'orientation'
    size = 'size'
    color = 'color'
    locale = 'locale'
    page = 'page'
    per_page = 'per_page'


class OrientationEnum(Enum):
    landscape = 'landscape'
    portrait = 'portrait'
    square = 'square'


class SizeEnum(Enum):
    large = 'large'
    medium = 'medium'
    small = 'small'


class ColorEnum(Enum):
    red = 'red'
    orange = 'orange'
    yellow = 'yellow'
    green = 'green'
    turquoise = 'turquoise'
    blue = 'blue'
    violet = 'violet'
    pink = 'pink'
    brown = 'brown'
    black = 'black'
    gray = 'gray'
    white = 'white'


class LocaleEnum(Enum):
    en = 'en-US'
    pt = 'pt-BR'
    es = 'es-ES'
    ca = 'ca-ES'
    de = 'de-DE'
    it = 'it-IT'
    fr = 'fr-FR'
    sv = 'sv-SE'
    id = 'id-ID'
    pl = 'pl-PL'
    ja = 'ja-JP'
    zh_t = 'zh-TW'
    zsh_c = 'zh-CN'
    ko = 'ko-KR'
    th = 'th-TH'
    nl = 'nl-NL'
    hu = 'hu-HU'
    vi = 'vi-VN'
    cs = 'cs-CZ'
    da = 'da-DK'
    fi = 'fi-FI'
    uk = 'uk-UA'
    el = 'el-GR'
    ro = 'ro-RO'
    nb = 'nb-NO'
    sk = 'sk-SK'
    tr = 'tr-TR'
    ru = 'ru-RU'
