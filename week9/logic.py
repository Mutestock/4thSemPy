import re
from pprint import pprint
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

def ex01():
    """
    1. Use regex on the data to get every different ip - save the ip’s in a list.
    """    
    ip_list = []
    with open('./resources/iplist.log', 'r') as fileReader:
        ip_list = [ip.strip() for line in fileReader.readlines() for ip in re.sub("\n","",line).split(';')]
        ip_list = [ip for ip in ip_list if len(re.sub(r'[\w]','',ip))>=3]
    return ip_list


def ex02(index):
    """
    2. Use selenium(or hint) to paste an ip from the list to: https://www.whois.com/whois/ and get NetName, NetRange, OrgName, Address, City, StateProv, PostalCode Country, RegDate.
    """
    requested_values = ['NetName', 'NetRange', 'OrgName', 'Address', 'City', 'StateProv', 'PostalCode Country', 'RegDate', 'PostalCode']
    ip = ex01()[int(index)]    
    URL = f"https://www.whois.com/whois/{ip}"
    html = requests.get(URL).text
    soup = BeautifulSoup(html,'html.parser')
    text = soup.get_text()
    values = [value for value in text.split('\n') if value != '']
    # Note that value in requeste_values did not work as a substring functionality here for whatever reason.
    new_values = {}
    for line in values:
        for requested in requested_values:
            try:
                line.index(requested)
            except:
                pass
            else:
                spl = line.split(':')
                new_values[spl[0]] = spl[1].replace(' ','')
    pprint(new_values)
    return new_values
