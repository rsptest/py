from socket import *

# Running on mininet
serverName = 'mininet-vm' #Hostname goes here
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

# Receive the message to be the setting clients
clientName = clientSocket.recv(1024).decode()
print("From Server "+ clientName)

# Sending message to the server
msg = input("Enter a message to send to server: ")
clientSocket.send(msg.encode())

# Receive the final message
fresponse = clientSocket.recv(1024).decode()
print("From Server: " + fresponse)

# Close the connection
clientSocket.close()
