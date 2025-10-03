#server
import socket
import threading
print("The Chat Has Started")
s=socket.socket()
host=socket.gethostbyname(socket.gethostname())
print(host)
port= 8080
s.bind((host,port))
servername=input("Enter Your Username:")
s.listen(1) #one client
print("Waiting for any connection")

conn,addr=s.accept()
print("\nRecieved Connection")


clientname=conn.recv(1024) 
clientname=clientname.decode() 
print(clientname,"Has connected to the chat Room")

conn.send(servername.encode())

def send_msg():
    while True:
      message=input("Please Enter your message: \n")
      conn.send(message.encode())
      print("Sent")
def recv_msg():
    while True:
      message=conn.recv(1024)
      message=message.decode()
      print(clientname," : ",message)
      
send_thread=threading.Thread(target=send_msg)
recv_thread=threading.Thread(target=recv_msg)
send_thread.start()
recv_thread.start()
