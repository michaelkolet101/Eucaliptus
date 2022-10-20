from tkinter import *
import tkintermapview

spring_dict = {'לבן': [31.7491491, 35.1595220],
               "ליפתא": [31.7945347, 35.1964675],
               "אורן": [32.71649450567904, 35.16088925182809]}


def search():
    spring = e_1.get()
    map_widget.set_position(*spring_dict[spring])
    map_widget.set_zoom(100)

height, width = 31.74981496779026, 35.159690931785256

app = Tk()
app.geometry("500x300")

l_1 = Label(app, text="springs", font=1, border=2)
l_2 = Label(app, text="enter spring name:", font=1, border=2)
e_1 = Entry(app, width=30)
btn = Button(text="search", command=search)
map_widget = tkintermapview.TkinterMapView(app, width=800, height=600, corner_radius=0)

l_1.pack()
l_2.pack()
e_1.pack()
btn.pack()
map_widget.pack()

app.mainloop()