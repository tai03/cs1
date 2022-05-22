import tkinter as tk
import socket
from tkinter.constants import LEFT, RIGHT

def client_program():
    host = str(entryCd.get())
    port = 5002  #default may be 
    client_socket = socket.socket() 
    client_socket.connect((host, port))  # connect to the server
    message = "Client Online!"
    client_socket.send(message.encode())

def close_program():
    socket.socket.close()
    pass

top = tk.Tk()
top.title("Client")
labelHello = tk.Label(top, text = "Input the Server IP", height = 5, width = 22, fg = "black")
labelHello.pack()

entryCd = tk.Entry(top, text = "255.255.255.0") 
entryCd.pack() 

btnCal = tk.Button(top, text = "Send", command = client_program,justify=RIGHT)
btnCal.pack()
btnCal = tk.Button(top, text = "Close", command = close_program,justify=LEFT)
btnCal.pack()

# client_socket = socket.socket()  
# data = client_socket.recv(1024).decode()
# labelHello.config(text="Received from Server: %s " % data)
# if data.lower().strip() == 'quit':
#     socket.socket.close()

top.mainloop()