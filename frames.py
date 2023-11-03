import tkinter as tk
from tkinter import ttk, BooleanVar, StringVar
import tkinter.font as font
from tkinter.ttk import Combobox
from tkinter.messagebox import showinfo
from turtle import color
from CalculateEnergy import Get_Energy


# if __name__ == '__main__':
from orms import *
#from menus import *
#from Ventana import *

import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class frame_log(tk.Frame):
    def __init__(self, container, controller, *arg, **kwarg):
        super().__init__(container, *arg, **kwarg)

        self.controller = controller

        # ------------------------------------CAMPOS------------------------------------------
        frameCampos = tk.Frame(self)
        frameCampos.grid(row=0, column=0, sticky='nsew', padx=0, pady=0)

        labelUsuario = tk.Label(frameCampos, text='Usuario:')
        labelPass = tk.Label(frameCampos, text='Contraseña:')
        labelUsuario.grid(row=0, column=0, sticky="e", padx=10, pady=10)
        labelPass.grid(row=1, column=0, sticky='e', padx=10, pady=0)

        self.labelWarning = tk.Label(frameCampos, font=('Arial', 10))
        self.labelWarning.grid(
            row=2, column=0, columnspan=2, sticky='w', padx=10, pady=10)

        # entryUsuario=tk.StringVar()
        # entryPass=tk.StringVar()

        # ,textvariable=entryUsuario)
        self.cuadroUsuario = tk.Entry(frameCampos)
        self.cuadroUsuario.grid(row=0, column=1, sticky='e', padx=10, pady=10)

        self.cuadroPass = tk.Entry(frameCampos)  # , textvariable=entryPass)
        self.cuadroPass.config(show='*')
        self.cuadroPass.grid(row=1, column=1, sticky='e', padx=10, pady=0)

        # ------------------------------------BOTONES------------------------------------------
        frameBotones = tk.Frame(self)
        frameBotones.grid(row=0, column=1, sticky='e', padx=20, pady=0)

        botonIngresar = tk.Button(
            frameBotones, text='Ingresar', width=17, command=self.log_in)
        botonIngresar.grid(row=0, column=0, sticky='w', padx=10, pady=10)
        botonCrearCuenta = tk.Button(
            frameBotones, text='Crear Cuenta', command=lambda: controller.show_frame(frame_new_user))
        botonCrearCuenta.grid(row=0, column=1, sticky='w', padx=15, pady=10)
        botonOlvideContrasena = tk.Button(
            frameBotones, text='Olvidé mi contraseña', width=17)
        botonOlvideContrasena.grid(
            row=1, column=0, sticky='w', padx=10, pady=0)
        botonTesteoRapido = tk.Button(frameBotones, text='Testeo rápido',
                                      width=17, command=lambda: controller.show_frame(frame_client))
        botonTesteoRapido.grid(row=2, column=0, sticky='w', padx=10, pady=50)

    def at_press_enter(self):
        # if self.focus_get() =
        print(self.focus_get())

    def at_raise(self):
        self.tkraise()
        self.controller.bind('<Return>', self.at_press_enter)
        self.controller.bind('<KP_Enter>', self.at_press_enter)
        Session.update(user='', client='', brand='', modelo='').where(
            Session.session_id == 1).execute()
        self.cuadroUsuario.delete(0, 'end')
        self.cuadroPass.delete(0, 'end')
        self.cuadroUsuario.focus()
        self.labelWarning['text'] = ''
        self.controller.mainMenu.entryconfigure(
            4, label='Sesión', state='disabled')

    def log_in(self):
        db = SqliteDatabase('interfaz\\DataBase.db')
        db.connect
        name = self.cuadroUsuario.get()
        password = self.cuadroPass.get()
        try:
            user = User.get(User.name == name)
            if user.password == password:
                Session.update(user=name).where(
                    Session.session_id == 1).execute()
                self.controller.mainMenu.refreshSessionMenu()
                self.controller.show_frame(frame_client)
            else:
                self.labelWarning['text'] = 'contraseña incorrecta'
        except:
            self.labelWarning['text'] = 'Nombre de usuario ó contraseña incorrecto'
        db.close


class frame_new_user(tk.Frame):
    def __init__(self, container, controller, *arg, **kwarg):
        super().__init__(container, *arg, **kwarg)

        self.frameController = controller

        # ------------------------------------CAMPOS------------------------------------------
        frameCampos = tk.Frame(self)
        frameCampos.grid(row=0, column=0, sticky='nsew', padx=0, pady=0)

        labelUser = tk.Label(frameCampos, text='Usuario:')
        labelEmail = tk.Label(frameCampos, text='Email')
        labelPassword = tk.Label(frameCampos, text='Contraseña:')
        laberAsteriskUser = tk.Label(frameCampos, text='*', fg='red')
        laberAsteriskEmail = tk.Label(frameCampos, text='*', fg='red')
        laberAsteriskPassword = tk.Label(frameCampos, text='*', fg='red')
        labelUser.grid(row=0, column=0, sticky='e', padx=10, pady=0)
        labelEmail.grid(row=1, column=0, sticky='e', padx=10, pady=0)
        labelPassword.grid(row=2, column=0, sticky='e', padx=10, pady=0)
        laberAsteriskUser.grid(row=0, column=2, sticky='w', padx=0, pady=0)
        laberAsteriskEmail.grid(row=1, column=2, sticky='w', padx=0, pady=0)
        laberAsteriskPassword.grid(row=2, column=2, sticky='w', padx=0, pady=0)

        self.labelWarning = tk.Label(frameCampos, font=('Arial', 10))
        self.labelWarning.grid(
            row=3, column=0, columnspan=3, sticky='w', padx=10, pady=10)

        self.EntryUser = tk.Entry(frameCampos, width=30, )
        self.EntryUser.grid(row=0, column=1, sticky='e', padx=10, pady=0)

        self.EntryEmail = tk.Entry(frameCampos, width=30)
        self.EntryEmail.grid(row=1, column=1, sticky='e', padx=10, pady=0)

        self.EntryPassword = tk.Entry(frameCampos, width=30, )
        self.EntryPassword.config(show='*')
        self.EntryPassword.grid(row=2, column=1, sticky='e', padx=10, pady=0)

        # ------------------------------------BOTONES------------------------------------------
        frameBotones = tk.Frame(self)
        frameBotones.grid(row=1, column=0, sticky='ws', padx=0, pady=0)

        ButtonSave = tk.Button(frameBotones, text='Guardar',
                               width=17, command=self.save)
        ButtonSave.grid(row=0, column=0, sticky='s', padx=10, pady=5)
        ButtonCancel = tk.Button(frameBotones, text='Cancelar',
                                 width=17, command=lambda: controller.show_frame(frame_log))
        ButtonCancel.grid(row=0, column=1, sticky='s', padx=15, pady=5)

        self.buttonForgotMyPassword = tk.Button(
            frameBotones, text='Olvide mi contraseña', width=20)
        self.buttonForgotMyPassword.grid(
            row=2, column=0, columnspan=2, sticky='w', padx=10, pady=5)
        self.buttonForgotMyPassword.grid_remove()

        self.buttonForgotMyUser = tk.Button(
            frameBotones, text='Olvide mi nombre de usuario', width=25)
        self.buttonForgotMyUser.grid(
            row=2, column=0, columnspan=2, sticky='w', padx=10, pady=5)
        self.buttonForgotMyUser.grid_remove()

    def at_raise(self):
        self.tkraise()
        self.labelWarning['text'] = ''
        self.EntryUser.focus()

    def save(self):
        name = self.EntryUser.get()
        email = self.EntryEmail.get()
        password = self.EntryPassword.get()

        if name == '':
            self.labelWarning['text'] = 'El nombre de usuario es obligatorio.'
            return
        if email == '':
            self.labelWarning['text'] = 'El el email es obligatorio.'
            return
        if password == '':
            self.labelWarning['text'] = 'Ingrese una contraseña válida.'
            return

        db = SqliteDatabase('interfaz\\DataBase.db')
        db.connect
        try:
            User.get(User.name == name)
            self.labelWarning['text'] = 'El nombre de usuario ya exixte.'
            self.buttonForgotMyUser.grid_remove()
            self.buttonForgotMyPassword.grid()
            db.close
            return
        except:
            pass

        try:
            User.get(User.email == email)
            self.labelWarning['text'] = 'El email ingresado ya pertenece a otra cuenta.'
            self.buttonForgotMyPassword.grid_remove()
            self.buttonForgotMyUser.grid()
            db.close
            return
        except:
            pass

        User.create(name=name, email=email, password=password)
        db.close
        self.frameController.show_frame(frame_log)


class frame_client(tk.Frame):

    def __init__(self, container, controller, *arg, **kwarg):
        super().__init__(container, *arg, **kwarg)

        self.controller = controller

        # ------------------------------------FIELDS------------------------------------------
        frameCampos = tk.Frame(self)
        frameCampos.grid(row=0, column=0, sticky='nsew', padx=0, pady=0)

        labelClient = tk.Label(frameCampos, text='Cliente:')
        labelClient.grid(row=0, column=0, sticky='e', padx=10, pady=20)
        labelBrand = tk.Label(frameCampos, text='Marca:')
        labelBrand.grid(row=1, column=0, sticky='e', padx=10, pady=10)
        labelModel = tk.Label(frameCampos, text='Modelo:')
        labelModel.grid(row=2, column=0, sticky='e', padx=10, pady=0)

        self.boxClient = ttk.Combobox(frameCampos)
        self.boxClient.grid(row=0, column=1, sticky='e', padx=10, pady=20)
        self.boxClient.bind('<<ComboboxSelected>>', self.select_client)

        self.boxBrand = Combobox(frameCampos)  # ,, textvariable=entryMarca)
        self.boxBrand.grid(row=1, column=1, sticky='e', padx=10, pady=10)
        self.boxBrand.bind('<<ComboboxSelected>>', self.select_brand)

        self.boxModel = Combobox(frameCampos)  # ,, textvariable=entryModelo)
        self.boxModel.grid(row=2, column=1, sticky='e', padx=10, pady=0)

        # ------------------------------------BUTTONS------------------------------------------
        frameButtons = tk.Frame(self)
        frameButtons.grid(row=0, column=1, sticky='e', padx=20, pady=0)

        buttonNewClient = tk.Button(frameButtons, text='Agregar nuevo cliente',
                                    width=20, command=lambda: controller.show_frame(frame_new_client))
        buttonNewClient.grid(row=1, column=0, sticky='w', padx=10, pady=20)
        buttonTest = tk.Button(frameButtons, text='Testear',
                               width=17, command=lambda: controller.show_frame(frame_select_tests))
        buttonTest.grid(row=2, column=0, sticky='w', padx=10, pady=90)

    def select_client(self, *args):
        self.boxBrand.set('')
        self.boxModel.set('')
        self.boxBrand.focus()

        db = SqliteDatabase('interfaz\\DataBase.db')
        db.connect

        client = self.boxClient.get()
        Session.update(client=client).where(Session.session_id == 1).execute()

        brandsList = []

        brands = Brand.select()
        for brand in brands:
            brandsList.append(brand.name)
        db.close
        self.boxBrand['values'] = brandsList

    def select_brand(self, *args):
        self.boxModel.focus()
        self.boxModel.set('')

        db = SqliteDatabase('interfaz\\DataBase.db')
        db.connect

        brand = self.boxBrand.get()
        Session.update(brand=brand).where(Session.session_id == 1).execute()

        modelsList = []

        for model in Modelo.select().where(Modelo.brand == brand):
            modelsList.append(model.name)
        db.close
        self.boxModel['values'] = modelsList

    def at_raise(self):
        self.tkraise()

        self.boxClient.delete(0, 'end')
        self.boxClient.delete(0, 'end')

        db = SqliteDatabase('DataBase.db')
        db.connect

        session = Session.get(Session.session_id == 1)

        clientList = []
        for client in Client.select().where(Client.user == session.user):
            clientList.append(client.name)

        db.close
        self.boxClient['values'] = clientList
        self.controller.mainMenu.refreshSessionMenu()
        self.controller.mainMenu.entryconfigure(4, state='normal')


class frame_new_client(tk.Frame):
    def __init__(self, container, controller, *arg, **kwarg):
        super().__init__(container, *arg, **kwarg)

        self.frameController = controller

        # ------------------------------------FIELDS------------------------------------------
        frameFields = tk.Frame(self)
        frameFields.grid(row=0, column=0, sticky="nsew", padx=10, pady=0)

        labelCliente = tk.Label(frameFields, text="Nuevo cliente:")
        labelCliente.grid(row=0, column=0, sticky="e", padx=10, pady=20)

        self.entryClient = tk.Entry(frameFields)
        self.entryClient.grid(row=0, column=1, sticky="e", padx=10, pady=20)

        self.labelWarning = tk.Label(frameFields, font=('Arial', 10))
        self.labelWarning.grid(
            row=3, column=0, columnspan=3, sticky='w', padx=10, pady=10)
        # ------------------------------------BUTTONS------------------------------------------
        frameButtos = tk.Frame(self)
        frameButtos.grid(row=2, column=1, sticky="e", padx=20, pady=100)

        buttonSave = tk.Button(frameButtos, text="Guardar",
                               width=17, command=lambda: self.save())
        buttonSave.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        buttonCancel = tk.Button(frameButtos, text="Cancelar", width=17,
                                 command=lambda: controller.show_frame(frame_client))
        buttonCancel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

    def save(self):
        name = self.entryClient.get()

        if name == '':
            self.labelWarning['text'] = "El nombre de cliente es obligatorio."
            return

        db = SqliteDatabase('interfaz\\DataBase.db')
        db.connect

        session = Session.get(Session.session_id == 1)

        try:
            Client.get((Client.name == name) & (Client.user == session.user))
            self.labelWarning['text'] = "El cliente ya existe."
            db.close
            return
        except:
            pass

        Client.create(name=name, user=session.user)
        db.close
        self.frameController.show_frame(frame_client)

    def at_raise(self):
        self.tkraise()
        self.labelWarning['text'] = ''
        self.entryClient.delete(0, 'end')
        self.entryClient.delete(0, 'end')
        self.entryClient.focus()


class frame_select_tests(tk.Frame):

    def __init__(self, container, controller, *arg, **kwarg):
        super().__init__(container, *arg, **kwarg)

        self.controller = controller

        # ------------------------------------CAMPOS------------------------------------------
        frameCampos = tk.Frame(self)
        frameCampos.grid(row=0, column=0, sticky="nsew", padx=10, pady=0)

        self.check_energia_de_carga = BooleanVar()
        check_energia_de_carga = tk.Checkbutton(frameCampos,
                                                variable=self.check_energia_de_carga, onvalue=True, offvalue=False)
        check_energia_de_carga.grid(
            row=0, column=0, sticky="w", padx=0, pady=0)

        self.check_Tiempo_de_carga = BooleanVar()
        check_Tiempo_de_carga = tk.Checkbutton(frameCampos,
                                               variable=self.check_Tiempo_de_carga, onvalue=True, offvalue=False)
        check_Tiempo_de_carga.grid(row=1, column=0, sticky="w", padx=0, pady=0)

        self.check_Retardo = BooleanVar()
        check_Retardo = tk.Checkbutton(frameCampos,
                                       variable=self.check_Retardo, onvalue=True, offvalue=False)
        check_Retardo.grid(row=2, column=0, sticky="w", padx=0, pady=0)

        self.check_Numero_de_cargas = BooleanVar()
        check_Numero_de_cargas = tk.Checkbutton(frameCampos,
                                                variable=self.check_Numero_de_cargas, onvalue=True, offvalue=False)
        check_Numero_de_cargas.grid(
            row=3, column=0, sticky="w", padx=0, pady=0)

        self.check_Señales_de_ECG = BooleanVar()
        check_Señales_de_ECG = tk.Checkbutton(frameCampos,
                                              variable=self.check_Señales_de_ECG, onvalue=True, offvalue=False)
        check_Señales_de_ECG.grid(row=4, column=0, sticky="w", padx=0, pady=0)

        self.check_DEA = BooleanVar()
        check_DEA = tk.Checkbutton(frameCampos,
                                   variable=self.check_DEA, onvalue=True, offvalue=False)
        check_DEA.grid(row=5, column=0, sticky="w", padx=0, pady=0)

        self.check_Calibracion_interna = BooleanVar()
        check_Calibracion_interna = tk.Checkbutton(frameCampos,
                                                   variable=self.check_Calibracion_interna, onvalue=True, offvalue=False)
        check_Calibracion_interna.grid(
            row=6, column=0, sticky="w", padx=0, pady=0)

        label_Energia_de_Carga = tk.Label(
            frameCampos, text="Secuencia de energía de carga")
        label_Energia_de_Carga.grid(
            row=0, column=1, sticky="w", padx=0, pady=0)
        label_Tiempo_de_carga = tk.Label(frameCampos, text="Tiempo de carga")
        label_Tiempo_de_carga.grid(row=1, column=1, sticky="w", padx=0, pady=0)
        label_Retardo = tk.Label(frameCampos, text="Retardo")
        label_Retardo.grid(row=2, column=1, sticky="w", padx=0, pady=0)
        label_Numero_de_cargas = tk.Label(
            frameCampos, text="Número de cargas a máxima energía con batería")
        label_Numero_de_cargas.grid(
            row=3, column=1, sticky="w", padx=0, pady=0)
        label_Señales_de_ECG = tk.Label(frameCampos, text="Señales de ECG")
        label_Señales_de_ECG.grid(row=4, column=1, sticky="w", padx=0, pady=0)
        label_DEA = tk.Label(frameCampos, text="DEA")
        label_DEA.grid(row=5, column=1, sticky="w", padx=0, pady=0)
        label_Calibracion_interna = tk.Label(
            frameCampos, text="Calibracion interna del AnaDefi")
        label_Calibracion_interna.grid(
            row=6, column=1, sticky="w", padx=0, pady=0)

        # ------------------------------------WARNING LABEL------------------------------------------
        frame_Warning = tk.Frame(self)
        frame_Warning.grid(row=1, column=0, sticky="nsew", padx=10, pady=20)

        self.labelWarning = tk.Label(
            frame_Warning, text='Verificando batería y conexión a linea...')
        self.labelWarning.grid(row=0, column=0, sticky="w", padx=0, pady=0)

        # ------------------------------------BOTONES------------------------------------------
        frameBotones = tk.Frame(self)
        frameBotones.grid(row=2, column=1, sticky="e", padx=20, pady=0)

        self.boton_test = tk.Button(frameBotones, text="Testear", width=17,
                                    command=self.get_tests_list)
        #self.boton_test.grid(row=0, column=0, sticky="w", padx=10, pady=50)

    def at_raise(self):
        self.tkraise()
        self.boton_test.grid_remove()
        self.labelWarning['text'] = 'Verificando batería y conexión a linea...'
        self.labelWarning.grid()
        self.DID_status_update()

    def DID_status_update(self):
        self.controller.status.update_status()

        if 0 <= self.controller.status.battery <= 20:
            self.labelWarning['text'] = 'Para iniciar la prueba la bateria del analizador debe ser superior al 20%.'
            try:
                self.boton_test.grid_remove()

            except:
                pass
            self.DID_status_update()
        else:
            if not self.controller.status.lineConnection:
                self.labelWarning['text'] = ''
                try:
                    self.boton_test.grid()
                except:
                    pass
            else:
                self.labelWarning['text'] = 'Desconecte el cargador del analizador para iniciar la prueba.'
                try:
                    self.boton_test.grid_remove()

                except:
                    pass
                self.DID_status_update()

    def get_tests_list(self):
        tests = {}
        tests = {frame_charge_energy_sequence_test: self.check_energia_de_carga,
                 test_empty1: self.check_Tiempo_de_carga,
                 test_empty2: self.check_Retardo,
                 test_empty3: self.check_Numero_de_cargas,
                 test_empty4: self.check_Señales_de_ECG,
                 test_empty5: self.check_DEA,
                 test_empty6: self.check_Calibracion_interna,
                 }

        for test in tests.values():
            if test.get():
                test.set(False)
                self.controller.show_frame(
                    list(tests.keys())[list(tests.values()).index(test)])
                break


class frame_charge_energy_sequence_test(tk.Frame):
    def __init__(self, container, controller, *arg, **kwarg):
        super().__init__(container, *arg, **kwarg)

        self.controller = controller

        # ------------------------------------CAMPOS------------------------------------------
        frameFields = tk.Frame(self)
        frameFields.grid(row=0, column=0, sticky="nsew", padx=10, pady=0)

        self.labelInstruction = tk.Label(frameFields, text="")
        self.labelInstruction.grid(row=0, column=0, sticky="w", padx=0, pady=0)

        # ------------------------------------BOTONES------------------------------------------
        frameButtons = tk.Frame(self)
        frameButtons.grid(row=1, column=0, sticky="w", padx=20, pady=0)

        button_omit_test = tk.Button(frameButtons, text="Omitir prueba", width=17,
                                     command=self.controller.omitir_Test)  # self.controller.omitir_Test(frame_select_tests))  #
        button_omit_test.grid(row=0, column=1, sticky="e", padx=10, pady=50)

        self.button_done = tk.Button(
            frameButtons, text="Listo", width=17, command=lambda: self.next_step())
        self.button_done.grid(row=0, column=0, sticky="e", padx=10, pady=50)

    def at_raise(self):
        self.tkraise()
        self.button_done.grid()
        showinfo(message='No conecte el analizador al tomacorriente durante la prueba.',
                 title='Advertencia')
        self.step = 0
        # Indicamos al DID que inicie la prueba:
        self.controller.communication_window.add_request(
            'iniciar prueba de secuencia de energia de carga')
        self.next_step()

    #def energies_by_model(self):
    #    modelID = 'orm_'
    #    for energy in orm_energias():
    #        self.energy = energy
    #        self.step = 0
    #        self.next_step()
    #    self.controller.show_frame(frame_show_data_results)

    def next_step(self):
        self.step = self.step + 1

        if self.step == 1:
            Energy = '10 Joules'
            mensaje = 'Seleccione en desfibrilador energía' + Energy
            self.labelInstruction['text'] = mensaje

        elif self.step == 2:
            mensaje = 'Coloque las paletas en electrodos apex y esterón'
            self.labelInstruction['text'] = mensaje

        elif self.step == 3:
            mensaje = 'Presione en el desfibrilador el botón "CARGA"'
            self.labelInstruction['text'] = mensaje

        elif self.step == 4:
            try:
                self.button_done.grid_remove()
            except:
                pass

            mensaje = 'Esperando confirmacion del DID...'
            self.labelInstruction['text'] = mensaje

            DIDconfirmation = False
            while DIDconfirmation == False and self.controller.omit == False:
                self.controller.communication_window.add_request(
                    'Descarga inminente. Confirmar(True/False).')
                response = self.controller.communication_window.wait_for_response()

                if response.lower() == 'true' or response == '1':
                    DIDconfirmation = True
                elif response.lower() == 'false' or response == '0':
                    DIDconfirmation = False
                else:
                    DIDconfirmation = False
                    self.controller.communication_window.add_request(
                        'Error: se espera un booleano: True/False ó 1/0')

            self.next_step()

        elif self.step == 5:
            try:
                self.button_done.grid_remove()
            except:
                pass

            mensaje = 'Manteniendo bien presionadas las paletas sobre\n' + \
                'los electrodos del DID, pulse los pulsadores de\n' + \
                'descarga de las paletas'
            self.labelInstruction['text'] = mensaje

            DIDconfirmation = False

            while DIDconfirmation == False and self.controller.omit == False:
                # self.controller.communication_window.add_request(
                #    self.controller.omitir)
                self.controller.communication_window.add_request(
                    'Confirme finalización de descarga.(True/False)')
                response = self.controller.communication_window.wait_for_response()
                if response.lower() == 'true' or response == '1':
                    DIDconfirmation = True
                elif response.lower() != 'false' and response != '0':
                    self.controller.communication_window.add_request(
                        'Error: se espera un booleano: True/False ó 1/0')

            mensaje = '-Instrucciones finales del seguridad-'
            self.labelInstruction['text'] = mensaje

            data = ''

            DIDconfirmation = False
            while DIDconfirmation == False and self.controller.omit == False:
                self.controller.communication_window.add_request(
                    'Envie datos adquiridos. envíe *fin* al finalizar.')
                response = self.controller.communication_window.wait_for_response()
                if response.lower() == 'fin':
                    DIDconfirmation = True

            if self.controller.omit == False:
                self.controller.show_frame(frame_show_data_results)
            else:
                self.controller.show_frame(frame_select_tests)

    # def omitir_Test(self):
    #    self.omitir = True
    #    print(self.omitir)


class frame_show_data_results(tk.Frame):
    def __init__(self, container, controller, *arg, **kwarg):
        super().__init__(container, *arg, **kwarg)

        self.controller = controller
        self.step = 0
        # ------------------------------------CAMPOS------------------------------------------
        frameFields = tk.Frame(self)
        frameFields.grid(row=0, column=0, sticky="nsew", padx=10, pady=0)

        self.labelInstruction = tk.Label(frameFields, text="")
        self.labelInstruction.grid(row=0, column=0, sticky="w", padx=0, pady=0)

        # ------------------------------------GRAFICO------------------------------------------
        framePicture = tk.Frame(self)
        framePicture.grid(row=1, column=0, sticky="w", padx=20, pady=0)
        path = 'Tabla_Monofasica.xlsx'
        data = pd.read_excel(path, header=None)

        figure = Figure(figsize=(5, 4), dpi=100)
        figure.add_subplot(111).plot(data)
        canvas = FigureCanvasTkAgg(figure, master=framePicture)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.Label_Energy=tk.Label(framePicture, text=Get_Energy(path))
        self.Label_Energy.grid(row=2, column=0, sticky="w", padx=0, pady=10)

        # ------------------------------------BOTONES------------------------------------------
        frameButtons = tk.Frame(self)
        frameButtons.grid(row=2, column=0, sticky="w", padx=20, pady=0)

        button_omit_test = tk.Button(
            frameButtons, text="Omitir prueba", width=17)
        button_omit_test.grid(row=0, column=1, sticky="e", padx=10, pady=50)

        self.button_done = tk.Button(
            frameButtons, text="Listo", width=17, command=lambda: self.next_step)
        self.button_done.grid(row=0, column=0, sticky="e", padx=10, pady=50)

    def at_raise(self):
        self.tkraise()


class test_empty1(tk.Frame):

    def __init__(self, container, controller, *arg, **kwarg):
        super().__init__(container, *arg, **kwarg)

        self.controller = controller

        # ------------------------------------WARNING LABEL------------------------------------------
        frame_Warning = tk.Frame(self)
        frame_Warning.grid(row=1, column=0, sticky="nsew", padx=10, pady=20)

        self.labelWarning = tk.Label(frame_Warning, text="Proximamente...")
        self.labelWarning.grid(row=0, column=0, sticky="w", padx=0, pady=0)

        # ------------------------------------BOTONES------------------------------------------
        frameBotones = tk.Frame(self)
        frameBotones.grid(row=2, column=1, sticky="e", padx=20, pady=0)

        self.boton_test = tk.Button(frameBotones, text="Omitir test", width=17,
                                    command=lambda: controller.show_frame(frame_select_tests))
        self.boton_test.grid(row=0, column=0, sticky="w", padx=10, pady=50)

    def at_raise(self):
        self.tkraise()


class test_empty2(tk.Frame):
    def __init__(self, container, controller, *arg, **kwarg):
        super().__init__(container, *arg, **kwarg)

        self.controller = controller

        # ------------------------------------WARNING LABEL------------------------------------------
        frame_Warning = tk.Frame(self)
        frame_Warning.grid(row=1, column=0, sticky="nsew", padx=10, pady=20)

        self.labelWarning = tk.Label(
            frame_Warning, text="Proximamente...")
        self.labelWarning.grid(row=0, column=0, sticky="w", padx=0, pady=0)

        # ------------------------------------BOTONES------------------------------------------
        frameBotones = tk.Frame(self)
        frameBotones.grid(row=2, column=1, sticky="e", padx=20, pady=0)

        self.boton_test = tk.Button(frameBotones, text="Omitir test", width=17,
                                    command=lambda: controller.show_frame(frame_select_tests))
        self.boton_test.grid(row=0, column=0, sticky="w", padx=10, pady=50)

    def at_raise(self):
        self.tkraise()


class test_empty3(tk.Frame):
    def __init__(self, container, controller, *arg, **kwarg):
        super().__init__(container, *arg, **kwarg)

        self.controller = controller

        # ------------------------------------WARNING LABEL------------------------------------------
        frame_Warning = tk.Frame(self)
        frame_Warning.grid(row=1, column=0, sticky="nsew", padx=10, pady=20)

        self.labelWarning = tk.Label(
            frame_Warning, text="Proximamente...")
        self.labelWarning.grid(row=0, column=0, sticky="w", padx=0, pady=0)

        # ------------------------------------BOTONES------------------------------------------
        frameBotones = tk.Frame(self)
        frameBotones.grid(row=2, column=1, sticky="e", padx=20, pady=0)

        self.boton_test = tk.Button(frameBotones, text="Omitir test", width=17,
                                    command=lambda: controller.show_frame(frame_select_tests))
        self.boton_test.grid(row=0, column=0, sticky="w", padx=10, pady=50)

    def at_raise(self):
        self.tkraise()


class test_empty4(tk.Frame):
    def __init__(self, container, controller, *arg, **kwarg):
        super().__init__(container, *arg, **kwarg)

        self.controller = controller

        # ------------------------------------WARNING LABEL------------------------------------------
        frame_Warning = tk.Frame(self)
        frame_Warning.grid(row=1, column=0, sticky="nsew", padx=10, pady=20)

        self.labelWarning = tk.Label(
            frame_Warning, text="Proximamente...")
        self.labelWarning.grid(row=0, column=0, sticky="w", padx=0, pady=0)

        # ------------------------------------BOTONES------------------------------------------
        frameBotones = tk.Frame(self)
        frameBotones.grid(row=2, column=1, sticky="e", padx=20, pady=0)

        self.boton_test = tk.Button(frameBotones, text="Omitir test", width=17,
                                    command=lambda: controller.show_frame(frame_select_tests))
        self.boton_test.grid(row=0, column=0, sticky="w", padx=10, pady=50)

    def at_raise(self):
        self.tkraise()


class test_empty5(tk.Frame):
    def __init__(self, container, controller, *arg, **kwarg):
        super().__init__(container, *arg, **kwarg)

        self.controller = controller

        # ------------------------------------WARNING LABEL------------------------------------------
        frame_Warning = tk.Frame(self)
        frame_Warning.grid(row=1, column=0, sticky="nsew", padx=10, pady=20)

        self.labelWarning = tk.Label(
            frame_Warning, text="Proximamente...")
        self.labelWarning.grid(row=0, column=0, sticky="w", padx=0, pady=0)

        # ------------------------------------BOTONES------------------------------------------
        frameBotones = tk.Frame(self)
        frameBotones.grid(row=2, column=1, sticky="e", padx=20, pady=0)

        self.boton_test = tk.Button(frameBotones, text="Omitir test", width=17,
                                    command=lambda: controller.show_frame(frame_select_tests))
        self.boton_test.grid(row=0, column=0, sticky="w", padx=10, pady=50)

    def at_raise(self):
        self.tkraise()


class test_empty6(tk.Frame):
    def __init__(self, container, controller, *arg, **kwarg):
        super().__init__(container, *arg, **kwarg)

        self.controller = controller

        # ------------------------------------WARNING LABEL------------------------------------------
        frame_Warning = tk.Frame(self)
        frame_Warning.grid(row=1, column=0, sticky="nsew", padx=10, pady=20)

        self.labelWarning = tk.Label(
            frame_Warning, text="Proximamente...")
        self.labelWarning.grid(row=0, column=0, sticky="w", padx=0, pady=0)

        # ------------------------------------BOTONES------------------------------------------
        frameBotones = tk.Frame(self)
        frameBotones.grid(row=2, column=1, sticky="e", padx=20, pady=0)

        self.boton_test = tk.Button(frameBotones, text="Omitir test", width=17,
                                    command=lambda: controller.show_frame(frame_select_tests))
        self.boton_test.grid(row=0, column=0, sticky="w", padx=10, pady=50)

    def at_raise(self):
        self.tkraise()
