from bson.objectid import ObjectId
from unittest.mock import patch
import unittest

from src.user import user_service
from src.user.user_entity import User
from src.error_handlers.api_exception import ResourceNotFound
from src.error_handlers.error_reference import GenericError
from src.helpers.flask_helper import ResponseHelper
from src.constants import http_status_code


class TestGetUser(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch('src.user.user_entitymanager.delete')
    @patch('src.user.user_service._get_user')
    @patch('src.user.user_service.user_prevalidation')
    @patch('src.utils.validator.validate_required_fields')
    def test_delete_user(self, 
                         mock_required_validate_required_fields,
                         mock_user_prevalidation,
                         mock_get_user,
                         mock_user_em_delete):
        params = {'id': '5dedac6221696c18d065e9ff'}
        user_obj = User(name='John', _id=ObjectId('5dedac6221696c18d065e9ff'),
                        email='john@email.com',
                        user_type='org',
                        description='sample description')
        mock_user_prevalidation.return_value = params
        mock_get_user.return_value = user_obj.to_dict()

        result = user_service.delete(params)

        self.assertTrue(isinstance(result, ResponseHelper))
        self.assertTrue(result.data is None)
        self.assertEqual(result.status_code, http_status_code.DELETED)

    @patch('src.user.user_entitymanager.delete')
    @patch('src.user.user_service._get_user')
    @patch('src.user.user_service.user_prevalidation')
    @patch('src.utils.validator.validate_required_fields')
    def test_delete_user_not_found(self, 
                         mock_required_validate_required_fields,
                         mock_user_prevalidation,
                         mock_get_user,
                         mock_user_em_delete):
        params = {'id': '5dedac6221696c18d065e9ff'}
        mock_user_prevalidation.return_value = params
        mock_get_user.side_effect = ResourceNotFound(GenericError.NOT_FOUND('user')), None

        with self.assertRaises(ResourceNotFound) as err_context:
            user_service.delete(params)
        self.assertDictEqual(err_context.exception.error_data,
                             GenericError.NOT_FOUND('user'))