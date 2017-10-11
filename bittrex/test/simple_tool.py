
import json
from bittrex.bittrex import Bittrex


# IS_CI_ENV = True if 'IN_CI' in os.environ else False

# def test_get_ticker(self):
#     actual = self.bittrex.get_ticker(market='BTC-LTC')
class TradingBittrex:
    ask = 0
    volum =0
    def setUp(self):
        with open("secrets.json") as secrets_file:
            self.secrets = json.load(secrets_file)
            secrets_file.close()
        self.bittrex = Bittrex(self.secrets['key'], self.secrets['secret'])

    def buyCoin(self,market,bit):
        ticket = self.bittrex.get_ticker(market)
        self.ask = ticket["result"]["Ask"]
        self.volum = bit/self.ask
        # actual = self.bittrex.buy_limit(market,volum,self.ask)

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
            print("\nwaiting... bid="+str(bid)+" time:"+str(count))
        print("\nsucess")
        self.bittrex.sell_limit(market,self.volum,bid)

    def run(self,market,bit):
        self.setUp()
        # volum = self.buyCoin(market,bit)
        self.ask=0.00054586
        self.volum=2.85216054
        ask = self.sellCoin(market)
        self.ask
buy = TradingBittrex()
buy.run("BTC-ARK",0.001)
