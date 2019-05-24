from socket import*
from datetime import datetime
from random import randint


ip='10.10.7.251'
port=9000
host='localhost'

def recieveData(s,conn):
    data=conn.recv(128)
    print(conn,data)
    return data;

def main():
    s=socket(AF_INET,SOCK_STREAM)
    s.bind((host,port))
    s.listen(10)
    print("Server eshte duke punuar.... \n")
    conn, addr=s.accept()
    while 1:
        data = conn.recv(128)
        if not data:
            break
        toBeReturned=str(if_else_func(data.decode('ASCII')))
        conn.send(toBeReturned.encode('ASCII'))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def gjej_zanoret(germa):
        if (germa == 'a'
            or germa =='A'
            or germa == 'e'
            or germa == 'E'
            or germa == 'i'
            or germa == 'I'
            or germa == 'o'
            or germa == 'O'
            or germa == 'u'
            or germa == 'U'
            or germa == 'y'
            or germa == 'Y'):
            return True

def numero_zanoret(fjala):
     nr_zanoreve = 0
     for i in fjala:
         rezultati = gjej_zanoret(i)
         if rezultati == True:
             nr_zanoreve += 1
     return nr_zanoreve

def area(width,height):
    return width*height




def convert(opsioni=None, numer=None):
    if opsioni == "FahToCel":
        return(numer - 32.0) * (5.0/9.0)
    elif opsioni == "CelToFah":
        return(numer * (9.0/5.0)) + 32.0
    elif opsioni == "FahToKel":
        return((numer - 32.0) * (5.0/9.0)) + 273.15
    elif opsioni == "KelToFah":
        return((numer-273.15)*(5.0/9.0))+32.0
    elif opsioni == "CelToKel":
        return(numer + 273.15)
    elif opsioni == "KelToCel":
        return(numer - 273.15)
    elif opsioni == "KilToPou":
        return(numer * 2.2)
    elif opsioni == "PouToKil":
        return(numer / 2.2)


def keno():
    rezultati = ""
    i=0
    while(i<20):
        rezultati = rezultati + str(randint(1,80)) + ","
        i=i+1
    return rezultati


def harmonik(n):
    total=0.0
    for i in range(1,n+1):
        total+=1.0/(i)
    return total

def if_else_func(message):
    if message=='IP': return("IP addressa eshte =")+ip
    if message=='PORTI': return port
    if message=='KOHA': return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if message=='HOST': return host
    if message[:6] == 'PRINTO': return message[7:]
    if message[:9] == 'FAKTORIEL': return factorial(int(message[10:]))
    if message[:6] == 'ZANORE': return numero_zanoret(message[8:])
    if message == 'KENO': return keno()
    if message[:8] == 'KONVERTO': return convert(message[9:17], int(message[18:]))
    if message[:4]=='AREA': return area(int(message[5:6]), int(message[7:8]))
    if message[:9]=='HARMONIKA': return harmonik(int(message[10:]))
    return "Komand e panjohur. Shkruani edhe nje here kerkesen."

main()
