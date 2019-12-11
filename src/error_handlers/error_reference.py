from src.constants.misc import GenericConstants, UserConstants


class GenericError:

    @staticmethod
    def NOT_FOUND(resource):
        return {
            'error': f"Resource not found: {resource}"
        }

    @staticmethod
    def INVALID_STRING_LENGTH(data):
        return {
            'error': f"""Value length must be between \
                  {GenericConstants.MINIMUM_STRING_LENGTH} and \
                  {GenericConstants.MAXIMUM_STRING_LENGTH}""",
            'parameter': data
        }

    INVALID_ID_LENGTH = {
            'error': f"id length must be {GenericConstants.ID_LENGTH}",
            'parameter': 'id'
    }


class UserError:

    INVALID_USER_TYPE = {
        'error': f"valid user types are: {','.join(UserConstants.USER_TYPES)}",
        'parameter': 'user_type'
    }

    INVALID_EMAIL = {
        'error': "Invalid email format",
        'parameter': 'email'
    }
