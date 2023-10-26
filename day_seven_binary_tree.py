# -*- coding:latin1 -*-

class Node:
    
    def __init__(self, produto):
        self.produto = produto
        self.direita = None
        self.esquerda = None


class Produto:

    def __init__(self, id, produto, quantidade):
        self.id = id
        self.produto = produto
        self.quantidade = quantidade


class ArvoreProduto:

    def __init__(self):
        self.raiz = None

    def inserir_produto(self, id, produto, quantidade):
        novo_produto = Produto(id, produto, quantidade)

        if self.raiz is None:
            self.raiz = Node(novo_produto)
        else:
            self._inserir_produto(novo_produto, self.raiz)

    def _inserir_produto(self, produto, node):
        
        if produto.id < node.produto.id:

            if node.esquerda is None:
                node.esquerda = Node(produto)
            else:
                self._inserir_produto(produto, node.esquerda)
        
        elif produto.id > node.produto.id:

            if node.direita is None:
                node.direita = Node(produto)
            else:
                self._inserir_produto(produto, node.direita)

        else:
            return print("Produto já existente")
    
    def buscar_produto(self, produto_id):
        return self._buscar_produto(self.raiz, produto_id) 

    def _buscar_produto(self, node, produto_id):
        
        if node is None:
            return print("Produto não encontrado")
        
        if produto_id == node.produto.id:
            return print(f"Id: {node.produto.id} | Nome: {node.produto.produto} | Quantidade {node.produto.quantidade}")   
        elif produto_id < node.produto.id:
            return self._buscar_produto(node.esquerda, produto_id)
        else:
            return self._buscar_produto(node.direita, produto_id)


arvore = ArvoreProduto()

arvore.inserir_produto(1, 'Café', 10)
arvore.inserir_produto(2, 'Arroz', 11)
arvore.inserir_produto(3, 'Batata', 8)
arvore.inserir_produto(4, 'Açúcar', 15)
arvore.inserir_produto(5, 'Frango', 9)
arvore.inserir_produto(6, 'Melancia', 5)
arvore.inserir_produto(7, 'Banana', 7)



produtoBuscado1 = arvore.buscar_produto(2)
produtoBuscado2 = arvore.buscar_produto(1)
produtoBuscado3 = arvore.buscar_produto(20)
produtoBuscado3 = arvore.buscar_produto(5)