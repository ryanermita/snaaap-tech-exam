import unittest

from src.utils import validator


class TestHasValidStrLength(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_has_valid_str_length(self):
        result = validator.has_valid_str_length('test')
        self.assertTrue(result)

    def test_has_valid_str_length_with_minimum_length(self):
        result = validator.has_valid_str_length('test', minimum_length=5)
        self.assertTrue(result is False)

    def test_has_valid_str_length_with_maximum_length(self):
        result = validator.has_valid_str_length('test', maximum_length=3 )
        self.assertTrue(result is False)

    def test_has_valid_str_length_invalid_data_parameter(self):
        with self.assertRaises(TypeError) as err_context:
            validator.has_valid_str_length([])
        self.assertEqual(str(err_context.exception),
                         'data parameter must be in str data type.')

    def test_has_valid_str_length_invalid_minimum_length_parameter(self):
        with self.assertRaises(TypeError) as err_context:
            validator.has_valid_str_length('test', minimum_length=[])
        self.assertEqual(str(err_context.exception),
                         'minimum_length parameter must be in int data type.')

    def test_has_valid_str_length_invalid_maximum_length_parameter(self):
        with self.assertRaises(TypeError) as err_context:
            validator.has_valid_str_length('test', maximum_length=[])
        self.assertEqual(str(err_context.exception),
                         'maximum_length parameter must be in int data type.')
