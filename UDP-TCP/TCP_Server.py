import socket
import datetime

sock=socket.socket()
host=socket.gethostname()
port=5556
sock.bind((host, port))
sock.listen(1)
client,address=sock.accept()

while True:
    myData=client.recv(1024)
    str = myData.decode("utf-8")
    if str=="Ping":
        sendData=bytes("Pong","utf-8")
        client.send(sendData)
    if str=="Timestamp":
        myTime=datetime.datetime.now().strftime('%H:%M:%S %Y/%m/%d')
        sendData=bytes(myTime, "utf-8")
        client.send(sendData)
    if str=="Exit":
        client.close()
        break
    if str=="File":
        file = "medium.mp3"
        sendData= bytes(file, "utf-8")
        client.send(sendData)
        myfile= open(file, 'rb')
        parts=myfile.read(1024)
        while(parts):
            client.send(parts)
            parts= myfile.read(1024)
        myfile.close()


