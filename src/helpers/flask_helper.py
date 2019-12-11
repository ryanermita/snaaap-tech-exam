import logging
import json

from flask import Response


class ResponseHelper:
    """
    A class helper used to represent a REST Response.

    Attributes
    ----------
    data : dict, list
        the response data (e.g query results or errors).
    status_code : int, optional
        the http status of the response (default is 200).
    success : boolean
        the indicator if the response is successful or not.

    Methods
    -------
    _format_response_data()
        format the response data using specific dictionary format.
    jsonify()
        Convert Reponse Object to flask.Response Object.
    """

    def __init__(self, data, status_code=200):
        """
        Parameters
        ----------
        data : dict, list
            the response data (e.g query results or errors).
        status_code : int, optional
            the http status of the response (default is 200).

        Raises
        ------
        TypeError:
            for invalid class parameters.
        Exception:
            for any uncatch syntax error.
        """

        try:
            if not isinstance(status_code, int):
                raise TypeError("Status code must be an integer.")

            self.data = data
            self.status_code = status_code

            # catch status code 4xx and 5xx.
            if str(status_code).startswith('4') or str(status_code).startswith('5'):
                self.success = False
            else:
                self.success = True

        except Exception as e:
            logging.error(e)
            raise

    def _format_response_data(self):
        """Format response data.

        Returns
        -------
        dict
            formatted response. example:
                {
                    "success": True,
                    "status_code": 200,
                    "results": {"first_name": "John"},
                    "errors": []
                }

        Raises
        ------
        Exception:
            for any uncatch syntax error.
        """

        try:
            return {
                "success": self.success,
                "results": self.data if self.success else [],
                "errors": self.data if not self.success else []
            }

        except Exception as e:
            logging.error(e)
            raise

    def jsonify(self):
        """Convert ResponseHelper object to flask.Response Object.

        Returns
        -------
        Response Object

        Raises
        ------
        Exception:
            for any uncatch syntax error.
        """

        try:
            return Response(json.dumps(self._format_response_data()), self.status_code, mimetype='application/json')
        except Exception as e:
            logging.error(e)
            raise
