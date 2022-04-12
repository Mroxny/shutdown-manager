from ast import IsNot, Not
from asyncio.windows_events import NULL
from operator import ipow
import tkinter as tk
from tkinter import *
import os
import subprocess

window_height = 200
window_width = 400

path_icon = "Assets/sm.ico"

text_app_name = "Shutdown Manager"
text_con_1 = "Select action:"
text_execute = "Execute"



root = tk.Tk()



def shutdown():

    time_multiplier = 60
    if time.get() == "seconds":
        time_multiplier = 1
    elif time.get() == "minutes":
        time_multiplier = 60
    elif time.get() == "hours":
        time_multiplier = 3600

    action_type = "-s"
    if action.get() == "shutdown":
        action_type = "-s"
    elif action.get() == "restart":
        action_type = "-r"


    if len(entry.get()) <= 0:
        value  = 0
        entry.insert(END, value)

    else:
        try:
            value = int(entry.get())

        except:
            print_error("Please insert numbers")
            value = -1

    
    
    if value != -1:
        print("Shutdown now in", value, time.get())
        save_file()

        try:
            
            subprocess.check_output(["shutdown", str(action_type), "-t", str(value * time_multiplier)])
                
            print(value)
            print_error(clear=True)

        except subprocess.CalledProcessError as e:
            print(e.output)
            print_error("Error")



   


def print_error(msg="",clear=False):

    if clear == False:
        errorLabel.config(text=msg)
    else:
        errorLabel.config(text="")


    




def save_file():
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

#Add a main label in the Canvas
label = Label(canvas, text= text_con_1, font= ('Helvetica 17 bold'))
label.pack(pady= 10, padx=40, side= tk.TOP, )

#Add a Error label in the Canvas
errorLabel = Label(canvas, text="", font=('Helvetica 10 bold'), fg="#ff0000")
errorLabel.pack(side=tk.TOP)

#Create option menu 1
action = StringVar(root)
action.set("shutdown") # default value
w = OptionMenu(root, action, "shutdown", "restart",)
w.place(relx=0.3, rely=0.5, anchor=CENTER)

label = Label(root, text= "in", font= ('Helvetica 8 bold'))
label.place(relx=0.45, rely=0.5, anchor=CENTER)

#Create an Input to read values
entry= Entry(root, width= 5)

entry.insert(END, '0')
entry.place(relx=0.53, rely=0.5, anchor=CENTER)

#Create option menu 2
time = StringVar(root)
time.set("minutes") # default value
w = OptionMenu(root, time, "seconds", "minutes", "hours",)
w.place(relx=0.67, rely=0.5, anchor=CENTER)

#Create a button in canvas widget
exeButton = tk.Button(root, text= text_execute, command= lambda: shutdown(), )
exeButton.pack(pady=20, side= tk.BOTTOM)

canvas.pack()
root.mainloop()