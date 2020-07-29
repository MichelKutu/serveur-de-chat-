import socket 
import threading
import sys 


class Server: 
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connections=[]
    def __init__(self):
        self.sock.bind(('0.0.0.0',10000))
        self.sock.listen(5)

    

    def handler (self , c,a):
        while True :
            data = c.recv(1024)
            for connection in self.connections:
                if c != connection:
                    connection.send(bytes(data))
                if not data : 
                    print(str(a[0])+" : "+ str(a[1]) + "disconnected")
                    self.connections.remove(c)
                    c.close()
                    break 
                
                
    def run (self):     
        while True: 
            print("server running ...")
            c,a=self.sock.accept()
            cthread = threading.Thread(target=self.handler , args=(c,a))
            cthread.daemon=True
            cthread.start()
            self.connections.append(c)
            print(str(a[0])+" : "+ str(a[1]) + "connected")
            
            
class Client:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    def sendMsg(self):
        while True:
            self.sock.send(bytes(input("")))      
            
    def __init__(self,address):
        self.sock.connect((address,10000))
         
        ithread= threading.Thread(target=self.sendMsg)
        ithread.daemon=True
        ithread.start()
        
        while  True:
            data=self.sock.recv(1024)
            if not data:
                break 
            print(str(data,'utf-8'))
            
    

if (len(sys.argv)> 1):
    client=Client(sys.argv[1])
else:     
    serveur=Server()
    serveur.run()

    