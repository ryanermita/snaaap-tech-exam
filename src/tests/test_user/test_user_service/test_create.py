from bson.objectid import ObjectId
from unittest.mock import patch
import unittest

from src.user import user_service
from src.user.user_entity import User
from src.helpers.flask_helper import ResponseHelper
from src.constants import http_status_code
from src.error_handlers.api_exception import MissingRequiredFields


class TestRetrieveMany(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch('src.user.user_entitymanager.create')
    @patch('src.user.user_service.user_prevalidation')
    @patch('src.utils.validator.validate_required_fields')
    def test_create_user(self,
                         mock_required_validate_required_fields,
                         mock_user_prevalidation,
                         mock_user_em_create):
        params = {'name': 'John', 'email': 'john@email.com',
                  'user_type': 'user'}
        user_obj = User(name='John', _id=ObjectId('5dedac6221696c18d065e9ff'),
                        email='john@email.com',
                        user_type='user',
                        description='sample description')
        mock_user_prevalidation.return_value = params
        mock_user_em_create.return_value = user_obj

        result = user_service.create(params)

        mock_required_validate_required_fields.assert_called_once()
        mock_user_prevalidation.assert_called_once_with(params)
        mock_user_em_create.assert_called_once_with(description=params.get('description'),
                                                    email=params['email'],
                                                    name=params['name'],
                                                    user_type=params['user_type'])
        self.assertTrue(isinstance(result, ResponseHelper))
        self.assertTrue(isinstance(result.data, dict))
        self.assertTrue('description' not in result.data)
        self.assertTrue('id' in result.data)
        self.assertTrue('name' in result.data)
        self.assertEqual(result.data['name'], params['name'])
        self.assertTrue('email' in result.data)
        self.assertEqual(result.data['email'], params['email'])
        self.assertTrue('user_type' in result.data)
        self.assertEqual(result.data['user_type'], params['user_type'])
        self.assertEqual(result.status_code, http_status_code.CREATED)

    @patch('src.user.user_entitymanager.create')
    @patch('src.user.user_service.user_prevalidation')
    @patch('src.utils.validator.validate_required_fields')
    def test_create_org(self,
                        mock_required_validate_required_fields,
                        mock_user_prevalidation,
                        mock_user_em_create):
        params = {'name': 'John', 'email': 'john@email.com',
                  'user_type': 'org', 'description': 'sample description'}
        user_obj = User(name='John', _id=ObjectId('5dedac6221696c18d065e9ff'),
                        email='john@email.com',
                        user_type='org',
                        description='sample description')
        mock_user_prevalidation.return_value = params
        mock_user_em_create.return_value = user_obj

        result = user_service.create(params)

        mock_required_validate_required_fields.assert_called_once()
        mock_user_prevalidation.assert_called_once_with(params)
        mock_user_em_create.assert_called_once_with(description=params.get('description'),
                                                    email=params['email'],
                                                    name=params['name'],
                                                    user_type=params['user_type'])
        self.assertTrue(isinstance(result, ResponseHelper))
        self.assertTrue(isinstance(result.data, dict))
        self.assertTrue('id' in result.data)
        self.assertTrue('name' in result.data)
        self.assertEqual(result.data['name'], params['name'])
        self.assertTrue('email' in result.data)
        self.assertEqual(result.data['email'], params['email'])
        self.assertTrue('user_type' in result.data)
        self.assertEqual(result.data['user_type'], params['user_type'])
        self.assertTrue('description' in result.data)
        self.assertEqual(result.data['description'], params['description'])
        self.assertEqual(result.status_code, http_status_code.CREATED)

    def test_missing_required_fields(self):
        params = {'name': 'John', 'email': 'john@email.com',
                  'user_type': 'org'}
        with self.assertRaises(MissingRequiredFields) as err_context:
            user_service.create(params)
        self.assertDictEqual(err_context.exception.error_data, 
                                  {'missing_required_fields': ['description']})
