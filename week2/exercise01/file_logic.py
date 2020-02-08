import os
from urllib.parse import urlparse
import urllib.request as req
import shutil
from argparse import PARSER as parser
from non_essential_qol import non_essential_qol as qol

directory = os.path.dirname(os.path.realpath(__file__))+"/downloads/"
urlList = ["http://data.kk.dk/dataset/76ecf368-bf2d-46a2-bcf8-adaf37662528/resource/9286af17-f74e-46c9-a428-9fb707542189/download/befkbhalderstatkode.csv"]
tupleList = [("cake", "Lul", "hi"), ("bye"), (123, 91, "something")]

#
# Exercise 1
#
#    Create a python file with 3 functions:
#        def print_file_content(file) that can print content of a csv file to the console

# A.


def print_file_content(*files):
    for file in files:
        with open(qol.file_name_handling(file), "r") as fileRead:
            data = fileRead.read()
            print(data+"\n")

# B

# pre rewrite


def write_list_to_file(output_file, lst):
    with open(output_file, "w") as fileWrite:
        for element in lst:
            fileWrite.write(str(element))

# write_list_to_file(directory+"_wltf_" +
#                  qol.file_name_handling(urlList[0]), tupleList)

# B. a.


def write_args_to_file(output_file, *args):
    with open(output_file, "w") as fileWrite:
        for element in args:
            fileWrite.write(element+"\n")


# write_args_to_file(directory+"_watf_" +
#                   qol.file_name_handling(urlList[0]), "cake", "John", "flem", "derp", "lul k")

# C


def read_csv(input_file):
    with open(qol.file_name_handling(input_file), "r") as fileRead:
        return [line for line in fileRead]


#csvLineList = read_csv(urlList[0])
# print(csvLineList)


def download(*urls, to=None):
    qol.qol_setup()
    for i, url in enumerate(urls):
        with req.urlopen(url[i]) as response, open(directory+qol.file_name_handling(url[i]), 'wb') as out_file:
            shutil.copyfileobj(response, out_file)


# download(urlList)
# print_file_content(urlList)

# 2.
# Using click package. See cli_ex.py
# A. --Path option
# B. --File option
# C. help="asdf" under each option
#
# Example usage:
# python exercise.py files --path example.csv --file cake.csv
# python exercise.py files --path example.csv
#
#
# If you need some test data, you can do this:
# python exercise.py files --download --path downloads\befkbhalderstatkode.csv --file cake.csv
# python exercise.py files --download --path downloads\befkbhalderstatkode.csv
#
# click is a standard package in python 3 in the sense that you don't need to manually download it, but I don't know about Anaconda
#
