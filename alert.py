# ebay avg price script
# search page for avg price and give it to you
from bs4 import BeautifulSoup
import requests
import re
import tweepy
import os
import time
from random import randint
from time import gmtime, strftime
from url import *

def avgPrice(url):
    headers = {'User-agent': 'Mozilla/5.0'}
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data,"html.parser")
    soldPrice = []
    itemNames = []
    # amntRegex = re.compile('\W[0-9]*')
    # amntRegex = re.compile('\$.(\d+).(\d+)')
    amntRegex = re.compile('((\d+).(\d+).(\d+)|(\d+).(\d+))')

    count = 0
    for details in soup.find_all("li",{"id": "item1c7a25e4c1", "r":"1"}):
        price = details.find_all("li",{"class": "lvprice prc"})
        link = details.find_all('a')
        for lin in link:
            print(lin['href'])




    exit()


    # Only check items from US + ignore "similar items" 
    count = int((soup.find_all("span",{"class":"rcnt"}))[0].text.replace(",",""))

    # all items on page
    items = soup.find_all("ul",{"id": "ListViewInner"})
    
    # Exit if too many results!
    try:
        itemPrice = items[0].find_all("span",{"class": "bold bidsold"})
    except Exception as e:
        print("\nSearch to broad! Too many items!")
        exit()
    try:
        itemName = items[0].find_all("h3",{"class": "lvtitle"})
    except:
        print("\nSearch to broad! Too many items!")
        exit()


    # for soldItems in range(0,count):
    #     currentPrice = (re.search(amntRegex,str(itemPrice[soldItems].text).lstrip().rstrip().strip())).group()
    #     soldPrice.append(float(currentPrice.replace(",","")))
    #     itemNames.append(str(itemName[soldItems].text).encode('utf-8').strip())
        
    #     print(soldPrice)
    #     exit()
    #     # Note max of 198
    #     if soldItems == 198:
    #         break;

    # soldPrice = list(map(float, soldPrice))


    print("\nTotal items: ",count)
    print("Highest: ",max(soldPrice))
    print("Lowest: ",min(soldPrice))

    # Write sold prices to a file
    f = open('ebaySales.txt', 'w')
    for sales in range(len(itemNames)):
        f.write(str(itemNames[sales])+" : "+str(soldPrice[sales])+"\n")
    f.close()

    averagePrice = (sum(soldPrice) / float(len(soldPrice)))
    print("The avg price is: $%.2f"%averagePrice)
    print("The median price is $%.2f"%statistics.median(soldPrice))
    print("The mean price is $%.2f"%statistics.mean(soldPrice))


def main():
    # Get Input:
    print("This script will tweet when someone beats your lowest price\n")
    price = "359.44"

    avgPrice(url)

main()
