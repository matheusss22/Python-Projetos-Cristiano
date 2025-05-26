class Projeto_Calcada:
    def __init__(self, largura_terreno, profundidade_terreno, largura_calcada, altura_concreto):
        self.set_largura_terreno(largura_terreno)
        self.set_profundidade_terreno(profundidade_terreno)
        self.set_largura_calcada(largura_calcada)
        self.set_altura_concreto(altura_concreto)

        self.area_terreno = self.largura_terreno * self.profundidade_terreno
        self.perimetro_terreno = 2 * (self.largura_terreno + self.profundidade_terreno)
        self.area_calcada = self.largura_calcada * self.largura_terreno
        self.perimetro_calcada = 2 * (self.largura_calcada + self.largura_terreno)
        self.volume_concreto = self.area_calcada * self.altura_concreto


    def get_largura_terreno(self):
        return self.largura_terreno

    def get_profundidade_terreno(self):
        return self.profundidade_terreno

    def get_largura_calcada(self):
        return self.largura_calcada

    def get_altura_concreto(self):
        return self.altura_concreto

    def set_largura_terreno(self, largura_terreno):
        largura_terreno = float(largura_terreno)
        if largura_terreno <= 0:
            raise ValueError("A largura do terreno deve ser maior que zero.")
        self.largura_terreno = largura_terreno

    def set_profundidade_terreno(self, profundidade_terreno):
        profundidade_terreno = float(profundidade_terreno)
        if profundidade_terreno <= 0:
            raise ValueError("A profundidade do terreno deve ser maior que zero.")
        self.profundidade_terreno = profundidade_terreno

    def set_largura_calcada(self, largura_calcada):
        largura_calcada = float(largura_calcada)
        if largura_calcada <= 1.2:
            raise ValueError("A largura da calçada deve ser maior que 1.2 m")
        self.largura_calcada = largura_calcada

    def set_altura_concreto(self, altura_concreto):
        altura_concreto = float(altura_concreto)
        if altura_concreto <= 0.06:
            raise ValueError("A altura do concreto deve ser maior que 6 cm")
        self.altura_concreto = altura_concreto
