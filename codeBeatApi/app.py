from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from codeBeatApi.resources.beat import Beat
from codeBeatApi.resources.User import User


app = Flask(__name__)
api = Api(app)


api.add_resource(User, "/user")
api.add_resource(Beat, "/beat")


if __name__ == "__main__":
    app.run(debug=True)
