"""
Base query class
"""

class Base(object):
    def __init__(self, api, params):
        self.api = api
        self.params = params
        self.response = None

    def rows(self):
        return self.get_response()['data']

    def total_rows(self):
        return self.get_response()['total_row_count']

    def get_response(self):
        if not self.response:
            self.response = self.api.execute(self)
        return self.response

    def merge_params(self, params):
        new_params = self.params.copy()
        new_params.update(params)
        return new_params
