import unittest

from factual import Factual
from factual.utils import circle
from test_settings import KEY, SECRET

class FactualAPITestSuite(unittest.TestCase):
    def setUp(self):
        self.factual = Factual(KEY, SECRET)
        self.places = self.factual.table('places')

    def test_search(self):
        q = self.places.search('factual')
        row = q.rows()[0]
        self.assertRegexpMatches(row['name'], 'Factual')

    def test_limit(self):
        q = self.places.search('sushi').limit(3)
        self.assertEqual(3, len(q.rows()))

    def test_select(self):
        q = self.places.select('name,address')
        row = q.rows()[0]
        self.assertEqual(2, len(row.keys()))

    def test_sort(self):
        q1 = self.places.sort_asc(['name'])
        self.assertTrue(q1.rows()[0]['name'] < q1.rows()[1]['name'])

        q2 = self.places.sort_desc(['name'])
        self.assertTrue(q2.rows()[0]['name'] > q2.rows()[1]['name'])

    def test_paging(self):
        q1 = self.places.offset(30)
        r1 = q1.rows()[0]

        q2 = self.places.page(3, 15)
        r2 = q2.rows()[0]
        self.assertEqual(r1['name'], r2['name'])

    def test_filters(self):
        q = self.places.filters({'region': 'NV'})
        for r in q.rows():
            self.assertEqual('NV', r['region'])

    def test_geo(self):
        q = self.places.search('factual').geo(circle(34.06021, -118.41828, 1000))
        row = q.rows()[0]
        self.assertEqual('Factual', row['name'])
        self.assertEqual('1801 Avenue Of The Stars', row['address'])

    def test_resolve(self):
        q = self.factual.resolve({'name': 'factual inc', 'locality': 'los angeles'})
        row = q.rows()[0]
        self.assertTrue(row['resolved'])
        self.assertEqual('1801 Avenue Of The Stars', row['address'])

    def test_schema(self):
        schema = self.places.schema()
        self.assertEqual(21, len(schema['fields']))
        self.assertTrue('title' in schema)
        self.assertTrue('locality' in set(f['name'] for f in schema['fields']))


if __name__ == '__main__':
    unittest.main()
