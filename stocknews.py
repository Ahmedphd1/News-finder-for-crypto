from tkinter import *
from tkinter.ttk import *
from cryptonews import *
import threading

tabcontrols = getcontrols()

stocktab = Frame(tabcontrols)

tabControl.add(stocktab, text='Stock news')

tabControl.pack(expand=1, fill="both")

def createlabelstock():
    # labels

    cryptonews = Label(stocktab, text="Stock news", font=("Courier", 20), foreground="green")
    cryptonews.place(x=170, y=20)

def createtreeviewstock():
    # treeview
    treev = Treeview(stocktab, selectmode='browse')
    treev.place(x=40, y=70)

    style.configure("Vertical.TScrollbar", gripcount=0,
                    background="green", darkcolor="DarkGreen", lightcolor="LightGreen",
                    troughcolor="blue", bordercolor="green", arrowcolor="blue")
    # scrollbar
    verscrlbar = Scrollbar(stocktab, orient="vertical", command=treev.yview)
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

def updatetreeviewstock(treeview, list):
    if treeview.get_children():
        for i in treeview.get_children():
            treeview.delete(i)
            treeview.unbind("<Double-1>", link_tree_stock(treeview))

    if list:
        for ele in list:
            if 'related' in ele:
                treeview.insert("", 'end', values=(ele['related'], ele['url']))

    treeview.bind("<Double-1>", link_tree_stock(treeview))

    pass

def link_tree_stock(treeview):
    if treeview.selection():
        input_id = treeview.selection()

        print(input_id)

        url = treeview.item(input_id)['values'][1]

        import webbrowser
        webbrowser.open('{}'.format(url))

        treeview.selection_remove(treeview.selection())
