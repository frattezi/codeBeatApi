import psycopg2


class PGHelper(object):
    def __init__(self):
        if not hasattr(self, "conn"):
            self.conn = self._connect_to_database()
        if not hasattr(self, "cur"):
            self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def execute(self, command):
        """
        Execute an SQL command using an open connection.
        """
        try:
            self.cur.execute(command)
            self.conn.commit()
            result = self.cur.fetchall()
            print("Successfully executed command")
            return result
        except Exception as e:
            print(e)

    def _connect_to_database(self):
        try:
            print("Connecting to database")
            conn = psycopg2.connect(
                database="beats",
                user="postgres",
                password="password",
                host="localhost",
                port="5432",
            )
            print("connection Succeeded")
            return conn
        except Exception as e:
            print("Failed to connect, error: {}".format(e))
            return
