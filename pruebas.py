class status2():
    def __init__(self, controller):
        self.battery = ''
        self.lineConnection = ''
        self.cancelRequest = False
        self.communication_window = controller.communication_window
        self.response_event = Event()

    def update_status(self):
        self.response_event.clear()
        while not self.cancelRequest:
            try:
                # Get lineConnection
                response = self.communication_window.send_message(
                    "get_lineConnection(True/False)")
                self.lineConnection = bool(response)

                # Get battery
                response = self.communication_window.send_message(
                    "get_battery")
                self.battery = int(response)

                # Esperar a que se ingrese una respuesta
                self.communication_window.wait_for_response()
                response_text = self.communication_window.get_response()
                self.add_response(response_text)

            except:
                pass
            finally:
                self.response_event.clear()

    def add_response(self, message):
        # agregar una entrada a la lista con la respuesta recibida del DID
        self.communication_window.add_response(message)
        self.response_event.set()
