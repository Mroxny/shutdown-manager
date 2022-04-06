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


    
    print("Shutdown now in ", time.get())
    save_file()

    try:
        ans = subprocess.check_output(["shutdown", str(action_type), "-t", str(10 * time_multiplier)])

    except subprocess.CalledProcessError as e:
        print(e.output)
        print_error(msg="Error")


def print_error(msg):
    errorLabel = Label(root, text= msg, font= ('Helvetica 10 bold'), fg="#ff0000")
    errorLabel.place(relx=0.5, rely=0.65, anchor=CENTER)
    




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

#Add a Label widget in the Canvas
mainLabel = Label(canvas, text= text_con_1, font= ('Helvetica 17 bold'))
mainLabel.pack(pady= 10, padx=40, side= tk.TOP, )

#Create option menu 1
action = StringVar(root)
action.set("shutdown") # default value
w = OptionMenu(root, action, "shutdown", "restart",)
w.place(relx=0.3, rely=0.5, anchor=CENTER)

mainLabel = Label(root, text= "in", font= ('Helvetica 8 bold'))
mainLabel.place(relx=0.45, rely=0.5, anchor=CENTER)

#Create an Input to read values
entry= Entry(root, width= 5)
entry.focus_set()
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