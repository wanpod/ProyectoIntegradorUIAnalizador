from cProfile import label
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from tkinter.ttk import Combobox

# if __name__ == '__main__':
#from frames import *
#from Ventana import *
from orms import *
# else:
#    print('modulo menus importado con éxito')


class barraMenu(tk.Menu):
    def __init__(self, container, controller, *arg, **kwarg):
        super().__init__(container, *arg, **kwarg)

        self.controller = controller
        self.config(bg="white")

        self.barraMenu = tk.Frame(self, bg="white")

        menuInicio = tk.Menu(self, tearoff=0)
        menuInicio.configure(bg="white", activebackground="white")
        menuInicio.add_command(label="Conectar")
        menuInicio.add_command(label="Salir", command=controller.quit)

        menuConectar = tk.Menu(self, tearoff=0)
        menuConectar.configure(bg="white", activebackground="white")
        menuConectar.add_command(label="Conexión bluetooth")

        ayudaMenu = tk.Menu(self, tearoff=0)
        ayudaMenu.configure(bg="white", activebackground="white")
        ayudaMenu.add_command(label="Licencia")
        ayudaMenu.add_command(label="Acerca de...")

        self.menuSession = tk.Menu(self, tearoff=0)
        self.menuSession.configure(bg="white", activebackground="white")
        self.menuSession.add_command(label='Cuenta')
        self.menuSession.add_command(label='Clientes')
        self.menuSession.add_command(label='Equipos')
        self.menuSession.add_separator()
        self.menuSession.add_command(
            label='Iniciar sesión', command=self.close_session, state='disabled')

        self.add_cascade(label="Inicio", menu=menuInicio)
        self.add_cascade(label="Conectar", menu=menuConectar)
        self.add_cascade(label="Ayuda", menu=ayudaMenu)
        self.insert_separator
        self.add_cascade(label='Sesión', menu=self.menuSession)

    def at_raise(self):
        self.tkraise()

    def refreshSessionMenu(self):
        db = SqliteDatabase('interfaz\\DataBase.db')
        db.connect
        session = Session.get(Session.session_id == 1)
        print('@' + session.user)
        db.close
        if session.user == '':
            self.entryconfigure(4, label="Sesión")
            self.menuSession.entryconfigure(0,
                                            state='disabled')
            self.menuSession.entryconfigure(1,
                                            state='disabled')
            self.menuSession.entryconfigure(2,
                                            state='disabled')
            self.menuSession.entryconfigure(4, label='Iniciar sesión',
                                            state='normal')
        else:
            self.entryconfigure(4, label='@' + session.user)
            self.menuSession.entryconfigure(0,
                                            state='normal')
            self.menuSession.entryconfigure(1,
                                            state='normal')
            self.menuSession.entryconfigure(2,
                                            state='normal')
            self.menuSession.entryconfigure(4, label='Cerrar sesión',
                                            state='normal')

    def close_session(self):
        self.controller.show_frame(self.controller.frame_log)
        self.refreshSessionMenu()
