import datetime


class User(object):
    def __init__(self, user_id, name, email):
        self.name = name
        self.email = email
        self.user_id = user_id
        self.created_at = datetime.datetime.utc()

    def get_user_info(self):
        return {
            "name": self.name,
            "email": self.email,
            "user_id": self.user_id,
        }
