class Usuario():
    def __init__(self, nome, email, password):
        self.__nome = nome
        self.__email = email
        self.__password = password

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password):
        self.__password = password