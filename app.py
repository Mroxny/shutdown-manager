from operator import ipow
import tkinter as tk
from tkinter import *
import os
import subprocess
from turtle import width

window_height = 200
window_width = 400

path_icon = "Assets/sm.ico"

text_app_name = "Shutdown Manager"
text_con_1 = "Select action:"
text_execute = "Execute"

root = tk.Tk()


def shutdown(time_units):

    if time_units == "seconds" or time_units == 1:
        time.set(1)
    elif time_units == "minutes" or time_units == 60:
        time.set(60)
    elif time_units == "hours" or time_units == 3600:
        time.set(3600)

    
    print("Shutdown now in ", time.get())
    saveFile()
    #subprocess.run(["shutdown", "-s", "-t", 1])

def saveFile():
    print("Save file")


#Set title and icon of app
root.wm_title(text_app_name)
root.iconbitmap(default=path_icon)

#Set the size of Tkinter Frame
root.geometry("%dx%d" % (window_width,window_height))

#Set the resizable to false 
root.resizable(False, False)

#Add a canvas widget
canvas = Canvas(root)

#Add a Label widget in the Canvas
label = Label(canvas, text= text_con_1, font= ('Helvetica 17 bold'))
label.pack(pady= 10, padx=40, side= tk.TOP, )

#Create option menu 1
action = StringVar(root)
action.set("shutdown") # default value
w = OptionMenu(canvas, action, "shutdown", "restart",)
w.pack(pady=20, side= tk.LEFT)

#Create an Input to read values
entry= Entry(canvas, width= 5)
entry.focus_set()
entry.pack(pady=20,padx=10, side= tk.LEFT)

#Create option menu 2
time = StringVar(root)
time.set("minutes") # default value
w = OptionMenu(canvas, time, "seconds", "minutes", "hours",)
w.pack(pady=20, side= tk.RIGHT)

#Create a button in canvas widget
tk.Button(canvas, text= text_execute, command= shutdown(time_units=time.get()), ).pack(pady=20)


canvas.pack()
root.mainloop()