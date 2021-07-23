from observador import Observador
from item import Item

class Cliente(Observador):

    def __init__(self, nome, cpf, menu):
        self.cpf = cpf
        self.nome = nome
        self.menu = menu
        self.pedidos = []
        self.totalConta = None
        self.pedidoConfirmado = False

    def listar_menu(self):
        for item in self.menu:
            print(item)

    def filtrar_menu_por_tipo(self, tipo):
        for item in self.menu:
            if (item["tipo"] == tipo):
                print(item)

    def realizar_pedido(self, item_id, quantidade):
        for item in self.menu:
            if (item["item_id"] == item_id):
                self.pedidos.append(Item(item["item_id"], item["nome"], quantidade, item["tipo"], item["preco"]).json())

    def update(self, codigo):
        print(f'{self.nome} --- {self.cpf}')
        if(codigo == 'pedidos'):
            self.pedidoConfirmado = True
            for pedido in self.pedidos:
                print(f'{pedido}')
        if(codigo == 'conta'):
            self.totalConta = 0.0
            for pedido in self.pedidos:
                self.totalConta += pedido["preco"] * pedido["quantidade"]
            print(f'R$ {self.totalConta}')

    def json(self):
        return {
            'cpf': self.cpf,
            'nome': self.nome,
            'pedidos': self.pedidos
        }
