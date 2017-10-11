# import the library
from bittrex.appJar.appjar import gui

# handle button events
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("User:", usr, "Pass:", pwd)

def click(button):
    print("clicked.........."+str(app.getEntry("market")))


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

app.addLabel("labelMarket", "Market", 0, 0)
app.addEntry("market", 0, 1)
app.addLabel("labelVolume", "Volume Bitcoin", 1, 0)
app.addEntry("volumeBitcoin", 1, 1)
app.addButtons(["Submit"], click, 2, 0, 2)
app.stopLabelFrame()

# app.setFocus("Market")
# start the GUI
app.go()