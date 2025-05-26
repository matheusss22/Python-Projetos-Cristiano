class Paciente:
    def __init__(self, nome, idade, peso, altura):
        self.set_nome(nome)
        self.set_idade(idade)
        self.set_peso(peso)
        self.set_altura(altura)

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_peso(self):
        return self.__peso

    def get_altura(self):
        return self.__altura

    def set_nome(self, nome):
        self.__nome = nome.strip()

    def set_idade(self, idade):
        self.__idade = int(idade)

    def set_peso(self, peso):
        self.__peso = float(peso)

    def set_altura(self, altura):
        self.__altura = float(altura)

    def get_imc(self):
        return round(self.__peso / (self.__altura ** 2), 2)
    
    def classificar_imc(self):
        imc = self.get_imc()
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Peso normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        elif 30 <= imc < 34.9:
            return "Obesidade grau 1"
        elif 35 <= imc < 39.9:
            return "Obesidade grau 2"
        else:
            return "Obesidade grau 3 (mórbida)"
