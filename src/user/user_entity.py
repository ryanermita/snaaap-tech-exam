import logging

from pymodm import MongoModel, fields


class User(MongoModel):
    name = fields.CharField()
    email = fields.EmailField()
    user_type = fields.CharField()
    description = fields.CharField(blank=True)

    class Meta:
        final = True

    def __repr__(self):
        try:
            self.to_dict(include_db_id=True)
        except Exception as e:
            logging.error(f"""Unexpected error occured while \
                          building object representation: {e}""")
            raise e

    def to_dict(self):
        try:
            data = {'id': str(self._id),
                    'name': self.name,
                    'email': self.email,
                    'user_type': self.user_type}
            if self.is_organization():
                data.update({'description': self.description})

            return data
        except Exception as e:
            logging.error(f"""Unexpected error occured while \
                          converting object to json: {e}""")
            raise

    def is_organization(self):
        return True if self.user_type == 'org' else False
