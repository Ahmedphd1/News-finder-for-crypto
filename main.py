from tkinter import *
from tkinter.ttk import *

# main frame
screen = Tk()
screen.title("News collector")

style = Style()
style.theme_use('clam')

# labels
cryptonews = Label(screen, text="Crypto news", font=("Courier", 20), foreground="red")
cryptonews.place(x=170, y=20)

# treeview
treev = Treeview(screen, selectmode='browse')
treev.place(x=40, y=70)

style.configure("Vertical.TScrollbar", gripcount=0,
                background="green", darkcolor="DarkGreen", lightcolor="LightGreen",
                troughcolor="blue", bordercolor="green", arrowcolor="blue")
# scrollbar
verscrlbar = Scrollbar(screen, orient="vertical", command=treev.yview)
verscrlbar.pack(side='right', fill="both")
treev.configure(xscrollcommand=verscrlbar.set)

# treeview columns
treev["columns"] = ("1", "2")
treev['show'] = 'headings'

treev.column("1", width=200, anchor='c')
treev.column("2", width=200, anchor='c')

treev.heading("1", text="Symbol")
treev.heading("2", text="Source")

treev.insert("", 'end', values=("BTC", "WWW.GOOGLE.COM"))

for Parent in treev.get_children():

    print(treev.item(treev.get_children())['values'])



mainloop()