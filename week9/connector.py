import pymysql
import configparser
import getpass
from decorators import Decorators
from sqlalchemy import create_engine


@Decorators.determine_environment
def DB_connection():
    active_environment = get_active_environment()
    conf = configparser.ConfigParser()
    conf.read("sensitive.ini")

    # This is for remote access. It's not required in this assignment, but I'm keeping it for future reference
    # if active_environment == "PRODUCTION":
    #    production_ssh_setup(active_environment, conf)

    cnx = pymysql.connect(
        user=conf[active_environment]["SQLUsername"],
        password=conf[active_environment]["SQLPassword"],
        host=conf[active_environment]["SQLHost"],
        port=int(conf[active_environment]["SQLPort"]),
        db=conf[active_environment]["SQLDB"],
    )
    return cnx


def get_active_environment():
    conf = configparser.ConfigParser()
    conf.read("configuration.ini")
    return conf["DEFAULT"]["ActiveEnvironment"]



@Decorators.determine_environment
def raw_connection():
    con_str = construct_con_str()
    engine = create_engine(con_str)
    return engine


def construct_con_str():
    active_environment = get_active_environment()
    print(active_environment)
    conf = configparser.ConfigParser()
    conf.read("sensitive.ini")
    return (
        "mysql+pymysql://"
        f"{conf[active_environment]['SQLUsername']}"
        f":{conf[active_environment]['SQLPassword']}"
        f"@{conf[active_environment]['SQLHost']}"
        f":{int(conf[active_environment]['SQLPort'])}"
        f"/{conf[active_environment]['SQLDB']}"
    )
