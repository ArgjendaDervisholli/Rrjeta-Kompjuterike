from socket import*

host='localhost'
port=9000

socketClient=socket(AF_INET,SOCK_DGRAM)
while 10:
    message=input("enter message :")
    socketClient.sendto(message.encode('ASCII'),(host,port))
    if_else_func=socketClient.recvfrom(128)
    print("Pergjigja: " + if_else_func.decode('ASCII'))
    socketClient.close()