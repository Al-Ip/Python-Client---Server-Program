#!/usr/bin/python
# Imports 
import socket                
  
# create the socket
sock = socket.socket()                      
  
# connect to the port on and ip address
# taking in ip address and port number

#ip_addr = raw_input("Plese enter an Ip Address: ")
ip_addr = '127.0.0.1'
#port_num = input("Plese enter an Port Number: ")
port_num = 12345 

# passing in ip address and port number
sock.connect((ip_addr, port_num)) 

clientMessage = raw_input(b"Please Enter a Message: ")

##sock.send(b"Hello")
sock.send(clientMessage)
  
# print out server response
print sock.recv(1024) 
# close the socket
sock.close() 
