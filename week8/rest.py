import werkzeug

werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask
from flask_restplus import Api, Resource
from connector import construct_con_str
from logic import crimes_between_dates, total_burglary
import configparser

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = construct_con_str()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)
ns = api.namespace("rest", description="Assignment Rest")


@ns.route("/<string:fromdate>=<string:todate>")
@api.response(404, "Nothing here but us lemmings")
class ResToFrom(Resource):
    def get(self, fromdate, todate):

        return crimes_between_dates(fromdate, todate)

    def post(self, fromdate, todate):
        # I don't see the point in making a post method here as per the assignment desc...
        return None, 201


@ns.route("/burglary")
@api.response(404, "Nothing here but us lemmings")
class ResBurglary(Resource):
    def get(self):
        return total_burglary()


def flask_run():
    conf = configparser.ConfigParser()
    conf.read("configuration.ini")

    if conf["DEFAULT"]["activeenvironment"] == "PRODUCTION":
        app.run(host="0.0.0.0")
    else:
        app.run(debug=True)
