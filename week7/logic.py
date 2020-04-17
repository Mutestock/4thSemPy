from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import bs4


def selenium_sequence(query, item_count):
    merchbar = "https://www.merchbar.com"
    driver = webdriver.Firefox()
    driver.get(merchbar)
    driver.implicitly_wait(5)

    search_field = driver.find_element_by_xpath(
        "//span[@class='twitter-typeahead']/input[1]"
    )
    search_field.send_keys(" ".join(query))
    search_field.send_keys(Keys.ENTER)
    # search_field.submit()

    sleep(5)
    try:
        fucking_adds_man = driver.find_element_by_class_name("close")
        if fucking_adds_man:
            fucking_adds_man.click()
    except:
        pass
    items = []
    page_sauce = driver.page_source
    soup = bs4.BeautifulSoup(page_sauce, "html.parser")
    total_product_count = soup.find("div", {"class": "d-none d-md-block col-md-3"})
    total_product_count = total_product_count.select_one("span").text.split("products")[
        0
    ]
    print("================================")
    print("Total product count: " + total_product_count)
    print("requested: " + str(item_count))
    print("================================")
    sleep(1)
    print("Iterating entries...")
    sleep(0.1)
    repition_doorstopper = {"len": 0, "repetition": 0}
    while True:
        print(len(items))
        if len(items) < item_count and len(items) < int(total_product_count):
            page_sauce = driver.page_source
            soup = bs4.BeautifulSoup(page_sauce, "html.parser")
            driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + Keys.END)
            sleep(0.2)
            items = soup.find_all("div", {"class": "col-md-4 col-6"})
            if repition_doorstopper["len"] == len(items):
                repition_doorstopper["repetition"] = (
                    repition_doorstopper["repetition"] + 1
                )
            print(repition_doorstopper["repetition"])
            repition_doorstopper["len"] = len(items)
        # if repition_doorstopper["repetition"] is 10:
        #    print("Caught in a loop. Continuing at:" + len(items))
        #    break
        else:
            break
    print("done")
    return items


def selenium_sequence_track_list(query, entry_number):
    merchbar = "https://www.merchbar.com"
    driver = webdriver.Firefox()
    driver.get(merchbar)
    driver.implicitly_wait(5)

    search_field = driver.find_element_by_xpath(
        "//span[@class='twitter-typeahead']/input[1]"
    )
    search_field.send_keys(query)
    search_field.send_keys(Keys.ENTER)
    # search_field.submit()

    sleep(5)
    try:
        fucking_adds_man = driver.find_element_by_class_name("close")
        if fucking_adds_man:
            fucking_adds_man.click()
    except:
        pass
    cd_category = driver.find_element_by_xpath("//label/span[text()='CDs']")
    cd_category.click()
    element = driver.find_element_by_xpath(
        f"//div[@class='col-md-4 col-6'][{entry_number}]"
    )
    element.click()
    sleep(1)
    page_sauce = driver.page_source
    soup = bs4.BeautifulSoup(page_sauce, "html.parser")
    sleep(1)
    # WebDriverWait(driver, 10).until(
    #    EC.presence_of_element_located((By.CLASS_NAME, "track"))
    # )
    try:
        tracks = soup.find_all("li", {"class": "track"})
        sleep(1)
        for track in tracks:
            print(track.text)
    except:
        print(
            "Could not find the tracklist with the selected format. Tell programmer to be smarter"
        )


def process_entries(query, item_count):
    items = selenium_sequence(query, item_count)
    print("Formatting html...")
    pseudo_objects = []
    for item in items:
        name = item.find("div", {"class": "MerchTile.module__title"}).text
        price = item.find("span", {"class": "MerchTile.module__price"}).text
        sale_price = price

        try:
            sale_price = item.find(
                "span", {"class": "MerchTile.module__salePrice"}
            ).text
        except:
            pass

        brand = item.find("div", {"class": "MerchTile.module__brandName"}).text

        stock = False
        if (
            str(item.find("div", {"class": "MerchTile.module__status"}).text)
            == "In Stock"
        ):
            stock = True

        pseudo_objects.append(
            {
                "name": name,
                "price": float(price.replace("DKK\xa0", "")),
                "sale_price": float(sale_price.replace("DKK\xa0", "")),
                "brand": brand,
                "in_stock": stock,
            }
        )
    return pseudo_objects
