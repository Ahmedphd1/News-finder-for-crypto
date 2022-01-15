from tkinter import *
from tkinter.ttk import *
from newsapi import *
import threading

# main frame
screen = Tk()
screen.title("News collector")

style = Style()
style.theme_use('clam')

# tab control
tabControl = Notebook(screen, width= 500, height = 450)

cryptotab = Frame(tabControl)

tabControl.add(cryptotab, text='Crypto news')

tabControl.pack(expand=1, fill="both")

def getcontrols():
    return tabControl

def createlabelcrypto():
    # labels
    cryptonews = Label(cryptotab, text="Crypto news", font=("Courier", 20), foreground="red")
    cryptonews.place(x=170, y=20)

def createtreeviewcrypto():
    # treeview
    treev = Treeview(cryptotab, selectmode='browse')
    treev.place(x=40, y=70)

    style.configure("Vertical.TScrollbar", gripcount=0,
                    background="green", darkcolor="DarkGreen", lightcolor="LightGreen",
                    troughcolor="blue", bordercolor="green", arrowcolor="blue")
    # scrollbar
    verscrlbar = Scrollbar(cryptotab, orient="vertical", command=treev.yview)
    verscrlbar.pack(side='right', fill="both")
    treev.configure(xscrollcommand=verscrlbar.set)

    # treeview columns
    treev["columns"] = ("1", "2")
    treev['show'] = 'headings'

    treev.column("1", width=200, anchor='c')
    treev.column("2", width=200, anchor='c')

    treev.heading("1", text="Symbol")
    treev.heading("2", text="Source")

    return treev

def updatetreeviewcrypto(treeview):

    if treeview.get_children():
        for i in treeview.get_children():
            treeview.delete(i)
            treeview.unbind("<Double-1>", link_tree(treeview))

    for ele in checklist():
        if 'currencies' in ele:
            treeview.insert("", 'end', values=(ele['currencies'][0]['code'], ele['url']))

    treeview.bind("<Double-1>", link_tree(treeview))

def link_tree(treeview):
    if treeview.selection():
        input_id = treeview.selection()

        print(input_id)

        url = treeview.item(input_id)['values'][1]

        import webbrowser
        webbrowser.open('{}'.format(url))

        treeview.selection_remove(treeview.selection())