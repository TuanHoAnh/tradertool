# import the library
from tradertool.bittrex.appJar.appjar import gui
from tradertool.bittrex.test.simple_tool import TradingBittrex
# handle button events
def click(button):
    buy = TradingBittrex()
    market = app.getEntry("market")
    volume = app.getEntry("volumeBitcoin")
    buy.run(market, volume)


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
app.addLabel("lbSelling","Checking bid now",3,0,1,1)
app.addMessage("Selling","hello cmdslajfdlajf",3,1,1,1)
app.stopLabelFrame()

# app.setFocus("Market")
# start the GUI
app.go()