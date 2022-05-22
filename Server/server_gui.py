import tkinter as tk
import socket
import time
from tkinter.constants import CENTER, LEFT
localtime = time.asctime( time.localtime(time.time()) )
TIME = list(localtime)
def server_program():
    labelHello.config(text = ("-----Listening Connection-----"))
    # time_left1 = 5
    # time_left2 = 5
    # while time_left1 > 0:
    #     time.sleep(1)
    #     time_left1 = time_left1 - 1
    host = socket.gethostname()
    port = 5002  #default may be 
    server_socket = socket.socket() 
    server_socket.bind((host, port))  
    server_socket.listen(2)
    conn, address = server_socket.accept() 
    data = conn.recv(1024).decode()
    labelHello.config(text = ("Connected: %s" %data))
    # while time_left2 > 0:
    #     time.sleep(1)
    #     time_left2 = time_left2 - 1
    labelHello.config(text=("Client IP:",str(address[0])+"\n"+"Client HOST:",str(address[1]) +"\n" ,"TIME:",str(TIME)),height=20,width=45,justify=CENTER,pady=2)

def close_program(self):
    socket.socket.close(self)
    # labelHello.config(text = ("-----Waiting-----"))
    pass

top = tk.Tk()

top.title("Server")
labelHello = tk.Label(top, text = "-----Waiting-----", height = 20, width = 45, fg = "black",justify=CENTER,pady=2)
labelHello.pack()

btnCal = tk.Button(top, text = "Hook!", command = server_program)
btnCal.pack()

btnCal = tk.Button(top, text = "Close", command = close_program)
btnCal.pack()


top.mainloop()