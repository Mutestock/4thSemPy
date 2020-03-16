import matplotlib.pyplot as plt
from logic import process_entries
import pandas as pd
import bs4


def pie_related(query, item_count):
    items = process_entries(query, item_count)
    print("Baking pie...")
    processed = {"true": 0, "false": 0}
    for item in items:
        if (
            "".join(query).lower() in str(item["name"]).lower()
            or "".join(query).lower() in str(item["brand"]).lower()
        ):
            processed["true"] = processed["true"] + 1
        else:
            processed["false"] = processed["false"] + 1
    print(processed)
    flg, ax = plt.subplots()
    ax.pie(processed.values())
    ax.set_aspect("equal")
    plt.show()


def bar_sale(query, item_count):
    items = process_entries(query, item_count)
    df = pd.DataFrame(items, columns=["price", "name", "sale_price"])
    plt.title("sale vs actual")
    bar1 = plt.bar(df["name"], sorted(df["price"]))
    bar2 = plt.bar(df["name"], sorted(df["sale_price"]))
    plt.legend([bar1, bar2], ["Saved value", "Current price"], loc="upper right")
    plt.show()


def pie_sold_out(query, item_count):
    items = process_entries(query, item_count)
    processed = {"true": 0, "false": 0}
    for item in items:
        if item["in_stock"] == True:
            processed["true"] = processed["true"] + 1
        if item["in_stock"] == False:
            processed["false"] = processed["false"] + 1
    # print("baking pie...")
    # df = pd.DataFrame(items, columns=["in_stock"])
    # print(df["in_stock"])
    flg, ax = plt.subplots()
    ax.pie(processed.values())
    plt.show()
