from flask_restful import Resource, reqparse


class Users(Resource):
    def __init__(self, **kwargs):
        self.pg_helper = kwargs.get("pg_helper", {})

    def get(self):
        get_command = """Select * from users"""
        try:
            response = self.pg_helper.execute(get_command)
            return response, 200
        except Exception as e:
            print(e)
            return "error", 500

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, help="User Name", required=True)
        parser.add_argument("email", type=str, help="User Email", required=True)
        args = parser.parse_args()

        create_user_sql = """
            insert into users ("name" , "email")
            values ('{}', '{}')""".format(
            args.get("name", ""), args.get("email", "")
        )
        print(create_user_sql)
        response = self.pg_helper.execute(create_user_sql)
        return response

    def delete(self):
        pass

    def put(self):
        pass
