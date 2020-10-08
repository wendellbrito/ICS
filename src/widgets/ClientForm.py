from tkinter import *

from widgets.Checkbox import *
from widgets.LabelEntry import *

class ClientForm(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.__entry_rsocial     = LabelEntry(
                self, 'Razão Social', ALPHANUMERIC + SPACE, 255)
        self.__entry_nfantasia   = LabelEntry(
                self, 'Nome Fantasia', ALPHANUMERIC + SPACE, 255)
        self.__entry_cnpj        = LabelEntry(
                self, 'CNPJ', NUMERIC, 14)
        self.__entry_iestadual   = LabelEntry(
                self, 'Inscrição Estadual', NUMERIC, 12)
        self.__entry_imunicipal  = LabelEntry(
                self, 'Inscrição Municipal', NUMERIC, 8)
        self.__entry_logradouro  = LabelEntry(
                self, 'Logradouro', ALPHANUMERIC + SPACE, 255)
        self.__entry_complemento = LabelEntry(
                self, 'Complemento', ALPHANUMERIC + SPACE, 255)
        self.__entry_bairro      = LabelEntry(
                self, 'Bairro', ALPHABET + SPACE, 255)
        self.__entry_municipio   = LabelEntry(
                self, 'Municipio', ALPHABET + SPACE, 255)
        self.__entry_uf          = LabelEntry(
                self, 'UF', ALPHABET + SPACE, 255)
        self.__entry_cep         = LabelEntry(
                self, 'CEP', NUMERIC, 8)
        self.__entry_telefone   = LabelEntry(
                self, 'Telefone', NUMERIC, 10)
        self.__entry_ncel        = LabelEntry(
                self, 'Celular', NUMERIC, 11)
        
        self.__check_whatsapp = Checkbox(self, 'WhatsApp?')

        self.__entry_email       = LabelEntry(
                self, 'E-mail', ALPHANUMERIC + "_@-.", 255)
        self.__entry_url         = LabelEntry(
                self, 'URL', ALPHANUMERIC + "_-./", 255)

        self.__button_salvar    = Button(self, text="Salvar")
        self.__button_cancelar  = Button(self, text="Cancelar",
                command=self.destroy)
        
        self.__entry_cep.rule_add(5, '-')

        self.__entry_cnpj.rule_add(2, '.')
        self.__entry_cnpj.rule_add(5, '.')
        self.__entry_cnpj.rule_add(8, '/')
        self.__entry_cnpj.rule_add(12, '-')

        self.__entry_iestadual.rule_add(3, '.')
        self.__entry_iestadual.rule_add(6, '.')
        self.__entry_iestadual.rule_add(9, '.')
        
        self.__entry_imunicipal.rule_add(1, '.')
        self.__entry_imunicipal.rule_add(4, '.')
        self.__entry_imunicipal.rule_add(7, '-')
        
        self.__entry_telefone.rule_add(0, '(')
        self.__entry_telefone.rule_add(2, ') ')
        self.__entry_telefone.rule_add(7, '-')
        
        self.__entry_ncel.rule_add(0, '(')
        self.__entry_ncel.rule_add(2, ') ')
        self.__entry_ncel.rule_add(4, ' ')
        self.__entry_ncel.rule_add(8, '-')
        
        self.grid_columnconfigure(index=0, minsize=1, weight=5)
        self.grid_columnconfigure(index=1, minsize=1, weight=1)
        self.grid_columnconfigure(index=2, minsize=1, weight=1)
        
        self.__entry_rsocial.grid(row=0, column=0, columnspan=6, stick='ew', pady=3)
        self.__entry_nfantasia.grid(row=1, column=0, stick='ew', pady=3)
        self.__entry_cnpj.grid(row=1, column=1, columnspan=5, stick='ew', pady=3)
        self.__entry_iestadual.grid(row=2, column=0, stick='ew', pady=3)
        self.__entry_imunicipal.grid(row=2, column=1, columnspan=5, stick='ew', pady=3)
        self.__entry_logradouro.grid(row=3, column=0, columnspan=6, stick='ew', pady=3)
        self.__entry_complemento.grid(row=4, column=0, stick='ew', pady=3)
        self.__entry_bairro.grid(row=4, column=1, columnspan=5, stick='ew', pady=3)
        self.__entry_municipio.grid(row=5, column=0, stick='ew', pady=3)
        self.__entry_uf.grid(row=5, column=1, columnspan=2, stick='ew', pady=3)
        self.__entry_cep.grid(row=5, column=3, columnspan=4, stick='ew', pady=3)
        self.__entry_telefone.grid(row=6, column=0, stick='ew', pady=3)
        self.__entry_ncel.grid(row=6, column=1, columnspan=4, stick='ew', pady=3)
        self.__check_whatsapp.grid(row=6, column=5, stick='nsew', pady=3)
        self.__entry_email.grid(row=7, column=0, columnspan=6, stick='ew', pady=3)
        self.__entry_url.grid(row=8, column=0, columnspan=6, stick='ew', pady=3)

        self.__button_salvar.grid(row=9, column=4, stick='e')
        self.__button_cancelar.grid(row=9, column=5, stick='e')

    def get_rsocial(self):
        self.__entry_rsocial.get_raw()

    def get_nfantasia(self):
        self.__entry_nfantasia.get_raw()

    def get_cnpj(self):
        self.__entry_cnpj.get_raw()

    def get_iestadual(self):
        self.__entry_iestadual.get_raw()

    def get_imunicipal(self):
        self.__entry_imunicipal.get_raw()

    def get_logradouro(self):
        self.__entry_logradouro.get_raw()

    def get_complemento(self):
        self.__entry_complemento.get_raw()

    def get_bairro(self):
        self.__entry_bairro.get_raw()

    def get_municipio(self):
        self.__entry_municipio.get_raw()

    def get_uf(self):
        self.__entry_uf.get_raw()

    def get_cep(self):
        self.__entry_cep.get_raw()

    def get_telefone(self):
        self.__entry_telefone.get_raw()

    def get_celular(self):
        self.__entry_celular.get_raw()

    def get_email(self):
        self.__entry_email.get_raw()

    def get_url(self):
        self.__entry_url.get_raw()
    
    def set_rsocial(self, value):
        self.__entry_rsocial.set_raw(value)

    def set_nfantasia(self, value):
        self.__entry_nfantasia.set_raw(value)

    def set_cnpj(self, value):
        self.__entry_cnpj.set_raw(value)

    def set_iestadual(self, value):
        self.__entry_iestadual.set_raw(value)

    def set_imunicipal(self, value):
        self.__entry_imunicipal.set_raw(value)

    def set_logradouro(self, value):
        self.__entry_logradouro.set_raw(value)

    def set_complemento(self, value):
        self.__entry_complemento.set_raw(value)

    def set_bairro(self, value):
        self.__entry_bairro.set_raw(value)

    def set_municipio(self, value):
        self.__entry_municipio.set_raw(value)

    def set_uf(self, value):
        self.__entry_uf.set_raw(value)

    def set_cep(self, value):
        self.__entry_cep.set_raw(value)

    def set_telefone(self, value):
        self.__entry_telefone.set_raw(value)

    def set_celular(self, value):
        self.__entry_celular.set_raw(value)

    def set_email(self, value):
        self.__entry_email.set_raw(value)

    def set_url(self, value):
        self.__entry_url.set_raw(value)