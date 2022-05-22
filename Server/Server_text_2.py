import socket
import time
localtime = time.asctime( time.localtime(time.time()) )

print('----------Loading----------')
def server_program():
    host = socket.gethostname()
    port = 5000  
    server_socket = socket.socket() 
    server_socket.bind((host, port))  
    server_socket.listen(2)
    conn, address = server_socket.accept() 
    print('----------Listening----------')
    print("Connection!  \n")
    print('Client IP:' , address[0] + '\t' +'Client HOST:', address[1])
    print('TIME:',localtime)
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("From Connected Client: " + str(data))
        print('Client IP:' , address[0] + '\t' +'Client HOST:', address[1])
        print('TIME:',localtime)
        data = input(' -> ')
        conn.send(data.encode()) 
    conn.close() 


if __name__ == '__main__':
    server_program()
