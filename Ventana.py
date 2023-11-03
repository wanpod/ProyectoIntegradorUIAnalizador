import tkinter as tk
import tkinter.font as font
from frames import *
from menus import *
from orms import *
import inspect
import frames
import inspect


import inspect
import frames


class communicationWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = parent
        self.parent = parent
        self.root = parent
        self.title("Comunicación con el DID")

        self.response_text = ''

        # manejar el cierre de la ventana
        self.protocol("WM_DELETE_WINDOW", self.close_window)
        # para expandir el widget de la lista
        self.grid_columnconfigure(0, weight=1)

        # crear una lista para mostrar la comunicación
        self.listbox = tk.Listbox(self, width=50, height=10)
        self.listbox.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # agregar una barra de desplazamiento
        scrollbar = tk.Scrollbar(self, orient="vertical")
        scrollbar.config(command=self.listbox.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.listbox.config(yscrollcommand=scrollbar.set)

        # agregar un cuadro de texto para ingresar la respuesta del DID
        self.response_entry = tk.Entry(self, width=50)
        self.response_entry.grid(
            row=1, column=0, padx=10, pady=10, sticky="nsew")

        # agregar un botón para enviar la respuesta
        send_button = tk.Button(self, text="Enviar",
                                command=self.send_response)
        send_button.grid(row=1, column=1, padx=10, pady=10)

    def close_window(self):
        # cerrar la ventana y volver a la ventana principal
        self.parent.deiconify()
        self.destroy()

    def clear_list(self):
        # borrar todas las entradas de la lista
        self.listbox.delete(0, tk.END)

    def add_request(self, message):
        # agregar una entrada a la lista con el mensaje enviado al DID
        self.listbox.insert(tk.END, f"Enviado: {message}")

    def add_response(self, message):
        # agregar una entrada a la lista con la respuesta recibida del DID
        self.listbox.insert(tk.END, f"DID: {message}")

    def send_response(self):
        # agregar la respuesta ingresada en el cuadro de texto a la lista de comunicación
        self.response_text = self.response_entry.get()
        self.add_response(self.response_text)
        self.response_entry.delete(0, tk.END)
        self.button_clicked = True

    def wait_for_response(self):
        self.button_clicked = False
        while not self.button_clicked:
            self.root.update()
        return self.response_text


class status():
    def __init__(self, controller):
        self.battery = ''
        self.lineConnection = ''
        self.cancelRequest = False
        self.controller = controller

    def update_status(self):
        answered = False
        self.cancelRequest = False
        while not self.cancelRequest and not answered:
            self.controller.communication_window.add_request(
                "get_lineConnection(True/False)")
            response = self.controller.communication_window.wait_for_response()
            answered = True
            if response.lower() == 'true' or response == '1':
                self.lineConnection = True
            elif response.lower() == 'false' or response == '0':
                self.lineConnection = False
            else:
                answered = False
                self.controller.communication_window.add_request(
                    'Error: se espera un booleano: True/False ó 1/0')

            # Get battery
            if answered:
                answered = False
                self.controller.communication_window.add_request("get_battery")
                response = self.controller.communication_window.wait_for_response()
                try:
                    if 0 <= int(response) <= 100:
                        self.battery = int(response)
                        answered = True
                    else:
                        self.controller.communication_window.add_request(
                            'Error: se espera un entero entre 0 y 100.')
                except:
                    self.controller.communication_window.add_request(
                        'Error: se espera un entero entre 0 y 100.')
                print(response)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(bg='black')
        font.nametofont('TkDefaultFont').configure(size=12, underline=False)
        self.title('AnaDefi v 1.0.0')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.omit = False

        self.mainMenu = barraMenu(self, self)
        self.config(menu=self.mainMenu, width=300, heigh=300)

        mainFrame = tk.Frame(self, bg='yellow')
        mainFrame.grid(padx=0, pady=0, sticky='nsew')

        self.frames = dict()
        self.frame_log = frame_log

        # Crea una lista de todas las clases en el módulo frames
        frame_list = []

        # Obtén todas las clases definidas en el módulo frame.py
        for name, obj in inspect.getmembers(frames, inspect.isclass):
            # Agrega las clases a la lista solo si no son clases internas
            if obj.__module__ == 'frames':
                frame_list.append(obj)

        for frame_class in frame_list:
            frame = frame_class(mainFrame, self)
            self.frames[frame_class] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(frame_log)

        self.communication_window = communicationWindow(self)
        self.status = status(self)

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.at_raise()

    def show_menu(self):
        self.config(menu=self.mainMenu, width=300, heigh=300)

    def omitir_Test(self):
        self.omit = True
        self.communication_window.add_request('Omitir prueba')
        self.status.cancelRequest = True
        self.communication_window.button_clicked = True
        self.show_frame(frame_select_tests)


root = Application()
root.mainloop()
