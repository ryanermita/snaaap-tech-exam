import logging
from bson.objectid import ObjectId

from .user_entity import User


def create(name, email, user_type, description=None):
    try:
        data = {'name': name,
                'email': email,
                'user_type': user_type,
                'description': description}
        return User.objects.create(**data)
    except Exception as e:
        logging.error(f"An error occured while creating User record: {e}")
        raise e


def retrieve_one(filters):
    try:
        if 'id' in filters:
            filters['_id'] = ObjectId(filters.pop('id'))
        return User.objects.get(filters)
    except User.DoesNotExist as e:
        logging.error(e)
        return None
    except Exception as e:
        logging.error(e)
        raise e


def retrieve_many(data):
    try:
        if 'id' in data:
            data['_id'] = ObjectId(data.pop('id'))

        return User.objects.raw(data)
    except Exception as e:
        logging.error(f"""An error occured while \
                      retrieving all User record: {e}""")
        raise e


def update(id, data):
    try:
        db_id_filter = {'_id': ObjectId(id)}
        return User.objects.raw(db_id_filter).update({"$set": data})
    except Exception as e:
        logging.error(f"An error occured while creating User record: {e}")
        raise e


def delete(id):
    try:
        db_id_filter = {'_id': ObjectId(id)}
        return User.objects.raw(db_id_filter).delete()
    except Exception as e:
        logging.error(f"An error occured while creating User record: {e}")
        raise e
