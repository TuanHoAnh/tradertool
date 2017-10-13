# import the library
from bittrex.appJar.appjar import gui
from bittrex.test.simple_tool import TradingBittrex
# handle button events

class Action:
    def click(self):
        buy = TradingBittrex()
        market = app.getEntry("market")
        volume = app.getEntry("volumeBitcoin")
        buy.run(market, volume)


    def changeStatus(self, content):
        app.setMessage('Selling', content)


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
action = Action
app.addButtons(["Submit"], action.click, 2, 0, 2)

app.stopLabelFrame()
app.startLabelFrame("Sell coin")
app.addLabel("lbSelling","Checking bid now",3,0)
app.addMessage("Selling","hello cmdslajfdlajf",3,1)
app.stopLabelFrame()
# app.setFocus("Market")
# start the GUI
app.go()