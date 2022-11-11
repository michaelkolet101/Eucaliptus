from tkinter import *
import tkintermapview
from menege_db import *

colors = ['white', '#13C0DF']
fonts = [("Times", "27", "bold italic"), ("Helvetica", "15"), ("Helvetica", "13")]

def set_new_count(spring_name):

    count = int(e_1.get())
    update_load(spring_name, count)
    l_2.config(text="enter spring name:", bg=colors[1])
    btn.config(text="search", command=search, bg='white', fg='black')
    e_1.delete(0, END)

def update_spring(spring_name):
    l_2.config(text='Enter a new quantity', bg='green')
    e_1.delete(0, END)
    btn.config(text='Confirm', command=lambda: set_new_count(spring_name), bg='green', fg='white')



def search():
    spring = e_1.get()
    location_lst = get_location(spring)
    map_widget.set_position(location_lst['x'], location_lst['y'])
    map_widget.set_zoom(100)
    count = get_loads(spring)
    l_3.config(text=f'spring name: {spring}\n load of peple: {count}')
    btn1.grid(row=4, column=1, columnspan=1)

app = Tk()

app.geometry("380x600")
app.title("eucalyptus app")
app.config(bg=colors[1])

l_1 = Label(app, text="welcom to eucalyptus", bg=colors[1], fg=colors[0], font=fonts[0] , border=20)
l_2 = Label(app, text="enter spring name:", bg=colors[1],fg=colors[0], font=fonts[1])
l_3 = Label(app, text="", bg=colors[1] ,font=fonts[1], fg=colors[0], border=10, )

e_1 = Entry(app, width=30, border=2, font=("ariel", '10'))

btn = Button(text="search", command=search, font=fonts[2], border=2)
btn1 = Button(text="update load", command=lambda: update_spring(e_1.get()) ,font=fonts[2],border=2) # TODO the command move to page 2

map_widget = tkintermapview.TkinterMapView(app, width=300, height=300, corner_radius=1)

l_1.grid(row=0, column=0, columnspan=2, pady=20)
l_2.grid(row=1, column=0, columnspan=1)
e_1.grid(row=2, column=0, columnspan=1)
btn.grid(row=2, column=1, columnspan=1)
map_widget.grid(row=3, column=0, columnspan=2, pady=10)
l_3.grid(row=4, column=0, columnspan=1)








app.mainloop()