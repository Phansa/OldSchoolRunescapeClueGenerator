import urllib.request as ur
import requests
import json
import time
import os
from bs4 import BeautifulSoup

#Install pip and run
#pip install request
#pip install beautifulsoup4
#befor runnign this program
def saveImage(directoryPath, itemName, itemImage):
    if not(os.path.isfile(directoryPath + itemName +".jpg")):
        imageLink = ur.urlopen(itemImage)
        out_path = open(directoryPath + "/" + itemName +".jpg","wb")
        out_path.write(imageLink.read())
        out_path.close()


def processGeneralTable(soup, directoryPath, index):
    difficulty = directoryPath.split('/')[-1] + "/"
    items = soup.find_all('table', {'class': 'wikitable'})
    result = items[index].find_all('a', {'class': "image image" +
                                     "-thumbnail link-internal"})
    outputJson = []
    if not(os.path.isdir(directoryPath)):
        os.makedirs(directoryPath)
    for item in result:
        itemImage = item.find_all("img")[1].get('src')
        itemName = item.get('title')
        saveImage(directoryPath, itemName, itemImage)
        itemObject = {}
        itemObject["Name"] = item.get('title')
        itemObject["Image"] = "/images/" + difficulty + item.get('title') + ".jpg"
        outputJson.append(itemObject)
    return outputJson

def processSingleItem(wikiUrl, directoryPath):
    difficulty = directoryPath.split('/')[-1] + "/"
    page = ur.urlopen(wikiUrl)
    soup = BeautifulSoup(page, "html.parser")
    itemName = wikiUrl.split('/')[-1]
    if('_' in itemName):
        itemName = itemName.replace('_', ' ')
    if(itemName == "Cowl"):
        itemName = "Leather cowl"
    itemJson = {}
    itemJson["Name"] = itemName
    #The ' character gets replaced in the image's alt tag
    if("d'hide" in wikiUrl):
        newItemName = itemName.replace("'", "&#039;")
        itemImage = soup.find_all("img", {"alt":newItemName})
    else:
        itemImage = soup.find_all("img", {"alt": itemName})#[1].get('src')
    for image in itemImage:
        if("vignette" in image.get('src')):
            itemImage = image.get('src')
            break
    itemJson["Image"] = "/images/" + difficulty + itemName + ".jpg"
    saveImage(directoryPath, itemName, itemImage)
    return itemJson

def processTalismans(wikiUrl, directoryPath, table):
    difficulty = directoryPath.split('/')[-1] + "/"
    page = ur.urlopen(wikiUrl)
    soup = BeautifulSoup(page, "html.parser")
    #Taken from https://stackoverflow.com/questions/28240956/bea
    #utifulsoup-find-only-elements-where-an-attribute-contains-a-
    #sub-string-is-th
    images = soup.findAll('img', alt=lambda x: x and 'talisman' in x)
    for image in images:
        if("vignette" in image.get('src')):
            talismanJson = {}
            itemName = image.get('alt')
            itemImage = image.get('src')
            talismanJson["Name"] = itemName
            talismanJson["Image"] = "/images/" + difficulty + itemName + ".jpg"
            table.append(talismanJson)
            saveImage(directoryPath, itemName, itemImage)

def allowedArmorCheck(item):
    disallowed = ["crossbow", "bolts", "arrow", "dart",
                  "javelin", "thrownaxe", "knife", "(t)", "(g)", "(h",
               "(lg)", "brutal", "defender", "gloves", "nails", "hide", "Wiki"]
    for itemName in disallowed:
        if(itemName in item):
            return False
    return True

def processArmorAndWeapons(armorType, directoryPath, table):
    difficulty = directoryPath.split('/')[-1] + "/"
    wikiUrl = "http://oldschoolrunescape.wikia.com/wiki/" + armorType
    page = ur.urlopen(wikiUrl)
    soup = BeautifulSoup(page, "html.parser")
    armorName = armorType.split('_')[0]
    images = soup.findAll('img', alt=lambda x: x and armorName in x)
    for image in images:
        itemName = image.get('alt')
        if(allowedArmorCheck(itemName)):
            itemJson = {}
            itemImage = image.get('src')
            itemJson["Name"] = itemName
            itemJson["Image"] = "/images/" + difficulty + itemName + ".jpg"
            table.append(itemJson)
            saveImage(directoryPath, itemName, itemImage)
        
def tableHelper(table, itemName, directoryPath):
    table.append(processSingleItem("http://" +
        "oldschoolrunescape.wikia.com/wiki/" + itemName,
        directoryPath))

def addTableDrops(table):
    unique = {}
    unique["Name"] = "Unique"
    unique["Image"] = "Null"
    table.append(unique)
    allDrop = {}
    allDrop["Name"] = "All"
    allDrop["Image"] = "Null"
    table.append(allDrop)

def processEasyCommonTable(directoryPath):
    easyCommonTable = []
    #Processing single items from common drop table
    tableHelper(easyCommonTable,"Oak_plank", directoryPath)
    tableHelper(easyCommonTable,"Willow_shortbow", directoryPath)
    tableHelper(easyCommonTable,"Coif", directoryPath)
    tableHelper(easyCommonTable,"Cowl", directoryPath)
    tableHelper(easyCommonTable,"Leather_vambraces", directoryPath)
    tableHelper(easyCommonTable,"Leather_chaps", directoryPath)
    tableHelper(easyCommonTable,"Leather_body", directoryPath)
    tableHelper(easyCommonTable,"Yew_shortbow", directoryPath)
    tableHelper(easyCommonTable,"Salmon", directoryPath)
    tableHelper(easyCommonTable,"Trout", directoryPath)
    tableHelper(easyCommonTable,"Steel_pickaxe", directoryPath)
    #Processing armor and weapon sets from common drop table
    processArmorAndWeapons("Black_equipment", directoryPath,
                           easyCommonTable)
    #Processing talismans
    processTalismans("http://oldschoolrunescape.wikia.com/wiki/Talisman",
                     directoryPath, easyCommonTable)
    #Adding Unique and All drop items
    addTableDrops(easyCommonTable)
    return easyCommonTable

def processMediumCommonTable(directoryPath):
    mediumCommonTable = []
    #Processing single items from common drop table
    tableHelper(mediumCommonTable,"Adamant_pickaxe", directoryPath)
    tableHelper(mediumCommonTable,"Adamantite_nails", directoryPath)
    tableHelper(mediumCommonTable,"Adamant_crossbow", directoryPath)
    tableHelper(mediumCommonTable,"Fire_battlestaff", directoryPath)
    tableHelper(mediumCommonTable,"Green_d'hide_body", directoryPath)
    tableHelper(mediumCommonTable,"Green_d'hide_chaps", directoryPath)
    tableHelper(mediumCommonTable,"Yew_shortbow", directoryPath)
    tableHelper(mediumCommonTable,"Teak_plank", directoryPath)
    tableHelper(mediumCommonTable,"Swordfish", directoryPath)
    tableHelper(mediumCommonTable,"Lobster", directoryPath)
    #Processing armor and weapon sets from common drop table
    processArmorAndWeapons("Adamant_equipment", directoryPath,
                           mediumCommonTable)
    #Adding Unique and All drop items
    addTableDrops(mediumCommonTable)
    return mediumCommonTable

def processHardCommonTable(directoryPath):
    hardCommonTable = []
    #Processing single items from common drop table
    tableHelper(hardCommonTable,"Black_d'hide_body", directoryPath)
    tableHelper(hardCommonTable,"Black_d'hide_chaps", directoryPath)
    tableHelper(hardCommonTable,"Black_d'hide_vamb", directoryPath)
    tableHelper(hardCommonTable,"Magic_shortbow", directoryPath)
    tableHelper(hardCommonTable,"Magic_longbow", directoryPath)
    tableHelper(hardCommonTable,"Law_rune", directoryPath)
    tableHelper(hardCommonTable,"Nature_rune", directoryPath)
    tableHelper(hardCommonTable,"Shark", directoryPath)
    tableHelper(hardCommonTable,"Lobster", directoryPath)
    #Processing armor and weapon sets from common drop table
    processArmorAndWeapons("Rune_equipment", directoryPath,
                           hardCommonTable)
    #Adding Unique and All drop items
    addTableDrops(hardCommonTable)
    return hardCommonTable

def printAllCurrentItems(Data):
    for category in Data:
        print(category)
        for item in Data[category]:
            print(item)

def crawlWiki():
    URL = "http://oldschoolrunescape.wikia.com/wiki/Treasure_Trails"
    page = ur.urlopen(URL)
    soup = BeautifulSoup(page, 'html.parser')
    if not(os.path.isdir("../public/images/")):
        os.makedirs("../public/images/")
    data = {}
    data["All"] = processGeneralTable(soup, "../public/images/all", 1)
    easyDirectoryPath = "../public/images/easy"
    data["EasyUnique"] = processGeneralTable(soup, easyDirectoryPath, 2)
    data["EasyCommon"] = processEasyCommonTable(easyDirectoryPath)
    mediumDirectoryPath = "../public/images/medium"
    data["MediumUnique"] = processGeneralTable(soup, mediumDirectoryPath, 3)
    data["MediumCommon"] = processMediumCommonTable(mediumDirectoryPath)
    hardDirectoryPath = "../public/images/hard"
    data["HardUnique"] = processGeneralTable(soup, hardDirectoryPath, 4)
    data["HardCommon"] = processHardCommonTable(hardDirectoryPath)
    with open("../src/data/Items.json", "w") as f:
        json.dump(data, f)
    f.close()

    with open("../src/data/Items.json", "r") as f:
        data = json.load(f)
    #printAllCurrentItems(data)
    f.close()
if __name__ == "__main__":
    crawlWiki()

