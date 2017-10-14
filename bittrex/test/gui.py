# import the library
from appJar import gui
from bittrex.test.simple_tool import TradingBittrex
import threading

class BuyingThread (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name

   def run(self):
       buy = TradingBittrex()
       market = app.getEntry("market")
       volume = app.getEntry("volumeBitcoin")
       buy.run(market, volume,changeStatus)

# handle button events
def click(self):
    buyThread = BuyingThread(1,"Buying")
    buyThread.start()

def changeStatus(content):
    app.setLabel('Selling', content)

# create a GUI variable called app
app = gui("Trader Tool", "600x400")
app.setBg("white")
app.setFont(18)

# # add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Bittrex")
app.setLabelBg("title", "gray")
app.setLabelFg("title", "orange")

app.startLabelFrame("Buy coin")
app.setSticky("ew")
app.setFont(20)

app.addLabel("labelMarket", "Market", 0, 0,1)
app.addEntry("market", 0, 1,2)
app.addLabel("labelVolume", "Volume Bitcoin", 1, 0,1)
app.addNumericEntry("volumeBitcoin", 1, 1,2)
app.addButtons(["Submit"], click, 2, 0, 2)

app.stopLabelFrame()
app.startLabelFrame("Sell coin")
app.addLabel("lbSelling","Checking bid now",3,0,2)
app.addLabel("Selling","....",3,2,1)
app.setLabelFont(15,"Comic Sans")
app.stopLabelFrame()
# app.setFocus("Market")
# start the GUI
app.go()