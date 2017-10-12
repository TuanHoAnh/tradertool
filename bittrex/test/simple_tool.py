
import json
from tradertool.bittrex.bittrex import Bittrex
from decimal import *


class TradingBittrex:
    ask = 0
    volum = 0
    def setUp(self):
        with open("secrets.json") as secrets_file:
            self.secrets = json.load(secrets_file)
            secrets_file.close()
        self.bittrex = Bittrex(self.secrets['key'], self.secrets['secret'])

    def buyCoin(self,market,bit):
        ticket = self.bittrex.get_ticker(market)
        self.ask = ticket["result"]["Ask"]
        self.volum = bit/self.ask
        actual = self.bittrex.buy_limit(market,self.volum,self.ask)

    def sellCoin(self,market):
        ticket = self.bittrex.get_ticker(market)
        bid = ticket["result"]["Bid"]
        priceUp= self.ask*1.05
        priceDown = self.ask*0.95
        count =0
        while((priceDown<=bid)&(bid<=priceUp)):
            count += 1
            ticket = self.bittrex.get_ticker(market)
            bid = ticket["result"]["Bid"]
            print("\nwaiting... bid="+str(round(Decimal(bid),8) )+" time:"+str(count))
        print("\nsucess")
        self.bittrex.sell_limit(market,self.volum,bid)

    def run(self,market,bit):
        self.setUp()
        volum = self.buyCoin(market,bit)
        ask = self.sellCoin(market)
