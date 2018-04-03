import urllib.request as ur
import requests
import json
import time
import os

from bs4 import BeautifulSoup


def processAllTable(soup):
    items = soup.find_all('table', {'class': 'wikitable'})
    result = items[1].find_all('a', {'class': "image image" +
                                     "-thumbnail link-internal"})
    allJson = []
    if not(os.path.isdir("../images/")):
        os.makedirs("../images/")
    if not(os.path.isdir("../images/all")):
        os.makedirs("../images/all")
    for item in result:
        itemImage = item.find_all("img")[1].get('src')
        itemName = item.get('title')
        #print(itemName)
        #print(itemImage)
        if not(os.path.isfile("../images/all/" + itemName +".jpg")):
            image_link = ur.urlopen(itemImage)
            out_path = open("../images/all/" + itemName +".jpg","wb")
            out_path.write(image_link.read())
            out_path.close()
        itemObject = {}
        itemObject["Name"] = item.get('title')
        itemObject["Image"] = "../images/all/" + item.get('title') + ".jpg"
        allJson.append(itemObject)
    return allJson
def crawlWiki():
    URL = "http://oldschoolrunescape.wikia.com/wiki/Treasure_Trails"
    #response = requests.get(URL)
    page = ur.urlopen(URL)
    soup = BeautifulSoup(page, 'html.parser')
    data = {}
    allJson = processAllTable(soup)
    #print(allJson)
    data["All"] = allJson
    with open("../data/Items.json", "w") as f:
        json.dump(data, f)
    f.close()

if __name__ == "__main__":
    crawlWiki()

