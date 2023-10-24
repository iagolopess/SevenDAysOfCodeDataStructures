# -*- coding:latin1 -*-


class Pedido:

    def __init__(self,num_pedido, nome_cliente, itens_pedido, valor_total):
        self.num_pedido = num_pedido
        self.nome_cliente = nome_cliente
        self.itens_pedido = itens_pedido
        self.valor_total = valor_total
    

class FilaDePedidos:

    def __init__(self):
        self.lista_pedidos = []
    
    def adiciona_pedido(self, num_pedido, nome_cliente, item_pedido, valor_total):
        novo_pedido = Pedido(num_pedido, nome_cliente, item_pedido, valor_total)

        self.lista_pedidos.append(novo_pedido)
    
    def remove_pedido(self):

        if len(self.lista_pedidos) < 1:
            return print("Lista está vazia")
        else:
            self.lista_pedidos.pop(0)

    def exibe_pedidos(self):

        if len(self.lista_pedidos) < 1:
            print("Não há mais pedidos a serem exibidos")
        else:
            for pedido in self.lista_pedidos:
                print(f"Nº Pedido {pedido.num_pedido} | Nome Cliente {pedido.nome_cliente} | Pedido {pedido.itens_pedido} | Total R$ {pedido.valor_total}")
            print("-"*60)

fazer_pedido = FilaDePedidos()
fazer_pedido.adiciona_pedido("123", "Andarirano", "Box Frango Louco", "45.90")
fazer_pedido.adiciona_pedido("124", "Marco", "Burguer Frango Mania Combo", "25.90")
fazer_pedido.adiciona_pedido("125", "Luiza", "Combo Pollo Loco", "30.90")
fazer_pedido.exibe_pedidos()
fazer_pedido.remove_pedido()
fazer_pedido.exibe_pedidos()
fazer_pedido.remove_pedido()
fazer_pedido.exibe_pedidos() 
fazer_pedido.remove_pedido()
fazer_pedido.exibe_pedidos()        