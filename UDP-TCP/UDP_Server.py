import socket
import datetime

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=socket.gethostname()
port=5678
sock.bind((host, port))
while True:
    mReq , client = sock.recvfrom(1024)
    sReq = mReq.decode("utf-8")
    if sReq== "Ping":
        sendData = bytes("Pong", "utf-8")
        sock.sendto(sendData,client)
    if sReq == "Timestamp":
        myTime = datetime.datetime.now().strftime('%H:%M:%S %Y/%m/%d')
        sendData = bytes(myTime, "utf-8")
        sock.sendto(sendData,client)
    if sReq == "Exit":
        sock.close()
        break
    if sReq=="File":
        file = "large.mp3"
        sendData= bytes(file, "utf-8")
        sock.sendto(sendData, client)
        myfile= open(file, 'rb')
        parts=myfile.read(1024)
        while(parts):
            sock.sendto(parts,client)
            parts= myfile.read(1024)
        myfile.close()
