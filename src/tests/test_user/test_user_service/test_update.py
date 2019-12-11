from bson.objectid import ObjectId
from unittest.mock import patch, Mock
import unittest

from src.user import user_service
from src.user.user_entity import User
from src.helpers.flask_helper import ResponseHelper
from src.constants import http_status_code
from src.error_handlers.api_exception import ResourceNotFound
from src.error_handlers.error_reference import GenericError


class TestUpdate(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    @patch('src.user.user_entitymanager.update')
    @patch('src.user.user_service._get_user')
    @patch('src.user.user_service.user_prevalidation')
    @patch('src.utils.validator.validate_required_fields')
    def test_update_user(self,
                         mock_required_validate_required_fields,
                         mock_user_prevalidation,
                         mock_get_user,
                         mock_user_em_update):
        params = {'id': '5dedac6221696c18d065e9ff', 'email': 'john@email.com'}
        user_obj = User(name='John', _id=ObjectId('5dedac6221696c18d065e9ff'),
                        email='john@email.com',
                        user_type='user',
                        description='sample description')
        mock_user_prevalidation.return_value = params
        mock_user_em_update.return_value = 1
        mock_get_user.side_effect = [user_obj, user_obj]

        result = user_service.update(params)

        mock_required_validate_required_fields.assert_called_once()
        mock_user_prevalidation.assert_called_once_with(params)
        mock_user_em_update.assert_called_once_with(params['id'], {'email': 'john@email.com'})
        self.assertTrue(isinstance(result, ResponseHelper))
        self.assertTrue(isinstance(result.data, dict))
        self.assertEqual(result.status_code, http_status_code.OK)

    @patch('src.user.user_entitymanager.update')
    @patch('src.user.user_service._get_user')
    @patch('src.user.user_service.user_prevalidation')
    @patch('src.utils.validator.validate_required_fields')
    def test_update_user_record_not_found(self,
                                          mock_required_validate_required_fields,
                                          mock_user_prevalidation,
                                          mock_get_user,
                                          mock_user_em_update):
        params = {'id': '5dedac6221696c18d065e9ff', 'email': 'john@email.com'}
        mock_user_prevalidation.return_value = params
        mock_get_user.side_effect = ResourceNotFound(GenericError.NOT_FOUND('user')), None

        with self.assertRaises(ResourceNotFound) as err_context:
            user_service._get_user({'id': '5dedac6221696c18d065e9ff'})
        self.assertDictEqual(err_context.exception.error_data,
                             GenericError.NOT_FOUND('user'))
