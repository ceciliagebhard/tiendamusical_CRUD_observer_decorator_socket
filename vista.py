from tkinter import Tk
from tkinter import StringVar
from tkinter import IntVar
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import N
from tkinter import W
from tkinter import E
from tkinter.colorchooser import askcolor
import random
#from tkinter import *
from tkinter.messagebox import *
#import sqlite3
from tkinter import ttk
#import re
from modelo import Abmc
from random import choice

####################
# VISTA

class Mivista(): 

    def __init__ (self, window): 
        self.root = window
        self.root.config(bg="#494C59")
        self.root.title("Tienda de música")
        self.root.resizable(width=300, height=200)
        self.objeto_base=Abmc()



        self.titulo = Label(
            self.root,
            text="Hola! Ingrese artista, album, unidades y valor del producto",
            bg="DarkSlateBlue",
            fg="thistle1",
            height=1,
            width=60,
        )
        self.titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky= W + E)

        self.var_artista, self.var_album, self.var_unidades, self.var_valor = (
            StringVar(),
            StringVar(),
            IntVar(),
            IntVar(),
        )

        self.artista = Label(
            self.root,
            text="Artista",
            borderwidth=2,
            relief="groove",
            foreground="white",
            background="#6666E6",
            width=10,
        )
        self.artista.grid(row=1, column=0, sticky=W)
        self.album = Label(
            self.root,
            text="Album",
            borderwidth=2,
            relief="groove",
            foreground="white",
            background="#6666E6",
            width=10,
        )
        self.album.grid(row=2, column=0, sticky=W)
        self.unidades = Label(
            self.root,
            text="Unidades",
            borderwidth=2,
            relief="groove",
            foreground="white",
            background="#6666E6",
            width=10,
        )
        self.unidades.grid(row=3, column=0, sticky=W)
        self.valor = Label(
            self.root,
            text="Valor",
            borderwidth=2,
            relief="groove",
            foreground="white",
            background="#6666E6",
            width=10,
        )
        self.valor.grid(row=4, column=0, sticky=W)
        

        ####################
        # entry
        self.entry_artista = Entry(
            self.root,
            textvariable=self.var_artista,
            width=35,
            background="#8B9DC3",
            foreground="white",
        )
        self.entry_artista.grid(row=1, column=1)
        self.entry_album = Entry(
            self.root,
            textvariable=self.var_album,
            width=35,
            background="#8B9DC3",
            foreground="white",
        )
        self.entry_album.grid(row=2, column=1)
        self.entry_unidades = Entry(
            self.root,
            textvariable=self.var_unidades,
            width=35,
            background="#8B9DC3",
            foreground="white",
        )
        self.entry_unidades.grid(row=3, column=1)
        self.entry_valor = Entry(
            self.root,
            textvariable=self.var_valor,
            width=35,
            background="#8B9DC3",
            foreground="white",
        )
        self.entry_valor.grid(row=4, column=1)

        ####################
        # treeview
        
        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("col1", "col2", "col3", "col4")
        self.tree.column("#0", minwidth=50, anchor=W)
        self.tree.heading("#0", text="ID")
        self.tree.column("col1", minwidth=60, anchor=W)
        self.tree.heading("col1", text="Artista")
        self.tree.column("col2", minwidth=60, anchor=W)
        self.tree.heading("col2", text="Album")
        self.tree.column("col3", minwidth=20, anchor=W)
        self.tree.heading("col3", text="Unidades")
        self.tree.column("col4", minwidth=30, anchor=W)
        self.tree.heading("col4", text="Valor")
        self.tree.grid(column=0, row=10, columnspan=4)

    #################
    # botones
    
        def cambiar_color(self, ):
            hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
            color_code = '#'
            color_code = color_code + choice(hex_chars)
            color_code = color_code + choice(hex_chars)
            color_code = color_code + choice(hex_chars)
            color_code = color_code + choice(hex_chars)
            color_code = color_code + choice(hex_chars)
            color_code = color_code + choice(hex_chars)
            print('El color hexagecimal generado es:', color_code)
            self.root.config(bg=color_code)

    
        self.boton_g = Button(
            self.root,
            text="Agregar",
            command=lambda: self.objeto_base.alta(
                self.var_artista.get(), self.var_album.get(), self.var_unidades.get(), self.var_valor.get(), self.tree
        ),
            borderwidth=2,
            relief="groove",
            foreground="black",
            background="#6666E6",
        )
        self.boton_g.grid(row=6, column=0)
        
        self.boton_e = Button(
            self.root,
            text="Eliminar",
            command=lambda: self.objeto_base.baja(self.tree, self.tree.selection()),
            borderwidth=2,
            relief="groove",
            foreground="black",
            background="#6666E6",
        )
        self.boton_e.grid(row=6, column=1)
        self.boton_m = Button(
            self.root,
            text="Modificar",
            command=lambda: self.objeto_base.modificar(
                self.var_artista.get(), self.var_album.get(), self.var_unidades.get(), self.var_valor.get(), self.tree
            ),
            borderwidth=2,
            relief="groove",
            foreground="black",
            background="#6666E6",
        )
        self.boton_m.grid(row=6, column=2)
        
        self.boton_v = Button(
            self.root,
            text="Ver",
            command=lambda: self.objeto_base.consulta(self.tree),
            borderwidth=2,
            relief="groove",
            foreground="black",
            background="#6666E6",
        )
        self.boton_v.grid(row=6, column=3)
        
        self.boton_sorpresa = Button(
            self.root,
            text="Sorpresa",
            command=lambda: cambiar_color(self,),
            borderwidth=2,
            relief="groove",
            foreground="black",
            background="#6666E6", 
        )
        self.boton_sorpresa.grid(row=6, column=4)
