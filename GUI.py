from tkinter import *
from tkinter.ttk import *
import cryptonews
from stocknews import *
from newsapi import *

cryptotreeview = createtreeviewcrypto()
stocktreeview = createtreeviewstock()

cryptonews.createlabelcrypto()
createlabelstock()

runthread()

def createwindow():
    updatetreeviewcrypto(cryptotreeview)
    updatetreeviewstock(stocktreeview, checklistst())

    screen.after(10, createwindow)

screen.after(10, createwindow)

mainloop()