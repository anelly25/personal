import tkinter as tk

from MVC.Model import Model
from MVC.View import View
from MVC.Controller import Controller

import socket



class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC Demo')

        # create a model
        model = Model('hello@pythontutorial.net')

        # create a view and place it on the root window
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)


        


        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP
        server.bind(('localhost', 2000))  # 127.0.0.1
        server.listen()

        client_socket, client_address = server.accept()

        file = open('server.file.jpg', "wb")
        image_chunk = client_socket.recv(2048)  # stream-based protocol

        while image_chunk:
            file.write(image_chunk)
            image_chunk = client_socket.recv(2048)

        file.close()
        client_socket.close()