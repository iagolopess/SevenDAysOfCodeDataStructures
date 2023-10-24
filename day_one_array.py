# -*- coding: utf-8 -*-


class ListaDeCompras:

    def __init__(self) -> None:
        self.lista_de_compras = []

    def adicionar_item(self, items, quantidades):
        listar_items = [item for item in items]
        self.lista_de_compras.append(listar_items)

        listar_quantidade = [quantidade for quantidade in quantidades]
        self.lista_de_compras.append(listar_quantidade)

    def remover_item(self, item):
        index_item = self.lista_de_compras[0].index(item)

        if item in self.lista_de_compras[0]:
            self.lista_de_compras[0].pop(index_item)
            self.lista_de_compras[1].pop(index_item)
    
    def listar_item(self):
    
        print("ITEM | QUANTIDADE")
        for item in range(len(self.lista_de_compras[0])):
            print(f"{self.lista_de_compras[0][item]} | {self.lista_de_compras[1][item]}")


lista_de_items = ["Macarrão", "Açúcar", "Arroz", "Feijão", "Frango"]
quantidade = [1, 3, 2, 1, 5]

minha_lista = ListaDeCompras()
minha_lista.adicionar_item(lista_de_items, quantidade)
minha_lista.remover_item("Arroz")
minha_lista.listar_item()
