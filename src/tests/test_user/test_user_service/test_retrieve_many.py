from bson.objectid import ObjectId
from unittest.mock import patch
import unittest

from src.user import user_service
from src.user.user_entity import User
from src.helpers.flask_helper import ResponseHelper
from src.constants import http_status_code


class TestRetrieveMany(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch('src.user.user_entitymanager.retrieve_many')
    @patch('src.user.user_service.user_prevalidation')
    def test_retrieve_many(self,
                           mock_user_prevalidation,
                           mock_user_em_retrieve_many):
        params = {'id': '5dedac6221696c18d065e9ff'}
        user_objs = [User(name='John', _id=ObjectId('5dedac6221696c18d065e9ff'),
                          email='john@email.com',
                          description='sample description')]
        mock_user_prevalidation.return_value = params
        mock_user_em_retrieve_many.return_value = user_objs

        result = user_service.retrieve_many(params)

        mock_user_prevalidation.assert_called_once_with(params)
        mock_user_em_retrieve_many.assert_called_once_with(params)
        self.assertTrue(isinstance(result, ResponseHelper))
        self.assertCountEqual(result.data, [user_objs[0].to_dict()])
        self.assertEqual(result.status_code, http_status_code.OK)
