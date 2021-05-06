# Sender.py
import time, socket, sys

def decimalToBinary(n):  
    return n.replace("0b", "")

def binarycode(s):
    a_byte_array = bytearray(s, "utf8")

    byte_list = []

    for byte in a_byte_array:
        binary_representation = bin(byte)
        byte_list.append(decimalToBinary(binary_representation))

    #print(byte_list)
    a=""
    for i in byte_list:
        a=a+i
    return a

print("Initialising....\n")
time.sleep(1)


# Initialising socket connection
s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
host = '127.0.1.2'
s.bind((host, port))
print(host, "(", ip, ")\n")
name = input(str("Enter your name: "))
           
s.listen(1)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has connected!\nEnter [e] to exit!\n")
conn.send(name.encode())

while True:
    message = input(str("Message : "))
    
    # Sends Message 
    conn.send(message.encode())
    if message == "[e]":
        message = "Left!"
        conn.send(message.encode())
        print("\n")
        break
    
    # Converts Message into Binary Code (ASCII Value)
    message=binarycode(message)
    
    # Length if message in binary
    f=str(len(message))
    
    # Sends length 
    conn.send(f.encode())
   
    i=0
    j=0
    j=int(input("Enter the window size -> "))
    
   
    b=""
   
    j=j-1
    f=int(f)
    k=j
    
    # i=0 -> binary length
    while i!=f:
        
        # i=0 -> binary length - window_size -1 [Window Size range]
        while(i!=(f-j)):
            # Sends first bit (from left)
            conn.send(message[i].encode())
            
            # Receives acknowledgement
            b=conn.recv(1024)
            
            # Decodes acknowledgment
            b=b.decode()
            print(b)
            if(b!="ACK Lost"):
                # If acknowledged
                time.sleep(0.5)
                print("Acknowledgement Received! The sliding window is in the range "+(str(i+1))+" to "+str(k+1)+" Now sending the next packet")
                i=i+1
                k=k+1
                time.sleep(0.5)
            else:
                # If not acknowldeged then repeat
                time.sleep(0.5)
                print("Acknowledgement of the data bit is LOST! The sliding window remains in the range "+(str(i+1))+" to "+str(k+1)+" Now Resending the same packet")
                time.sleep(0.5)
        
        # For any remaing Packet 
        while(i!=f):
            
            conn.send(message[i].encode())
            b=conn.recv(1024)
            b=b.decode()
            print(b)
            if(b!="ACK Lost"):
                time.sleep(0.5)
                print("Acknowledgement Received! The sliding window is in the range "+(str(i+1))+" to "+str(k)+" Now sending the next packet")
                i=i+1
                time.sleep(0.5)
            else:
                time.sleep(0.5)
                print("Acknowledgement of the data bit is LOST! The sliding window remains in the range "+(str(i+1))+" to "+str(k)+" Now Resending the same packet")
                time.sleep(0.5)
            
     
