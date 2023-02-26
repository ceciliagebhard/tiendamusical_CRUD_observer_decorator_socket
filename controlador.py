from tkinter import Tk
import vista
import observador

####################
# CONTROLADOR

class Controller:
    
    def __init__(self, root):
        self.root_controller=root
        self.objeto_vista=vista.Mivista(self.root_controller)
        self.el_observador = observador.ConcreteObserverA(self.objeto_vista.objeto_base)
            
if __name__ =="__main__":
    root = Tk()
    Controller(root)
    root.mainloop()
