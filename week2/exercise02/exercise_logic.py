import os
from pathlib import Path


def first_func(path):
    """
    1. first function takes a path to a folder and writes all filenames in the folder to a specified output file
    """
    with open("first_func_output.txt", "w") as fileWrite:
        for file in os.listdir(path):
            fileWrite.write(file+"\n")


def second_func(path):
    """
    2. second takes a path to a folder and write all filenames recursively(files of all sub folders to)
    """
    if(not os.path.isfile("second_func_output.txt")):
        Path("second_func_output.txt").touch()
    with open("second_func_output.txt", "w") as fileWrite:
        for root, dirs, files in os.walk(path):
            for file in files:
                fileWrite.write(file+"\n")
            for direc in dirs:
                second_func(direc)


def third_func(list_name):
    """
    3. third takes a list of filenames and print the first line of each
    """
    for element in list_name:
        with open(element) as fileRead:
            print(fileRead.readline())


def fourth_func(list_name):
    """
    4. fourth takes a list of filenames and print each line that contains an email(just look for @)
    """
    for element in list_name:
        with open(element) as fileRead:
            try:
                for line in fileRead.readlines():
                   # print(line)
                    if("@" in line):
                        print(line)
            except UnicodeDecodeError:
                print("file in fourth func unreadable")


def fifth_func(list_name):
    """
    5. fifth takes a list of md files and writes all headlines(lines starting with  # ) to a file
    Make sure your module can be called both fro/m cli and imported to another module
    Create a new module that imports utils.py and test each function.
    """
    lineList = []
    if(not os.path.isfile("fifth_func_output.txt")):
        Path("fifth_func_output.txt").touch()
    for element in list_name:
        with open(element, "r") as fileRead:
            lineList = [line for line in fileRead.readlines()
                        if(line[0] is '#')]
    with open("fifth_func_output.txt", "w") as fileWrite:
        for line in lineList:
            fileWrite.write(line)

        # except UnicodeDecodeError:
        #    print("Unicode decoder error in fifth")
