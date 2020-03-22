Chosen Assignment Hand-In 8 - Black Tears

Data URL: http://samplecsvs.s3.amazonaws.com/SacramentocrimeJanuary2006.csv

I've translated the assignment to english

1. Download the data from the link and save it in a dataframe. Save it in a MySQL database.
2. Make a function which returns a dict containing, as a minimum, the following data:
   a. The amount of crimes between two given dates in 2006(as parametres to the function)
   b. Find the total amount of burglaries in January
3. Make a flask server in which you can open, as a minimum, the following endpoints:
   a. GET: Returns data about the amount of crimes in a given period
   b. POST: Returns the total amount of burglaries in janaury exclusively as data, which request.body contains a json object with {'key' : 'secret}

In this Hand-In I will play around with some different techniques out of interest and not necessity.

Note that the DB settings are hidden away in an

Instructions:

testing: 'nose2 -v'

cli commands:

python main.py ex --flask
python main.py ex --sync
python main.py ex --between date1 date2

dateformat: yyyy-mm-dd

endpoints(local):
http://127.0.0.1:5000/rest/burglary
http://127.0.0.1:5000/rest/{to}={from}
example:
http://127.0.0.1:5000/rest/2006-01-05=2006-03-20

server-side: http://178.62.118.111/

Please be aware, that this program requires a 'sensitive.ini' file to function correctly.
I don't feel like putting sensitive information out there tbh.
If you want to run this program, then you're going to have to create a 'sensitive.ini' file by yourself

Q: Why restplus?
A: Because base URL documentation http://127.0.0.1:5000/ and because I was interested
