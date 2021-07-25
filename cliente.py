from observador import Observador
from item import Item

class Cliente(Observador):

    def __init__(self, nome, cpf, menu):
        self.cpf = cpf
        self.nome = nome
        self.menu = menu
        self.pedidos = []
        self.totalConta = None
    
    def __eq__(self, client):
        if (isinstance(client, Cliente)):
            return True if self.cpf == client.cpf else False
        else:
            return False

    def listar_menu(self):
        return self.menu

    def filtrar_menu_por_tipo(self, tipo):
        return [item for item in self.menu if item["tipo"] == tipo]

    def realizar_pedido(self, item_id, quantidade):
        for item in self.menu:
            if (item["item_id"] == item_id):
                self.pedidos.append(Item(item["item_id"], item["nome"], quantidade, item["tipo"], item["preco"]).json())
        return self.nome, self.cpf, self.pedidos

    def update(self):
        self.totalConta = 0.0
        for pedido in self.pedidos:
            self.totalConta += pedido["preco"] * pedido["quantidade"]
        return self.totalConta
