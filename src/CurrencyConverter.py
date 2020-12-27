from tkinter import *
import requests
import json

root = Tk()
root.title("USD Currency Converter")
root.geometry("500x220")

r = requests.get("http://api.currencylayer.com/live?access_key=") #API key removed for privacy reasons
jsonObject = json.loads(r.content)

def calculate():
    find = "USD"+currency.get()
    if currency.get() == "Select a Currency":
        print("Error...")
    else:
        rate = float(jsonObject['quotes'][find])
        foreignAmount = float(amountEntry.get()) * rate
        usdLabel = Label(root, text=str(float(amountEntry.get())) + " USD = " + str(round(foreignAmount,2)) + " " + currency.get(), font=("Palatino",21))
        usdLabel.place(x=250, y=184, anchor="center")

titleLabel = Label(root, text="USD Currency Converter", width=50, bg="#195e83", fg="white", font=("Palatino",24))
titleLabel.place(x=-50,y=0)

fromLabel = Label(root, text="Amount:            From:                             To:", font=("Palatino",18))
fromLabel.place(x=20,y=50)

amountEntry = Entry(root, width=10)
amountEntry.place(x=23,y=70)
amountEntry.insert(0,"1.00")

usdLabel = Label(root, text="United States Dollar", font=("Palatino",17))
usdLabel.place(x=145,y=73)

currency = StringVar()
currency.set("Select a Currency")
currencyOptions = ["EUR", "GBP", "JPY", "CAD", "PLN", "CHF", "AUD", "CNY"]
currencyEntry = OptionMenu(root, currency, *currencyOptions)
currencyEntry.place(x=325, y=73)

convertButton = Button(root, text="Convert", width=10,height=2,command=calculate)
convertButton.place(x=200,y=115)

root.mainloop()