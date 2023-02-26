import socket
import sys
import binascii
import cliente



class Sujeto:

    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        pass
#### notificar ####
    def notificar(self, *args):
        for observador in self.observadores:
            observador.update(args) # update llama a la rutina de ConcreteObserverA




class Observador:
    def update(self):
        raise NotImplementedError("Delegación de actualización")


class ConcreteObserverA(Observador):
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)


    def update(self, *args):
        print("Actualización dentro de ObservadorConcretoA")
        print("Aquí están los parámetros: ", args)
        return cliente.envio_de_datos(str(args))
