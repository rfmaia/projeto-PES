class Item:

    def __init__(self, item_id, nome, quantidade, tipo, preco):
        self.item_id = item_id
        self.nome = nome
        self.quantidade = quantidade
        self.tipo = tipo
        self.preco = preco

    def json(self):
        return {
            'item_id': self.item_id,
            'nome': self.nome,
            'quantidade': self.quantidade,
            'tipo': self.tipo,
            'preco': self.preco
        }
        