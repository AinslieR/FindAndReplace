from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import os

root = Tk() # This creates the main window 
root.title("Find and Replace") #This is the title of the main window
# root.iconbitmap(r'C:\Users\rainslie\Documents\Python_Scripts\Python\EXEs\z.images\CGSlogo(1).ico') #If you want to use a custom icon, insert the directory here

def inputButton():
    global inputFolder, inLabel #Creates global variables to be used throughout the script
    
    root.filename = filedialog.askdirectory(initialdir=r"C:\Users\rainslie\Documents", title="Select folder to be process") #This initiates a file dialogue for the user to select the folder location
    inputFolder = root.filename
    inLabel = Label(root, text="Input: " + inputFolder) #After the user selected the location, this label displays it
    inLabel.grid(column=0, row=0) #This makes the label display on the main window

lookForValue = Entry(root, width=50) #This is the box for the manual text input
lookForValue.grid(column=0, row=2) #This just packs the value to the root window
lookForValue.insert(0, "Look for")

replaceWithValue = Entry(root, width=50) #This is the box for the manual text input
replaceWithValue.grid(column=0, row=3) #This just packs the value to the root window
replaceWithValue.insert(0, "Replace with")

def button1Click():
    os.chdir(inputFolder)
    
    files = os.listdir(inputFolder)

    for src in files:
        dst = src.replace(lookForValue.get(), replaceWithValue.get())
        os.rename(src,dst) 

    # changeLabel = Label(root, text="List of name changes:\n " + src + " : " + dst) #After the user selected the location, this label displays it
    # changeLabel.grid(column=0, row=5) #This makes the label display on the main window

myButtonInDir = Button(root, text="Select location", command=inputButton) #Ths creates an "input" button
myButtonInDir.grid(row=1, column=0) #This displays the input button on the main window

myButtonRun = Button(root, text="Run", command=button1Click ) #Ths creates a "zip" button
myButtonRun.grid(row=4, column=0) #This displays the zip button on the main window

myButtonExit = Button(root, text="Exit", command=root.quit) #Ths creates an "exit" button
myButtonExit.grid(row=6,column=0) #This displays the exit button on the main window

root.mainloop()


