from tkinter import *
from tkinter.messagebox import *
import sqlite3
from tkinter import ttk
import re
from tkinter import Label
from tkinter import messagebox
from random import choice
from peewee import *
import datetime
import queue
import socket
from observador import Sujeto


####################
# MODELO

# conexion a la base de datos

db = SqliteDatabase("mi_base_peewee2.db")

class BaseModel(Model):
    class Meta:
        database = db

##### Decoradores alta, baja y modificar

def aviso(funcion):
    def inner(*args, **kwargs):
        
        print(datetime.date.today())
        print("Se acaba de ejecutar el %s" %funcion.__name__)
        if funcion.__name__ == "alta":
            mi_fecha=datetime.datetime.now()
            mi_nombre=funcion.__name__
            for valor in args:
                #print(valor)

                mi_texto= str(mi_fecha) + "," + mi_nombre + str(valor)
                mi_texto = mi_texto + "\n"
                archivo=open("disqueriaregistro.txt", "a")
                archivo.write(mi_texto)
                archivo.close
                

        elif funcion.__name__ == "modificar":
            mi_fecha=datetime.datetime.now()
            mi_nombre=funcion.__name__
            for valor in args:
                print(valor)
                # print(type(valor))
                mi_texto= str(mi_fecha) + "," + mi_nombre + str(valor)
                mi_texto = mi_texto + "\n"
                archivo=open("disqueriaregistro.txt", "a")
                archivo.write(mi_texto)
                archivo.close
        elif funcion.__name__ == "baja":
            mi_fecha=datetime.datetime.now()
            mi_nombre=funcion.__name__
            for valor in args:
                #print(valor)
                print("1----", args)
                print("Artista:", args[1].item(args[2])['values'][0])
                print("Album:", args[1].item(args[2])['values'][1])
                mi_texto= str(mi_fecha) + "," + mi_nombre + str(valor)
                mi_texto = mi_texto + "\n"
                archivo=open("disqueriaregistro.txt", "a")
                archivo.write(mi_texto)
                archivo.close
                        
                
        else: pass
        return funcion(*args, **kwargs)
        
    return inner
    


    




# the user model specifies its fields (or columns) declaratively, like django
class Discografica(BaseModel):
    artista = CharField(unique=False)
    album = CharField()
    unidades= IntegerField()
    valor = IntegerField()
    
db.connect()
db.create_tables([Discografica])

class Abmc(Sujeto):
    
    def __init__(
        self, 
    ): pass

    

    @aviso
    def alta(self, artista, album, unidades, valor, tree):
        cadena = artista
        patron = "[a-zA-Záéíóú 0-9 \s]+" #regex que valida campo de entrada artista tolerando varios espacios, entre caracteres alfanúmericos
        cadena2 = unidades
        if cadena2 < 0:
            messagebox.showinfo(title="Error",
                message="Valor no permitido, introduzca un número positivo")
            raise Exception("Valor no permitido, introduzca un número positivo")
            # excepción que impide el alta si se ingresa un número negativo en el item unidades
        if re.match(patron, cadena):
            print(artista, album, unidades, valor)
        
            discografica=Discografica()
            discografica.artista=artista
            discografica.album=album
            discografica.unidades=unidades
            discografica.valor=valor
            discografica.save() 
            self.actualizar_treeview(tree)
            print("Item ingresado exitosamente a la base de datos")
            messagebox.showinfo(title="Enhorabuena", message="Item ingresado exitosamente a la base de datos")
            ##### NOTIFICAR ####
            self.notificar(artista, album, unidades, valor)

        else:
            print("Error en campo Artista")
            messagebox.showinfo(title="Error", message="Error en campo Artista, ingrese nuevamente")


    def consulta(self, tree): 
        self.actualizar_treeview(tree)

    
    def actualizar_treeview(self, mitreview):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)
        
        for fila in Discografica.select():
            mitreview.insert("", 0, text=fila.id, values=(fila.artista, fila.album, fila.unidades, fila.valor))


    @aviso

    def baja(self, tree, *args):
        valor = tree.selection()
        item = tree.item(valor)
        ##### observador notificar
        self.notificar(item)
        mi_id = item['text']
        item_seleccionado = tree.focus()
        mi_id = tree.item(item_seleccionado)
        borrar=Discografica.get(Discografica.id==mi_id["text"])
        borrar.delete_instance()
        
        

        print("Item dado de baja")
        messagebox.showinfo(title="Enhorabuena!", message="Item eliminado con éxito")
        self.actualizar_treeview(tree)
        # tree.delete(valores)
    

    @aviso
    def modificar(self, artista, album, unidades, valor, tree):
        valores = tree.selection()
        print(valores)
        item = tree.item(valores)
        listaparasocket=queue.Queue() #LIFO queue class
        argumentos = [artista, album, unidades, valor]
        for x in argumentos:
            listaparasocket.put(x)
            print(listaparasocket.get(), argumentos, "se acaba de realizar una actualización de la siguiente informacion, información en queue", end="\t")
        print(item)
        print(item["text"])
        mi_id = item["text"]
        actualizar=Discografica.update(artista=artista, album=album, unidades=unidades, valor=valor).where(Discografica.id==mi_id)
        actualizar.execute()
        print("Item modificado")
        messagebox.showinfo(title="Enhorabuena!", message="Item modificado con éxito")
        self.actualizar_treeview(tree)
        #### observador notificar
        self.notificar(artista, album, unidades, valor)
