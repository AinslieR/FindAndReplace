'''
Copyright (c) 2022 Ruan Ainslie

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
------------------------------------------------------------------------------

There should be no need to install tkinter (just incase "pip install tk")
It might be necessary to install zipfile ("pip install zipfile38")
'''


from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *

root = Tk() # This creates the main window 
root.title("PDF to Image Converter") #This is the title of the main window
# root.iconbitmap(r'C:\Users\rainslie\Documents\Python_Scripts\Python\EXEs\z.images\CGSlogo(1).ico') #If you want to use a custom icon, insert the directory here

def inputButton():
    global inputFolder, inLabel #Creates global variables to be used throughout the script
    
    root.filename = filedialog.askdirectory(initialdir=r"C:/", title="Select folder to be zipped") #This initiates a file dialogue for the user to select the folder location
    inputFolder = root.filename
    inLabel = Label(root, text="Input: " + inputFolder) #After the user selected the location, this label displays it
    inLabel.grid(column=0, row=0) #This makes the label display on the main window


def outputButton():
    global outputFolder, outLabel #Creates global variables to be used throughout the script
    
    root.filename = filedialog.askdirectory(initialdir=r"C:/", title="Select Output Location")#This initiates a file dialogue for the user to select the folder location
    outputFolder = root.filename
    outLabel = Label(root, text="Output: " + outputFolder) #After the user selected the location, this label displays it
    outLabel.grid(column=0, row=2) #This makes the label display on the main window

def button1Click():
    import os, zipfile, time

    def create_zip(folder_path, zipped_filepath):
        zip_obj = zipfile.ZipFile(zipped_filepath, 'w') # create a zip file in the required path
        for filename in next(os.walk(folder_path))[2]: # loop over all the files in this folder
            zip_obj.write(
                os.path.join(folder_path, filename), # get the full path of the current file
                filename, # file path in the archive: we put all in the root of the archive
                compress_type=zipfile.ZIP_DEFLATED
            )
        zip_obj.close
        
    def zip_subfolders(input_folder, output_folder):
        os.makedirs(output_folder, exist_ok=True) # create output folder if it does not exist
        for folder_name in next(os.walk(input_folder))[1]: # loop over all the folders in your input folder
            zipped_filepath = os.path.join(output_folder, f'{folder_name}.zip') # create the path for the output zip file for this folder
            curr_folder_path = os.path.join(input_folder, folder_name) # get the full path of the current folder
            create_zip(curr_folder_path, zipped_filepath) # create the zip file and put in the right location
                 
    if __name__=='__main__':
        zip_subfolders(inputFolder, outputFolder)

myButtonInDir = Button(root, text="Open File", command=inputButton) #Ths creates an "input" button
myButtonInDir.grid(row=1, column=0) #This displays the input button on the main window

myButtonOutDir = Button(root, text="Output location", command=outputButton) #Ths creates an "outputput" button
myButtonOutDir.grid(row=3, column=0) #This displays the output button on the main window

myButtonZip = Button(root, text="Zip", command=button1Click ) #Ths creates a "zip" button
myButtonZip.grid(row=4, column=0) #This displays the zip button on the main window

myButtonExit = Button(root, text="Exit", command=root.quit) #Ths creates an "exit" button
myButtonExit.grid(row=5,column=0) #This displays the exit button on the main window

root.mainloop()