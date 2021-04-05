# Multithreading is needed to establish 2 connections at the same time and so that the return message 
# doesn't just send the order in which the clients connected

from socket import *
import threading
from multiprocessing import Queue
import time

host = 'Ren'
port = 12000

#create the socket 
s = socket(AF_INET, SOCK_STREAM)
s.bind((host, port))
s.listen(2)
q = Queue(maxsize=3 )
print('Server ready to recieve')

#thread function
def thread_function(name):
    global fmessage
    while True:
        c, addr = s.accept()
        c.send(("Client " + name + " connected").encode())
        print("Client connected, will be named " + name)
        cmsg = c.recv(1024).decode()
        print("From " + name + ": " + cmsg)
        #checks to see if a message was already sent
        if(q.empty()): #message sent is the first
            q.put(cmsg)
            if(threads[0] == name):
                fmessage = threads[0] + " received before " + threads[1]
            else:
                fmessage = threads[1] + " received before " + threads[0]
        else: #message sent isn't the first
            q.get()
            if(threads[0] == name):
                fmessage = threads[1] + " received before " + threads[0]
            else:  
                fmessage = threads[0] + " recieved before " + threads[1]
        c.send(fmessage.encode())
threads = ["X", "Y"]
x = threading.Thread(target = thread_function, args = ("X",))
x.start() #creates and starts the first thread
y = threading.Thread(target=thread_function,args=("Y",))
y.start #creates and starts the second thread
x.join()
y.join()
