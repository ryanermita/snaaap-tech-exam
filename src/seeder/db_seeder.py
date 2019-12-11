import logging

from src.user.user_entity import User
from src.initializer import _initialize_db

try:
    _initialize_db()
    users = [
        User(name='John Doe', email='johndoe@email.com', user_type=1),
        User(name='Doe Organization', email='doe@organization.com',
             user_type=2, description="sample doe organization description"),
    ]
    User.objects.bulk_create(users)
    logging.info("Successfully seeded user data.")
except Exception as e:
    logging.exception(f"""something went wrong while \
                      creating user seed data: {e}""")
    raise e
