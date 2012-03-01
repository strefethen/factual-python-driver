from base import Base

class Crosswalk(Base):
    def __init__(self, api, params={}):
        self.path = 'places/crosswalk'
        self.action = 'crosswalk'
        Base.__init__(self, api, params)

    def factual_id(self, factual_id):
        return self.create({'factual_id': factual_id})

    def limit(self, max_rows):
        return self.create({'limit': max_rows})

    def only(self, namespaces):
        return self.create({'only': namespaces})

    def include_count(self, include):
        return self.create({'include_count': include})

    def namespace(self, namespace, namespace_id):
        return self.create({'namespace': namespace, 'namespace_id': namespace_id})

    def create(self, params):
        return Crosswalk(self.api, self.merge_params(params))
