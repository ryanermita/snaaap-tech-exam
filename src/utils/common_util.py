import logging

from src.constants.misc import GenericConstants


def data_cleanup(data):
    """ Clean data inside the data parameter.

    Parameters
    ----------
    data : dict
        the data to be cleaned.

    Returns
    -------
    Dictionary
        the cleaned data

    Raises
    ------
    Exception:
        for any uncaught syntax error.

    TODO:
        - this function currently works on dictionary,
          modify to clean data in other data types.
    """
    try:
        cleansed_data = dict()
        for key, item in data.items():
            if isinstance(item, str):
                item = item.strip()
            cleansed_data[key] = item

        return cleansed_data
    except Exception as e:
        logging.error(f"Something went wrong while cleaning up data: {e}")
        raise e


def remove_unnecessary_keys(valid_keys, data):
    """ Remove unnecessary keys inside a dictionary.

    Parameters
    ----------
    valid_keys: list
        the list of valid keys inside the dictionary.
    data : dict
        the data to be checked using valid_keys

    Returns
    -------
    Dictionary
        modified data dictionary without the unnecessary keys.

    Raises
    ------
    TypeError:
        for invalid parameter data types.
    Exception:
        for any uncaught syntax error.
    """
    try:
        if not isinstance(valid_keys, list):
            raise TypeError("valid_keys parameter must a list data type.")
        if not isinstance(data, dict):
            raise TypeError("data parameter must a dict data type.")
        if not valid_keys:
            return data

        valid_keys_set = set(valid_keys)
        data_keys_set = set(data.keys())
        unnecessary_keys = data_keys_set.difference(valid_keys_set)

        for unnecessary_key in unnecessary_keys:
            del data[unnecessary_key]

        return data
    except Exception as e:
        logging.error(e)
        raise e


def to_bool(data):
    """ Convert data value to boolean data.

    Parameters
    ----------
    data: str, list, float
        the data to be coverted to boolean.

    Returns
    -------
    Boolean
        the converted boolean data.

    Raises
    ------
    ValueError:
        for data value that is not in the truthy and falsy values.
    Exception:
        for any uncaught syntax error.
    """
    try:
        if data in set(GenericConstants.TRUTHY_VALUES):
            return True
        elif data in set(GenericConstants.FALSY_VALUES):
            return False

        raise ValueError(f'Invalid data for boolean convertion: {data}')
    except Exception as e:
        logging.error(e)
        raise e
