import logging
import re

from src.error_handlers import api_exception


def validate_required_fields(required_fields, data):
    """ Validate required fields from a dictionary.

    Parameters
    ----------
    required_fields: list
        the list of required fields.
    data: dict
        the data to be checked with required fields.

    Returns
    -------
    None

    Raises
    ------
    TypeError:
        for invalid parameter data type.
    MissingRequiredFields:
        for missing required fields from the data parameter.
    Exception:
        for any uncaught syntax error.
    """
    try:
        if not isinstance(required_fields, list):
            raise TypeError("required_fields should be a list data type.")

        if not isinstance(data, dict):
            raise TypeError("data should be a dict data type.")

        set_required_fields = set(required_fields)
        set_data = set(data)

        missing_required_fields = set_required_fields.difference(set_data)
        if missing_required_fields:
            error = {'missing_required_fields': list(missing_required_fields)}
            raise api_exception.MissingRequiredFields(error)

        return None
    except Exception as e:
        logging.error(e)
        raise e


def has_valid_str_length(data, minimum_length=1, maximum_length=255):
    """ Validate the string lenght is between minimun and maximum length.

    Parameters
    ----------
    data: str
        the strign data to be checked.
    minimum_length: int, optional
        the minimum length of the string.
        default to 1
    miximum_length: int, optional
        the maximum length of the string.
        default to 255

    Returns
    -------
    Boolean

    Raises
    ------
    TypeError:
        for invalid parameter data type.
    Exception:
        for any uncaught syntax error.
    """
    try:
        if not isinstance(data, str):
            raise TypeError("data parameter must be in str data type.")
        if not isinstance(minimum_length, int):
            raise TypeError("minimum_length parameter must be in int data type.")
        if not isinstance(maximum_length, int):
            raise TypeError("maximum_length parameter must be in int data type.")

        str_length = len(data)

        return minimum_length <= str_length <= maximum_length
    except Exception as e:
        logging.error(e)
        raise e


def is_valid_email(email):
    """ Validate the email format.

    Parameters
    ----------
    email: str
        the string data to be checked.

    Returns
    -------
    Boolean

    Raises
    ------
    Exception:
        for any uncaught syntax error.
    """
    try:
        email_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        return bool(re.match(email_pattern, email))
    except Exception as e:
        logging.error(e)
        raise e
