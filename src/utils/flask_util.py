import logging


def get_request_data(request):
    """ Retrieve request data from the request object.

    Parameters
    ----------
    request: object
        the request object instance

    Returns
    -------
    Dictionary
        the request data from the request object.

    Raises
    ------
    Exception:
        for any uncaught syntax error.
    """
    try:
        data = request.get_json()
        if not data:
            data = request.values.to_dict()

        return data
    except Exception as e:
        logging.error(f"""Error ocurred while retrieving \
                      flask request data: {e}""")
        raise e
