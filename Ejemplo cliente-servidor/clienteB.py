import socket

mi_socket = socket.socket()
mi_socket.connect(("localhost",8002))#recibe tupla (direccion a conectar,puerto que vamos a usar)
print("----------------------------")
#envia mensaje al servidor
mi_socket.send("Hola, soy una solicitud desde el cliente B".encode()	)#Usamos encode para enviar
#recibe mensaje del servidor
respuesta = mi_socket.recv(1024).decode()#1024 hace refercnia al buffer usamos decode para recibir

print(respuesta)
mi_socket.close()
print("----------------------------")