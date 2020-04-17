import configparser
import bs4
import pandas as pd
import numpy as np
import json
from datetime import datetime
from decorators import Decorators
from connector import raw_connection


@Decorators.determine_environment
def data_sync():
    config = configparser.ConfigParser()
    config.read("configuration.ini")

    df = pd.read_csv(config["DEFAULT"]["URL"])
    df = df.applymap(str)
    df.to_sql("profiles", con=raw_connection(), if_exists="replace", index=False)


# This solves 2. But it's not what I need for 3.
# def crimes_between_dates(a, b):
#    df = pd.read_sql_table("profiles", con=raw_connection(), parse_dates=["cdatetime"])
#    # print(df[["crimedescr", "cdatetime"]])
#    df1 = df[(df["cdatetime"] > a) & (df["cdatetime"] < b)]
#    total_between = df1.shape[0]
#    df2 = df[df["crimedescr"].str.contains("BURGLARY")]
#    total_burglary = df2.shape[0]
#    return {"total_burglary": total_burglary, "total_between": total_between}


def crimes_between_dates(a, b):
    df = pd.read_sql_table("profiles", con=raw_connection(), parse_dates=["cdatetime"])
    df = df[(df["cdatetime"] > a) & (df["cdatetime"] < b)]
    return df.shape[0]


def total_burglary():
    df = pd.read_sql_table("profiles", con=raw_connection(), parse_dates=["cdatetime"])
    df = df[df["crimedescr"].str.contains("BURGLARY")]
    return df.shape[0]
