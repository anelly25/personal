import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk,Image  

fileName = "";

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # set window title
        self.winfo_toplevel().title("Image Hashing Program")


        # create widgets
        # label
        self.uploadLabel = ttk.Label(self, text=' ', wraplength=210)
        self.uploadLabel.grid(row=1, column=1)

        # upload photo button
        self.uploadPhoto_button = ttk.Button(self, text='Choose Photo', width=30, command=self.browseFiles)
        self.uploadPhoto_button.grid(row=2, column=1, padx=5)

        # hashify button
        self.hashify_button = ttk.Button(self, text='Hashify', width=30, command=self.hashify_button_clicked, state=DISABLED)
        self.hashify_button.grid(row=2, column=2, padx=5)

        # hashify status label
        self.hashifyStatusLabel = ttk.Label(self, text='Test Text', wraplength=400)
        self.hashifyStatusLabel.grid(row=3, column=2, padx=5, pady=10)

        # check match button
        self.checkMatch_button = ttk.Button(self, text='Check for Match', width=30, command=self.checkMatch_button_clicked, state=DISABLED)
        self.checkMatch_button.grid(row=2, column=3, padx=5)

        # create empty preview canvas
        self.previewCanvas = tk.Canvas(self, bg='grey', width=550,height=350)
        self.previewCanvas.grid(row=4,column=2,pady=30)
        
        

        # set the controller
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller


    def hashify_button_clicked(self):
        self.controller.Sendtohashie(fileName);
        return

    def checkMatch_button_clicked(self):
        #self.controller.
        return

    def browseFiles(self):
        self.fileName = filedialog.askopenfilename(initialdir = "/",
                                              title = "Select a File",
                                              filetypes = (("Text files",
                                                            "*.jpg*"),
                                                           ("all files",
                                                            "*.*")))
        shortFilename = fileName[0:10] + "..." + fileName[-4:]
        
        # change label contents
        self.uploadLabel.configure(text="File Opened: " + shortFilename)
        #if good_file
        #    self.hashifyStatusLabel.configure(text="File ready to hash!")
        #else 
        #    self.hashifyStatusLabel.configure(text="Error", foreground='#ff0000')

        self.hashify_button['state'] = NORMAL
        self.checkMatch_button['state'] = NORMAL

        # display image
        self.previewImage = ImageTk.PhotoImage(Image.open(self.fileName).resize((500,300)))
        self.displayPreviewImage = ttk.Label(self, text='Image Preview', width=100, image=self.previewImage)
        self.displayPreviewImage.image = self.previewImage
        self.displayPreviewImage.grid(row=3, column=2, pady=30)

        
    
    
