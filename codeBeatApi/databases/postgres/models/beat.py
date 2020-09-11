import datetime


class Beat(object):
    def __init__(self, beat_id, user_id, data):
        self.beat_id = beat_id
        self.user_id = user_id
        self.data = data
        self.published_date = datetime.datetime.utc()

    def get_user_info(self):
        return {
            "data": self.data,
            "beat_id": self.beat_id,
            "user_id": self.user_id,
            "published_date": self.published_date,
        }
