import unittest
from request_manager.handler import array_q_to_dict, parse


class MyTestCase(unittest.TestCase):
    def test_parse_parses_whole_all_query_params(self):
        query = {'filter[month]': ['12'], 'filter[day]': ['3'], 'page[offset]': ['3'], 'page[limit]': ['30']}
        actual = parse(query)
        expected = {'filter': {'month': 12, 'day': 3}, 'page': {'offset': 3, 'limit': 30}}
        self.assertEqual(expected, actual)

    def test_array_q_to_dict_converts_array_q_params_to_multi_levl_dict(self):
        compound_key = ('filter[month]')
        val = ['12']
        actual = array_q_to_dict(compound_key, val, {})
        expected = {'filter': {'month': 12}}
        self.assertEqual(expected, actual)

    def test_array_q_to_dict_converts_array_q_params_to_multi_levl_dict_when_key_already_exists(self):
        compound_key = ('filter[day]')
        val = ['25']
        actual = array_q_to_dict(compound_key, val, {'filter': {'month': 12}})
        expected = {'filter': {'month': 12, 'day': 25}}
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
