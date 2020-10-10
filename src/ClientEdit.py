from  CenteredWindow import CenteredWindow
from widgets.ClientForm import *

class ClientEdit(CenteredWindow):
    def __init__(self):
        super().__init__(800, 487, 'Cadastro Cliente')

        self.__frame = Frame(self)
        self.__client_form = ClientForm(self.__frame)
        self.__client_form.pack(fill='both')
        self.__frame.pack(fill='both', padx=10, pady=10)


