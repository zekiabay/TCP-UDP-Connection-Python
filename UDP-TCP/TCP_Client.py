import socket
import time

socket.setdefaulttimeout(1)
sock=socket.socket()
host=socket.gethostname()
port=5556
sock.connect((host,port))
myReq = input("Enter Request for TCP: ")
while myReq!="Exit":
    sendData= bytes(myReq,"utf-8")
    sock.send(sendData)
    if myReq!="File":
        received=sock.recv(1024).decode("utf-8")
        print(received)
    else:
        fileBit = sock.recv(1024)
        print(fileBit.decode("utf-8"))
        newFileName = "mediumTCP.mp3"
        with open(newFileName,'wb') as newFile:
            sTime = time.time()
            while True:
                try:
                    wData=sock.recv(1024)
                    newFile.write(wData)
                except socket.timeout:
                    break
            newFile.close()
            print("time: " , (time.time()-sTime-1.0))
    myReq = input("Enter Request for TCP: ")
sendData=bytes(myReq, "utf-8")
sock.send(sendData)
sock.close()

