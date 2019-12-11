import unittest

from src.utils import common_util


class TestDataCleanup(unittest.TestCase):
    def setUp(self):
        self.data_for_cleanup = {'first_name': '    john',
                                 'last_name': 'doe    ',
                                 'email': '  johndoe@email.com    ',
                                 'list_data': [],
                                 'tuple_data': (),
                                 'dict_data': {},
                                 'int_data': 1,
                                 'float_data': 1.0}
        self.cleaned_data = {'first_name': 'john',
                             'last_name': 'doe',
                             'email': 'johndoe@email.com',
                             'list_data': [],
                             'tuple_data': (),
                             'dict_data': {},
                             'int_data': 1,
                             'float_data': 1.0}

    def tearDown(self):
        pass

    def test_data_cleanup(self):
        cleaned_data = common_util.data_cleanup(self.data_for_cleanup)

        for key, item in cleaned_data.items():
            with self.subTest(key=key, item=item):
                self.assertEqual(cleaned_data[key], self.cleaned_data[key])
