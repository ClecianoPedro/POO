from livro import Livro
from biblioteca import Biblioteca

def main():
    livro = Livro("POO", "Elisson", 2024, "FAP")
    livro.exibir_livro()
    livro.emprestar()
    livro.exibir_livro()
    livro.devolver()
    livro.exibir_livro()

    livro2 = Livro("POO 2", "Elisson", 2024, "FAP")
    livro2.exibir_livro()
    livro2.emprestar()
    livro2.exibir_livro()
    livro2.devolver()
    livro2.exibir_livro()

    biblioteca = Biblioteca()
    biblioteca.adicionar_livro(livro)
    biblioteca.adicionar_livro(livro2)
    biblioteca.listar_livros()

if __name__ == "__main__":
    main()