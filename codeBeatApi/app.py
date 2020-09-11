from flask import Flask
from flask_restful import Api
from codeBeatApi.resources.users import Users
from codeBeatApi.databases.postgres.helper import PGHelper

app = Flask(__name__)
api = Api(app)

api.add_resource(Users, "/users", resource_class_kwargs={"pg_helper": PGHelper()})


if __name__ == "__main__":
    app.run(debug=True)
