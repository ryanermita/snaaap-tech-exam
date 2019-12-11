from bson.objectid import ObjectId
from unittest.mock import patch
import unittest

from src.user import user_service
from src.user.user_entity import User
from src.error_handlers.api_exception import ResourceNotFound
from src.error_handlers.error_reference import GenericError


class TestGetUser(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch('src.user.user_entitymanager.retrieve_one')
    def test_get_user(self, mock_user_em_retrieve_one):
        user_obj = User(name='John', _id=ObjectId('5dedac6221696c18d065e9ff'),
                        email='john@email.com',
                        user_type='org',
                        description='sample description')
        mock_user_em_retrieve_one.return_value = user_obj
        user = user_service._get_user({'id': '5dedac6221696c18d065e9ff'})

        self.assertDictEqual(user, user_obj.to_dict())

    @patch('src.user.user_entitymanager.retrieve_one')
    def test_user_not_found(self, mock_user_em_retrieve_one):
        mock_user_em_retrieve_one.return_value = None

        with self.assertRaises(ResourceNotFound) as err_context:
            user_service._get_user({'id': '5dedac6221696c18d065e9ff'})
        self.assertDictEqual(err_context.exception.error_data,
                             GenericError.NOT_FOUND('user'))
