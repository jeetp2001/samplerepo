from sample2 import display
from pystray import MenuItem as item
import pystray
import PIL.Image
from tkinter import *

def action1():
    master = Tk()
    e = Entry(master)
    e.pack()
    e.focus_set()
    def clear():
        e.delete(0, END)
    def destroy():
        master.destroy()    
    b1 = Button(master, text = "Search", width = 10, command = lambda: display(e.get()))
    b2 = Button(master, text = "Remove", width = 10, command = clear)
    b3 = Button(master, text = "Exit", width = 10, command = destroy)
    b1.pack()
    b2.pack()
    b3.pack()
    mainloop()

def action2():
    exit()

image = PIL.Image.open("/home/jeet/Documents/tray-icons/icon1.jpeg")    

menu = (item('Search',action1),item('Remove',action2))

icon = pystray.Icon('NAME',image,'title',menu)
icon.run()

