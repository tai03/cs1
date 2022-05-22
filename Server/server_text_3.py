import socket
import time
localtime = time.asctime( time.localtime(time.time()) )
host = 'local host'
port = 5000
def count(n):
    while n>0:
        print(':%s'%(n))
        time.sleep(1)
        n -= 1 
        if n == 0:
            print('----------Done----------')
# create a socket at server side using TCP / IP protocol
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# bind the socket with server and port number
s.bind(('', port))
# allow maximum 1 connection to the socket
s.listen(1)
print('----------Listening----------')
# wait till a client accept connection
c, addr = s.accept()
# display client address
print('Connection!')
Client_address = {'Client IP:':addr[0], 'Client HOST:':addr[1]}
for I,H in Client_address.items():
    print(I,H)
# print("CONNECTION FROM:", str(addr))
print('TIME:',localtime)
# send message to the client after encoding into binary string
c.send(b"------ONline-----")
count(10)
msg = "-----Offline-----"
c.send(msg.encode())
# disconnect the server
c.close()
