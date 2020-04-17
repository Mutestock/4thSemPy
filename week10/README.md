Chosen assignment - happy county:

data: https://github.com/AndreasVikke/CPH-Business-Python/blob/master/Week9/WeekExcersies/ip-logfile.log

1. Use regex on the data to get every different ip save the ip’s in a list.
2. Use selenium(or hint) to paste an ip from the list to: https://www.whois.com/whois/ and get NetName, NetRange, OrgName, Address, City, StateProv, PostalCode Country, RegDate.
3. Store some of the data in a database with PyMySQL and create a flask server with a GET endpoint to show all the data stored in the DB. (Optionally deploy flask server on your droplet)

hints:

- Data is a CSV file use your knowledge about CSV.
- Save regex result to a set to easy deal with duplicates.
- You can use https://whois.whoisxmlapi.com/ instead of selenium"
