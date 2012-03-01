"""
Factual table api query
"""

from base import Base

DEFAULT_LIMIT = 20

class Table(Base):
    def __init__(self, api, path, params={}):
        self.path = path
        self.action = 'read'
        Base.__init__(self, api, params)

    def search(self, terms):
        return self.create({'q': terms})

    def filters(self, filters):
        return self.create({'filters': filters})

    def include_count(self, include):
        return self.create({'include_count': include})

    def geo(self, geo_filter):
        return self.create({'geo': geo_filter})

    def limit(self, max_rows):
        return self.create({'limit': max_rows})

    def select(self, fields):
        return self.create({'select': fields})

    def sort(self, sort_params):
        return self.create({'sort': sort_params})

    def offset(self, offset):
        return self.create({'offset': offset})

    def page(self, page_num, limit=DEFAULT_LIMIT):
        limit = DEFAULT_LIMIT if limit < 1 else limit
        page_num = 1 if page_num < 1 else page_num
        return self.offset((page_num - 1) * limit).limit(limit)

    def sort_asc(self, fields):
        return self.sort(",".join([f + ":asc" for f in fields]))

    def sort_desc(self, fields):
        return self.sort(",".join([f + ":desc" for f in fields]))

    def create(self, params):
        return Table(self.api, self.path, self.merge_params(params))
