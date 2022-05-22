# 服务器
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))
print('---UDP on 9999---')
print('----listening----')
while True:
    # 接收数据
    data, addr = s.recvfrom(1024)
    print('Received from %s : %s. ' % addr)
    print
    reply = 'Online!, %s' % data.decode('utf-8')
    s.sendto(reply.encode('utf-8'),addr)