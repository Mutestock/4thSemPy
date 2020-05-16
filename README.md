# 4thSemPy
repo for python assignments

The main.py file in the folders will often hold vital information for the assignment.
Herein CLI commands to demonstrate the solutions to the assignments.

##IMPORTANT:

###1:

Note that most of these assignments uses virtual environments

To use the same setup as I do:

pip install pipenv

go to project root

pipenv shell
pipenv sync

Replace the python_version in the pipfile if necessary.

###2:

Some of these assignments focuses on Rest services and connection to a database. 
These assignments require a 'sensitive.ini' file which contains connection information to the database.
This file is in .gitignore for obvious reasons.
If you want these assignments to work, you're going to have to do the following:

Create sensitive.ini file in project root.

Paste this in and fill in the information. 
Filling in the PRODUCTION section is only necessary if you're going to deploy.

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





