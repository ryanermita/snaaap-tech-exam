import logging

from src.user import user_entitymanager
from src.utils import validator, common_util
from src.helpers import flask_helper
from src.constants import http_status_code, misc
from src.error_handlers import api_exception
from src.error_handlers.error_reference import GenericError, UserError


def create(data):
    try:
        required_fields = ['name', 'email', 'user_type']
        if data.get('user_type') == misc.UserConstants.USER_TYPE_ORG:
            required_fields.append('description')
        validator.validate_required_fields(required_fields, data)

        cleaned_data = user_prevalidation(data)
        user = user_entitymanager.create(name=cleaned_data['name'],
                                         email=cleaned_data['email'],
                                         user_type=cleaned_data['user_type'],
                                         description=cleaned_data.get('description'))

        return flask_helper.ResponseHelper(user.to_dict(), http_status_code.CREATED)
    except Exception as e:
        logging.error(e)
        raise


def retrieve_many(data):
    try:
        cleaned_data = user_prevalidation(data)
        users = user_entitymanager.retrieve_many(cleaned_data)
        results = [user.to_dict() for user in users]
        return flask_helper.ResponseHelper(results, http_status_code.OK)
    except Exception as e:
        logging.error(f"Error occured: {e}")
        raise e


def update(data):
    """
    TODO:
        find a way to call collection.findOneAndUpdate(), currently pymodm .update()
        only returns the number of updated record.
    """
    try:
        required_fields = ['id']
        validator.validate_required_fields(required_fields, data)

        cleaned_data = user_prevalidation(data)
        updated_data = {key: val for key, val in cleaned_data.items()
                        if val is not None}
        db_id = updated_data.pop('id')
        _get_user({'id': db_id})  # call to validate if user exist
        user_entitymanager.update(db_id, updated_data)
        user = _get_user({'id': db_id})  # call to get the updated data.
        return flask_helper.ResponseHelper(user.to_dict(), http_status_code.OK)
    except Exception as e:
        logging.error(e)
        raise


def delete(data):
    try:
        required_fields = ['id']
        validator.validate_required_fields(required_fields, data)
        cleaned_data = user_prevalidation(data)

        # call to validate if user exist
        # this will raise ResourceNotFound if record does
        # not exist.
        user = _get_user(cleaned_data)
        user_entitymanager.delete(user['id'])
        return flask_helper.ResponseHelper(None, http_status_code.DELETED)
    except Exception as e:
        logging.error(e)
        raise e


def _get_user(filters):
    try:
        user = user_entitymanager.retrieve_one(filters)
        if user is None:
            raise api_exception.ResourceNotFound(GenericError.NOT_FOUND('user'))
        return user.to_dict()
    except Exception as e:
        logging.error(e)
        raise e


def user_prevalidation(data):
    """ Basic validation for user data.

    Parameters
    ----------
    data: dict
        the user data stored in a dictionary.

    Returns
    -------
    Dictionary
        validated user data stored in a dictionary.

    Raises
    ------
    RequestParamException:
        for invalid request parameters.
    Exception:
        for any uncaught syntax error.
    """
    try:
        valid_keys = ['name', 'email', 'user_type', 'description', 'id']
        data = common_util.remove_unnecessary_keys(valid_keys, data)
        cleaned_data = common_util.data_cleanup(data)

        for_str_validation = ['name', 'email', 'user_type', 'description']
        for item in for_str_validation:
            if item in cleaned_data and not validator.has_valid_str_length(cleaned_data[item]):
                raise api_exception.RequestParamException(GenericError.INVALID_STRING_LENGTH(item))

        if 'id' in cleaned_data:
            if not validator.has_valid_str_length(cleaned_data['id'],
                                                  minimum_length=misc.GenericConstants.ID_LENGTH,
                                                  maximum_length=misc.GenericConstants.ID_LENGTH):
                raise api_exception.RequestParamException(GenericError.INVALID_ID_LENGTH)

        if 'user_type' in cleaned_data:
            if cleaned_data['user_type'] not in set(misc.UserConstants.USER_TYPES):
                raise api_exception.RequestParamException(UserError.INVALID_USER_TYPE)

        if 'email' in cleaned_data:
            if not validator.is_valid_email(cleaned_data['email']):
                raise api_exception.RequestParamException(UserError.INVALID_EMAIL)

        return cleaned_data
    except Exception as e:
        logging.error(e)
        raise e
