import urllib.request as ur
import requests
import json
import time
import os

from bs4 import BeautifulSoup


def processTable(soup, directoryPath, index):
    items = soup.find_all('table', {'class': 'wikitable'})
    result = items[index].find_all('a', {'class': "image image" +
                                     "-thumbnail link-internal"})
    outputJson = []
    if not(os.path.isdir("../images/")):
        os.makedirs("../images/")
    if not(os.path.isdir(directoryPath)):
        os.makedirs(directoryPath)
    for item in result:
        itemImage = item.find_all("img")[1].get('src')
        itemName = item.get('title')
        if not(os.path.isfile(directoryPath + itemName +".jpg")):
            image_link = ur.urlopen(itemImage)
            out_path = open(directoryPath + "/" + itemName +".jpg","wb")
            out_path.write(image_link.read())
            out_path.close()
        itemObject = {}
        itemObject["Name"] = item.get('title')
        itemObject["Image"] = directoryPath + item.get('title') + ".jpg"
        outputJson.append(itemObject)
    return outputJson

def printAllCurrentItems(Data):
    for item in Data["All"]:
        print(item["Name"])

def crawlWiki():
    URL = "http://oldschoolrunescape.wikia.com/wiki/Treasure_Trails"
    #response = requests.get(URL)
    page = ur.urlopen(URL)
    soup = BeautifulSoup(page, 'html.parser')
    data = {}
    allJson = processTable(soup, "../images/all", 1)
    #print(allJson)
    data["All"] = allJson
    easyJson = processTable(soup, "../images/easy", 2)
    data["Easy"] = easyJson
    with open("../data/Items.json", "w") as f:
        json.dump(data, f)
    f.close()

    with open("../data/Items.json", "r") as f:
        data = json.load(f)
    printAllCurrentItems(data)
    f.close()
if __name__ == "__main__":
    crawlWiki()

