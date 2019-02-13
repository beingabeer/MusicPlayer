import time
import os
from tkinter import *
import tkinter.messagebox
from pygame import mixer
import play
from functools import partial


# Initialize pygame music mixer
mixer.init()

root = Tk()

# Title
root.title("Title")
root.configure(background='grey')

# Icon
# root.call('wm', 'iconphoto', root._w, PhotoImage(file='logo.ico'))

# Fullscreen
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("{}x{}+0+0".format(w, h))

# Frame for tool bar
topframe = Frame(root, bg="black")
topframe.pack(side=TOP, expand=NO, fill=X)


# Start songs button
Satsang_button = Button(topframe, text="Play songs", command=)
Satsang_button.config(height=1)
Satsang_button.pack(fill=X)


# Create main menu bar
menu_bar = Menu(root)


# Create the submenu (
Exit_menu = Menu(menu_bar)
path_menu = Menu(menu_bar)


# Add the "File" drop down sub-menu in the main menu bar
menu_bar.add_cascade(label="Path List", menu=path_menu)
menu_bar.add_cascade(label="Exit", menu=Exit_menu)


# Add commands to submenu
Exit_menu.add_separator()
Exit_menu.add_command(label="Exit", command=root.destroy)


path_list = []
path_list = (file for file in os.listdir() if 'mp3' in file)
path_menu.add_separator()

for path in path_list:
    path_menu.add_command(label=path, command=partial(play.play_audio, path))


root.config(menu=menu_bar)

# Show text on root window
Label(root,
      text="Sample Text",
      fg="white",
      bg="black",
      font="Verdana 20 bold").pack(fill=X)

imgPath = "Image.png"
photo = PhotoImage(file=imgPath)
img = photo.subsample(1, 1)
label = Label(image=img)
label.pack()

# Status bar
status = Label(root,
               text="Status..",
               bd=5,
               relief=SUNKEN,
               font="Verdana 10",
               anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()
