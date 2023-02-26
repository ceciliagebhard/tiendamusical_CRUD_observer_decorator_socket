import socket
import binascii
import queue
import time


def envio_de_datos(args):
    UDP_IP = 'localhost'
    UDP_PORT = 8003
    
    
    mi_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # mi_socket.send(str.encode("Información desde el cliente: "), (UDP_IP, UDP_PORT))
    q = queue.Queue()
    
    # infonueva = str(args)
    # for x in infonueva: # envio de data mediante socket

    q.put(args)
    q.get('utf-8')
        #infoenviada=str(x[1:])
        # infoenviada=''.join((x[1:]).encode('UTF-8'))

    mi_socket.connect(("192.168.0.10",UDP_PORT))
        # mi_socket.send(infoenviada.encode("UTF-8"))
    mi_socket.send(str.encode(args))
    # recibido = mi_socket.recv(1024) # De momento la app en mac osx se congela y no ejecuta correctamente el CRUD
    # mi_socket.close()               # por este motivo fueron comentadas estas últimas líneas del script que permiten recibir datos en el mismo código
    # print(recibido)                 # por ahora funciona correctamente enviando información externamente a otras app
            
