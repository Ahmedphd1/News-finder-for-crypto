import requests
import time
import threading
import json
from datetime import datetime
from datetime import timedelta
from datetime import date

newslist = None
newsliststock = None

def getlatestnewscrypto():
      global newslist

      while True:
            try:
                  allnews = requests.get("https://cryptopanic.com/api/v1/posts/?auth_token=06f93314b38f0ae69af532cb8241454977b82438&filter=lol").json()

                  newsele = allnews['results']
                  newslist = newsele

                  time.sleep(6)
            except:
                  print("cannot find crypto")

def getlatestnewsstocks():
      global newsliststock

      today = datetime.today().strftime('%Y-%m-%d')

      with open("tickers.txt", mode="r") as f:
            mylist = f.readlines()

      while True:
            stocklist = []
            try:
                  for items in mylist:
                        response = requests.get(f'https://finnhub.io/api/v1/company-news?symbol={items.strip()}&from={today}&to={today}&token=bsc851nrh5rcbdomt6s0')

                        if type(response.json()) == list and len(response.json()) >= 1:

                              stocklist.append(response.json()[0])
            except:
                  print("cannot find ticker")

            newsliststock = stocklist

def runthread():
      thread1 = threading.Thread(target=getlatestnewscrypto, daemon=True)
      thread2 = threading.Thread(target=getlatestnewsstocks, daemon=True)
      thread1.start()
      thread2.start()

def checklist():
      while True:
            if newslist:
                  return newslist

def checklistst():
      if newsliststock:
            return newsliststock

