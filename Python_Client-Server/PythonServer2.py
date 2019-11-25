#!/usr/bin/python
# imports
import socket                
  
# create the socket 
sock = socket.socket()          
print "Socket successfully created"
  
# setting the server port
port = 1050
#Kill proccesses assosiated with the port number
#sudo fuser -k 1050/tcp


sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

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
   #message = c.recv(1024)
   
   #message = int(numArr)
   # printing out the clients message	
   #print type(message)
   #print len(numArr)
   for x in range (4):
   	numArr = [c.recv(1024)]
	print numArr[2] 
	
 

   counter = 1;

   #while counter <= 4:
   	#numArr = [message]
   message= 5
   

   print "Message from Client: %s"% message  
   # print a statement saying that a client has connected to the server and print the server addres  
   print 'Got connection from', clientAddress   
   def is_power2(message):

	return message != 0 and ((message & (message -1)) ==0)

   if(is_power2(message)):
     print "True"
     c.send('True')
   else:
     print "False" 
     c.send('False')

  
   # Close the connection with the client 
c.close() 
