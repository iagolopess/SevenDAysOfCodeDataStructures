# -*- coding:latin1 -*-

class Produto:

    def __init__(self, cod_do_produto, nome_produto, quantidade, preco):
        self.cod_produto = cod_do_produto
        self.nome_produto = nome_produto
        self.quantidade = quantidade
        self.preco = preco
        self.proximo = None
        self.anterior = None


class ListaDeProdutos:

    def __init__(self):
        self.head = None
        self.tail = None

    def adicionar_produto(self, cod_do_produto, nome_produto, quantidade, preco):
        novo_produto = Produto(cod_do_produto, nome_produto, quantidade, preco)

        if self.head is None:
            self.head = novo_produto
            self.tail = novo_produto
        else:
            novo_produto.anterior = self.tail
            self.tail.proximo = novo_produto
            self.tail = novo_produto

    def exibir_produtos(self):

        if self.head is None:
            return print("Não há produtos a serem exibidos")
        else:
            produto_atual = self.head

            while produto_atual is not None:
                print(produto_atual.cod_produto, produto_atual.nome_produto, produto_atual.quantidade, produto_atual.preco, end="\n")
                produto_atual = produto_atual.proximo
            
            print("-"*10)

    
    def procurar_produto(self, cod_produto):
          
        produto_atual = self.head

        while produto_atual.proximo is not None:

            
            if produto_atual.cod_produto == cod_produto:
                return produto_atual
            
            produto_atual = produto_atual.proximo
            
        return None

    def remover_produtos(self, cod_do_produto):
        produto_atual = self.head

        while produto_atual is not None:
                
            if produto_atual.cod_produto == cod_do_produto:
                
                if produto_atual.anterior is not None:
                    produto_atual.anterior.proximo = produto_atual.proximo
                else:
                    self.head = produto_atual.proximo
                
                if produto_atual.proximo is not None:
                    produto_atual.proximo.anterior = produto_atual.anterior
                else:
                    self.tail = produto_atual.anterior
                
                return
            
            produto_atual = produto_atual.proximo
    
    def atualizar_produto(self, cod_produto, nova_quantidade):
        produto_atual = self.procurar_produto(cod_produto)

        if produto_atual is not None:
            produto_atual.quantidade = nova_quantidade
        else:
            return print(f"Não foi possivel atualizar o produto {cod_produto}: Produto não encontrado")

adicionar_produto = ListaDeProdutos()
adicionar_produto.adicionar_produto("317283", "Arroz", "5", "50")
adicionar_produto.adicionar_produto("317284", "Feijão", "3", "33")
adicionar_produto.adicionar_produto("317285", "Frango", "2", "40")
adicionar_produto.adicionar_produto("317286", "Pão", "15", "5")
adicionar_produto.adicionar_produto("317287", "Leite", "12", "48")
adicionar_produto.adicionar_produto("328593", "Sabonete", "6", "3")
adicionar_produto.adicionar_produto("328493", "Shampoo", "2", "10")
adicionar_produto.adicionar_produto("328596", "Detergente", "1", "2")
adicionar_produto.adicionar_produto("328613", "Macarrão", "3", "9")
adicionar_produto.exibir_produtos()
adicionar_produto.remover_produtos("317286")
adicionar_produto.atualizar_produto("317287", "13")
adicionar_produto.atualizar_produto("517287", "13")
adicionar_produto.remover_produtos("217286")
