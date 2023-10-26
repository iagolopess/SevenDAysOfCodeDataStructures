# -*- coding:latin1 -*-

class Livro():
    
    def __init__(self, titulo, n_paginas):
        self.titulo = titulo
        self.n_paginas = n_paginas


class PilhaDeLivros:

    def __init__(self):
        self.pilha_de_livros = []

    def adiciona_livro(self, titulo, n_paginas):
        novo_livro = Livro(titulo, n_paginas)

        self.pilha_de_livros.append(novo_livro)

    def remove_livro(self):

        if len(self.pilha_de_livros) < 1:
            return ("Não há livros a serem removidos")
        else:
            self.pilha_de_livros.pop()

    def exibe_livro_topo(self):

        if len(self.pilha_de_livros) < 1:
            return("Não há livros a serem exibidos")
        else:
            livro_topo = self.pilha_de_livros[-1]
            return print(f"Titulo: {livro_topo.titulo} | Nº de páginas {livro_topo.n_paginas}")
        
    def exibe_lista_livros(self):

        for livro in self.pilha_de_livros:
            print(f"Titulo: {livro.titulo} | Nº de Páginas: {livro.n_paginas}")
        print("-"*60)

add_novo_livro = PilhaDeLivros()
add_novo_livro.adiciona_livro("Guerra dos Tronos", 592)
add_novo_livro.adiciona_livro("A Fúria dos reis", 656)
add_novo_livro.adiciona_livro("A tormenta de espadas", 884)
add_novo_livro.adiciona_livro("O Festim dos Corvos", 644)
add_novo_livro.adiciona_livro("A dança dos dragões", 872)
add_novo_livro.exibe_lista_livros()
add_novo_livro.remove_livro()
add_novo_livro.exibe_lista_livros()
add_novo_livro.exibe_livro_topo()