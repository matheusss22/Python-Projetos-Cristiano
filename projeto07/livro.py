class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.set_titulo(titulo)
        self.set_autor(autor)
        self.set_ano_publicacao(ano_publicacao)

    # Getters
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_ano_publicacao(self):
        return self.__ano_publicacao

    # Setters
    def set_titulo(self, titulo):
        self.__titulo = titulo.strip()

    def set_autor(self, autor):
        self.__autor = autor.strip()

    def set_ano_publicacao(self, ano):
        try:
            self.__ano_publicacao = int(ano)
        except ValueError:
            raise ValueError("Ano de publicação deve ser um número inteiro.")
