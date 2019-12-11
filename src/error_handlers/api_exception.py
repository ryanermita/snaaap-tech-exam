class MissingRequiredFields(Exception):

    def __init__(self, error_data):
        self.error_data = error_data


class RequestParamException(Exception):
    def __init__(self, error_data):
        self.error_data = error_data


class ResourceNotFound(Exception):
    def __init__(self, error_data):
        self.error_data = error_data
