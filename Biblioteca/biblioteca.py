from livro import Livro

class Biblioteca:
    # Construtor
    def __init__(self):
        # Atributos
        self.lista_de_livros = []

    # Métodos
    def adicionar_livro(self, livro):
        self.lista_de_livros.append(livro)

    def listar_livros(self):
        for livro in self.lista_de_livros:
            livro.exibir_livro()