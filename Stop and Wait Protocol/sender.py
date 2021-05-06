import socket
from threading import *

# Creates Socket connection object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8000

# Local Socket Connection is established at port number 8000
serversocket.bind((host, port))

# Sends data to receiver.py
class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            r=input("Send data -->")
            if r=="exit":
                break
            clientsocket.send(r.encode())
            # Decodes at most 1024 bytes
            print(clientsocket.recv(1024).decode())
            
# Waits till connected with receiver.py
serversocket.listen(5)
print ('Sender ready and is listening')


#to accept all incoming connections
clientsocket, address = serversocket.accept()
print("Receiver "+str(address)+" connected")
'''create a different thread for every 
    incoming connection''' 
client(clientsocket, address)
