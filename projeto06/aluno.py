class Aluno:
    def __init__(self, nome, email, telefone, senha):
        self.set_nome(nome)
        self.set_email(email)
        self.set_telefone(telefone)
        self.set_senha(senha)

    # Getters
    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_telefone(self):
        return self.__telefone

    def get_senha(self):
        return self.__senha

    # Setters
    def set_nome(self, nome):
        self.__nome = nome.strip()

    def set_email(self, email):
        self.__email = email.strip()

    def set_telefone(self, telefone):
        self.__telefone = telefone.strip()

    def set_senha(self, senha):
        self.__senha = senha.strip()