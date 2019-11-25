#!/usr/bin/python
# imports
import socket                
  
# create the socket 
sock = socket.socket()          
print "Socket successfully created"
  
# setting the server port
#port = 1050
port = 12345                

# bind the socket to the port 
sock.bind(('', port))
# print a message saying that the socket is binded to the port  
# note: need to use the percent symbol to concatenate strings and ints      
print "socket binded to Port: %s "%(port) 

# set the server to listen for any client requests 
sock.listen(5)      
print "Waiting for client Requests"            
  
# setting the server to run for ever, so we can handle multple client requests
while True: 
  
   # Establish connection with client. 
   c, clientAddress = sock.accept() 
   # message holds the clients message that he has sent
   message = c.recv(1024);
   # printing out the clients message	
   print "Message from Client: "+message  
   # print a statement saying that a client has connected to the server and print the server addres  
   print 'Got connection from', clientAddress 
   response = message.isalpha()
   print response
   if response == True:
   	c.send('This message is true') 
   
  
   # Close the connection with the client 
   c.close() 
