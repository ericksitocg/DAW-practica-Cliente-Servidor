import socket

mi_socket = socket.socket()#socket con valores por defecto
mi_socket.bind(("localhost",8002))#tupla (direccion de host, puerto)
mi_socket.listen(5)#Cuantas peticiones puede manejar en cola el socket

n_solicitudes = 0
while True:#siempre escuchando
	print("\n----------------------------")
	conexion, addr = mi_socket.accept()#aceptamos las peticiones del cliente
	
	n_solicitudes+=1
	print("Nueva conexion establecida, solicitud %d"%n_solicitudes)
	print(addr)

	peticion = conexion.recv(1024).decode()#recibo la solititud del cliente
	print(peticion)
	
	mensaje = "Hola,soy la respuesta desde el servidor para el cliente %s"%peticion[-1]

	conexion.send(mensaje.encode())#Envio una respuesta al cliente
	conexion.close()
	print("----------------------------")