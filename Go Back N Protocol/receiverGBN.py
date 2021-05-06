# Receiver.py
import time, socket, sys
import random


print("Initialising....\n")
time.sleep(1)

s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
host = '127.0.1.2'
name = input(str("\nEnter your name: "))
port = 1234
print("\nTrying to connect to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connected...\n")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "Joined!\nEnter [e] to exit \n")

while True:
    
    # Receives Message
    m=s.recv(1024)
    # Decodes it 'utf-8'
    m=m.decode()
    
    # Receives Length of Binary Message
    k=s.recv(1024)
    
    # Decodes the length
    k=k.decode()
    k=int(k)
    
    i=0
    a=""
    b=""
    f=random.randint(0,1)
    message=""
    
    # for i=0 -> Binary length
    while i!=k:
       
       # f Random number 0 or 1
       f=random.randint(0,1)
       
       
       if(f==0):
          b="ACK Lost"
          
          # Message received
          message = s.recv(1024)
          message = message.decode()
          # Sends this message
          s.send(b.encode())
         
       elif(f==1):
          b="ACK "+str(i)
          message = s.recv(1024)
          message = message.decode()
          
          # Sends this message
          s.send(b.encode())
          a=a+message
          i=i+1
          
       
    
    print("The message received is :", m)
   
