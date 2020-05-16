import cli

if(__name__ == '__main__'):
    cli.manager()


'''
Note that I use a pipenv virtual environment for this solution. To use the same setup do the following:

pip install pipenv
navigate to project root
pipenv shell
pipenv sync

note that if you don't have the same python version as I used, then you're going to have to change it yourself in the Pipfile

[requires]
python_version = "3.7"

CLI commands:

python main.py exercise -1
python main.py exercise -2 [index value]
python main.py exercise -3

test connection to mysql with:
nose2 -v

Note that exercise 3 will NOT work for you, unless you construct your own sensitive.ini file in the project root.
This is, ofc, because I don't want to share my mysql information (hence the file name). 
It's in the .gitignore file.

This is the format:

[PRODUCTION]
ServerUser=
Distribution=
SQLUsername=
SQLPassword=
SQLHost=
SQLDB=
SQLPort=

[LOCAL]
SQLUsername=
SQLPassword=
SQLHost=
SQLDB=
SQLPort=
'''