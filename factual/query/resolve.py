from base import Base

class Resolve(Base):
    def __init__(self, api, params={}):
        self.path = 'places/resolve'
        self.action = 'resolve'
        Base.__init__(self, api, params)

    def values(self, values):
        return self.create({'values': values})

    def include_count(self, include):
        return self.create({'include_count': include})

    def create(self, params):
        return Resolve(self.api, self.path, self.merge_params(params))
