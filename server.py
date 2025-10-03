#client
import socket
import threading
print("The Chat Has Started")
s=socket.socket()
host=input("Enter the IP of your host:")
myname=input("Please Enter Your Name:")
port=8080

print("Trying To Connect To",host,"At Port",port)


s.connect((host,port))
print("Connected")

s.send(myname.encode())

servername=s.recv(1024) 
servername=servername.decode()
print(servername,"Has joined The Chat Room")

def recv_msg():
    while True:
       message=s.recv(1024)
       message=message.decode()
       print(servername," :",message)
def send_msg():
    while True:
      message=input("Please Enter your message:\n ")
      s.send(message.encode())
      print("Sent")

send_thread=threading.Thread(target=send_msg)
recv_thread=threading.Thread(target=recv_msg)
send_thread.start()
recv_thread.start()