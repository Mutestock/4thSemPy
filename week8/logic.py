import configparser
import bs4
import pandas as pd
import numpy as np

config = configparser.ConfigParser()
config.read("configuration.ini")


def data_sync():
    df = pd.read_csv(config["DEFAULT"]["URL"])
    print(df)
