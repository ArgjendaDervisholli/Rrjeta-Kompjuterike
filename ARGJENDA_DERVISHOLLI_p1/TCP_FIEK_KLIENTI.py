from socket import*

host='localhost'
port=9000

socketClient=socket(AF_INET,SOCK_STREAM)
socketClient.connect((host,port))
while 10:
    message=input("Shkruani Kërkesën :")
    socketClient.send(message.encode('ASCII'))
    if_else_func=socketClient.recv(128)
    print("Pergjigja: " + if_else_func.decode('ASCII'))