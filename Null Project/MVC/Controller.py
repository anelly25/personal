import socket



class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view


    #server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP
    #server.bind(('localhost', 2000))  # 127.0.0.1
    #server.listen()

    #hash_socket, hash_address = server.accept()

    #file = open('IMG_0683.JPG', "wb")
    #image_packet = hash_socket.recv(2048)  # stream-based protocol

    #while image_packet:
    #    file.write(image_packet)
    #    image_packet = hash_socket.recv(2048)

    #file.close()
    #hash_socket.close()


    def Sendtohashie(self, filename):

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP
        client.connect(('localhost', 2000))  # 127.0.0.1
        file = open(filename, 'rb')
        image_data = file.read(2048)
        while image_data:
            client.send(image_data)
            image_data = file.read(2048)
        file.close()
        client.close()
