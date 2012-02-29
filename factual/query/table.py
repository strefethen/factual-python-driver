"""
Factual table api query
"""

from base import Base

class Table(Base):
    def __init__(self, api, path, params={}):
        self.path = path
        self.action = 'read'
        Base.__init__(self, api, params)

    def search(self, args):
        return self.create({'q': args})

    def filters(self, args):
        return self.create({'filters': args})

    def include_count(self, include):
        return self.create({'include_count': include})

    def geo(self, args):
        return self.create({'geo': args})

    def limit(self, max_rows):
        return self.create({'limit': max_rows})

    def select(self, args):
        return self.create({'select': args})

    # TODO refactor for easier asc/desc (per field, too?)
    def sort(self, args):
        return self.create({'sort': args})

    def create(self, params):
        return Table(self.api, self.path, self.merge_params(params))
