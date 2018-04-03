import urllib.request as ur
import requests
import json
import time
from pathlib import Path


def getItemsFromCatalogue(idNumber,startingLetter,pageNumber):
    URL = "http://services.runescape.com/m=itemdb_oldschool/api/catalogue"  \
    + "/items.json?category=" + str(idNumber) + "&alpha=" \
    + str(startingLetter) + "&page=" + str(pageNumber)
    response = requests.get(URL)
    return response.json()

def getFromCatalogue(Number):
    URL = "http://services.runescape.com/m=itemdb_oldschool/" \
    + "api/catalogue/category.json?category=" + Number
    response = requests.get(URL)
    return response.json()

def getQuery(Item):
    URL = "http://services.runescape.com/m=itemdb_oldschool" + Item
    response = requests.get(URL)
    return response.json()

def getItemDetail(ItemId):
    URL = "http://services.runescape.com/m=itemdb_oldschool/api/" \
    + "catalogue/detail.json?item=" + str(ItemId)
    response = requests.get(URL)
    return response.json()


def getItemDetailForJson(ItemId):
    URL = "http://services.runescape.com/m=itemdb_oldschool/api/" \
    + "catalogue/detail.json?item=" + str(ItemId)
    response = requests.get(URL)
    if(response.status_code == 404):
        data = {}
        data["Id"] = ItemId
        data["Name"] = "Invalid"
        data["Icon"] = "Invalid"
        data["IconLarge"] = "Invalid"
        return data
    else:
        result = response.json()
        data = {}
        data["Id"] = ItemId
        data["Name"] = result["item"]["name"]
        data["Icon"] = result["item"]["icon"]
        data["IconLarge"] = result["item"]["icon_large"]
        return data

# Godbooks are located in category 27
def getGodBooks():
    #FindArmdayl and Ancient
    count = 0
    pageNumber = 1
    while(count != 8):
        response = getItemsFromCatalogue(27,"a", pageNumber)
        for item in response["items"]:
            print(item)
        count +=1

    return 0

#Prints all current items found in the items.json
def printAllCurrentItems(Data):
    for item in Data["Items"]:
        print(item["Name"])

#Goes through each item id up to around 40,000 and
#stores them in my items.json file. There is a rate limit of
#one request per 5 seconds which is why the sleep is there.
def findAllValidItems():
    #Creates file if it doesn't exist yet
    itemsFile = Path("../data/Items.json")
    if not(itemsFile.is_file()):
        data = {}
        data["MaxIndex"] = 0
        data["Items"] = []
        with open("../data/Items.json", "w") as f:
            json.dump(data, f)
        f.close()
    with open("../data/Items.json", "r") as f:
        data = json.load(f)
    f.close()
    #printAllCurrentItems(data)
    i = data["MaxIndex"]
    print("Current max index is " + str(i))
    while(i < 350):
        response = getItemDetailForJson(i)
        i += 1
        data["MaxIndex"] = i
        if(response["Name"] != "Invalid"):
            print("Found " + response["Name"])
            data["Items"].append(response)
        time.sleep(5)
    with open("../data/Items.json", "w") as f:
        json.dump(data, f)
    f.close()

if __name__ == "__main__":
    findAllValidItems()

