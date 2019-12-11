import unittest

from src.utils import validator
from src.error_handlers import api_exception


class TestValidateRequiredFields(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_validate_required_fields_with_correct_data(self):
        data = {'name': 'John'}
        required_fields = ['name']
        result = validator.validate_required_fields(required_fields, data)
        self.assertTrue(result is None)

    def test_validate_required_fields_with_invalid_required_fields_params(self):
        with self.assertRaises(TypeError) as err_context:
            validator.validate_required_fields('test', {})
        self.assertEqual(str(err_context.exception),
                         "required_fields should be a list data type.")

    def test_validate_required_fields_with_invalid_data_params(self):
        with self.assertRaises(TypeError) as err_context:
            validator.validate_required_fields([], 'test')
        self.assertEqual(str(err_context.exception),
                         "data should be a dict data type.")

    def test_validate_required_fields_that_raise_missing_required_fields_exception(self):
        data = {'name': 'John'}
        required_fields = ['age']
        with self.assertRaises(api_exception.MissingRequiredFields) as err_context:
            validator.validate_required_fields(required_fields, data)
        self.assertDictEqual(err_context.exception.error_data,
                             {'missing_required_fields': ['age']})
   