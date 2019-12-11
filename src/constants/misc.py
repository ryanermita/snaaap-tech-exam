class GenericConstants:
    MINIMUM_STRING_LENGTH = 1
    MAXIMUM_STRING_LENGTH = 255
    ID_LENGTH = 24
    TRUTHY_VALUES = ('t', 'true', 'True', 1, 1.0)
    FALSY_VALUES = ('f', 'false', 'False', 0, 0.0)


class UserConstants:
    USER_TYPE_USER = 'user'
    USER_TYPE_ORG = 'org'
    USER_TYPES = (USER_TYPE_USER, USER_TYPE_ORG)
