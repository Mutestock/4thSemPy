import werkzeug

werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask, jsonify
from flask_restplus import Api, Resource
from logic import ex02
from connector import construct_con_str
from decorators import Decorators
import configparser

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = construct_con_str()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)
ns = api.namespace("rest", description="Assignment Rest")


@ns.route("/<string:index>")
@api.response(404, "Nothing here but us lemmings")
class ResToFrom(Resource):
    def get(self,index):
        return jsonify(ex02(index))

        
@Decorators.determine_environment
def flask_run():
    conf = configparser.ConfigParser()
    conf.read("configuration.ini")

    if conf["DEFAULT"]["activeenvironment"] == "PRODUCTION":
        app.run(host="0.0.0.0")
    else:
        app.run(debug=True)
