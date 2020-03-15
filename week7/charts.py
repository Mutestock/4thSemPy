import matplotlib.pyplot as plt
from logic import process_entries
import bs4


def pie_related(query, item_count):
    items = process_entries(query, item_count)
    print("Baking pie...")
    processed = []
    for item in items:
        print(item)
        print(item["name"])
        if "".join(query) in str(item["name"]) or "".join(query) in str(item["brand"]):
            item["related"] = True
        else:
            item["related"] = False
        processed.append(item)
    print(processed)


def pie_sale(query, item_count):
    items = process_entries(query, item_count)
    print("ba")
    pass


def pie_sold_out():
    pass
