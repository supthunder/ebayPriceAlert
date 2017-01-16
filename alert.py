# ebay avg price script
# search page for avg price and give it to you
from bs4 import BeautifulSoup
import requests
import tweepy
import os
import time
from time import gmtime, strftime
from url import *
from tokens import *

# setup twitter
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)

# insert your username here
username = ""

def tweet(listingPrice,listinglink):
    tweet = "Someone beat your price "
    tweet += "@"+username+"!\n"
    tweet += "New Price: $"+str(listingPrice)
    tweet += "\nLink: "+listinglink+"\n"
    tweet += strftime("%Y-%m-%d %H:%M:%S", gmtime())
    # print(tweet)
    api.update_status(tweet) 



def avgPrice(url, price):
    # connect to eBay
    headers = {'User-agent': 'Mozilla/5.0'}
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data,"html.parser")

    
    listinglink = ""
    listingPrice = ""
    # pull the lowest price
    for details in soup.find_all("li",{"id": "item1c7a25e4c1", "r":"1"}):
        value = details.find_all("li",{"class": "lvprice prc"})
        for eachPrice in value:
            listingPrice = str(eachPrice.text).strip()
            break;

        href = details.find_all('a')
        for links in href:
            listinglink = links['href']
            break;

    listingPrice = float(listingPrice[1:])
    if listingPrice < price:
        tweet(listingPrice,listinglink)
    else:
        print("Your item has the lowest price!")


def main():
    # Insert values here:
    print("This script will tweet when someone beats your lowest price\n")
    
    # insert a float() price
    price = 0.00

    avgPrice(url, price)

main()
