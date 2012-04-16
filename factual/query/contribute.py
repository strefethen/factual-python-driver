from write import Write

class Contribute(Write):
    def __init__(self, api, table, factual_id, params={}):
        Write.__init__(self, api, table, factual_id, params)

    def values(self, values):
        return self._copy({'values': values})

    def user(self, user):
        return self._copy({'user': user})

    def comment(self, comment):
        return self._copy({'comment': comment})

    def reference(self, reference):
        return self._copy({'reference': reference})

    def _path(self):
        path = 't/' + self.table
        if self.factual_id:
            path += '/' + self.factual_id
        path += '/contribute'
        return path

    def _copy(self, params):
        return Contribute(self.api, self.table, self.factual_id, self.merge_params(params))
