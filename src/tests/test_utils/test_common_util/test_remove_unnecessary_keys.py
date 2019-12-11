import unittest

from src.utils import common_util


class TestRemoveUnnecessaryKeys(unittest.TestCase):
    def setUp(self):
        self.data = {'name': 'John', 'age': 19}
        self.valid_keys = ['name']
        self.cleaned_data = {'name': 'John'}
        pass

    def tearDown(self):
        pass

    def test_remove_unnecessary_keys(self):
        result = common_util.remove_unnecessary_keys(self.valid_keys,
                                                     self.data)
        self.assertDictEqual(result, self.cleaned_data)

    def test_remove_unnecessary_keys_invalid_valid_key_params(self):
        with self.assertRaises(TypeError) as err_context:
            common_util.remove_unnecessary_keys('test', self.data)
        self.assertEqual(str(err_context.exception),
                         "valid_keys parameter must a list data type.")

    def test_remove_unnecessary_keys_invalid_data_params(self):
        with self.assertRaises(TypeError) as err_context:
            common_util.remove_unnecessary_keys(self.valid_keys, 'test')
        self.assertEqual(str(err_context.exception), 
                         "data parameter must a dict data type.")
