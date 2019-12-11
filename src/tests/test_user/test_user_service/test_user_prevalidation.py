import unittest
import copy

from src.user import user_service
from src.error_handlers.api_exception import RequestParamException
from src.error_handlers.error_reference import GenericError, UserError


class TestUserPreValidation(unittest.TestCase):
    def setUp(self):
        self.params = {'name': 'John', 'email': 'john@email.com.ph',
                       'user_type': 'org', 'description': 'some description',
                       'id': '5dedac6221696c18d065e9ff'}

    def tearDown(self):
        pass

    def test_user_prevalidation(self):
        result = user_service.user_prevalidation(self.params)
        self.assertDictEqual(result, self.params)

    def test_str_valid_length(self):
        params_copy = copy.copy(self.params)
        for_str_validation = ['name', 'email', 
                              'user_type', 'description']
        for item in for_str_validation:
            with self.subTest(item=item):
                params_copy[item] = 'x' * 300
                with self.assertRaises(RequestParamException) as err_context:
                    user_service.user_prevalidation(params_copy)
                error_message = GenericError.INVALID_STRING_LENGTH(item)
                self.assertDictEqual(err_context.exception.error_data,
                                     error_message)
                params_copy[item] = self.params[item]

    def test_id_valid_length(self):
        invalid_ids = ['x' * 23, 'x' * 25]

        for invalid_id in invalid_ids:
            with self.subTest(invalid_id=invalid_id):
                self.params['id'] = invalid_id
                with self.assertRaises(RequestParamException) as err_context:
                    user_service.user_prevalidation(self.params)
                self.assertDictEqual(err_context.exception.error_data,
                                     GenericError.INVALID_ID_LENGTH)

    def test_invalid_user_type(self):
        self.params['user_type'] = 'admin'

        with self.assertRaises(RequestParamException) as err_context:
            user_service.user_prevalidation(self.params)
        self.assertDictEqual(err_context.exception.error_data,
                             UserError.INVALID_USER_TYPE)

    def test_invalid_email(self):
        self.params['email'] = 'doe@john@.com'

        with self.assertRaises(RequestParamException) as err_context:
            user_service.user_prevalidation(self.params)
        self.assertDictEqual(err_context.exception.error_data,
                             UserError.INVALID_EMAIL)
