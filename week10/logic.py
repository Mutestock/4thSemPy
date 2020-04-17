import json
import re
import os
import pandas as pd
from urllib import request
import bs4
from io import StringIO


def reg_log_file(file):
    """
    Use regex on the data to get every different ip save the ip’s in a list.
    """
    return [re.split(";", ip)[1] for ip in open(file)]


def rip_info(file):
    """
    2. Use selenium(or hint) to paste an ip from the list to: https://www.whois.com/whois/ and get NetName, NetRange, OrgName, Address, City, StateProv, PostalCode Country, RegDate.
    """
    url = "https://www.whois.com/whois/"
    ip_list = reg_log_file(file)
    raw_data = {}
    switcheroo = []
    requested_parametres = [
        "NetRange",
        "CIDR",
        "NetName",
        "NetHandle",
        "Parent",
        "NetType",
        "OriginAS",
        "Organization",
        "RegDate",
        "Updated",
        "Ref",
        "OrgName",
        "OrgId",
        "Address",
        "City",
        "StateProv",
        "PostalCode",
        "Country",
        "Updated",
        "OrgTechHandle",
        "OrgTechName",
        "OrgTechEmail",
        "OrgAbuseHandle",
        "OrgAbuseName",
        "OrgAbusePhone",
    ]
    reg = r"|\b"
    thing = requested_parametres[1:]
    concatted = reg.join(thing)
    concatted = f"{concatted}{requested_parametres[0]}"

    df = pd.DataFrame()

    for param in requested_parametres:
        df[param] = None

    # for ip in ip_list:
    #    item = None
    #    item = __rip_it(url, ip)
    #    if item:
    #        print(f"{ip} appended..")
    #    else:
    #        print(f"{ip} skipped!")
    #    for line in item:
    #        if line & not 'Comment' in line and not '<' in line and not '>' in line and not '#' in line:
    #            print(line)
    #            if not ip in raw_data:
    #                raw_data[ip] = []
    #            # switcheroo = raw_data[ip]
    #            # switcheroo.update()
    #            raw_data[ip].append(str(item))
    #            df = pd.DataFrame([x.split(":") for x in line.split("\n")])

    print("Extracting data from ips. Please hold")
    all_info = []
    formatted = {}
    for ip in ip_list:
        all_info.append(f"!£!@!~!!{ip}")
        all_info.append(str(__rip_it(url, ip)))
        print(f"{ip} appended..")
    for i, item in enumerate(all_info):
        cut_lines = item.split("\n")
        ip = None
        row = {}
        for line in cut_lines:
            lc = line
            ip = line.copy().split("!£!@!~!!")[1]
            key_val = line.split(":", 1)
            print(key_val[0])
            if key_val[0] in requested_parametres:
                row[key_val[0]] = key_val[1]
        for param in requested_parametres:
            if param not in row:
                row[param] = None
        print(row)
        formatted[ip] = row
    print(formatted)
    return raw_data


def __rip_it(url, ip):
    """
    requisite of 2.
    """
    htmlrip = request.urlopen(url + ip)
    byte = htmlrip.read().decode("utf-8")
    htmlrip.close()
    soup = bs4.BeautifulSoup(byte, "html.parser")
    item = soup.find("pre", {"class": "df-raw"})
    return item


def format_data(raw_data):
    outer = {}
    sorted_data = {}
    for data in raw_data:
        for line in data:
            if line:
                line = str(line)
                if line[0] != "%" and line[0] != "<" and line and line[0] != "#":
                    split_thing = line.split(": ")
                    if not split_thing[0] in sorted_data:
                        sorted_data[split_thing[0]] = {}
                    switcheroo = sorted_data[split_thing[0]]
                    switcheroo.append(split_thing[1])
                    sorted_data[split_thing[0]] = switcheroo
    json_format = json.dumps(sorted_data, indent=4)
    print(json_format)
    df = pd.DataFrame.from_dict(sorted_data)
    print(df)
