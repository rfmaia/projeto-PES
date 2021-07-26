import unittest

from src.cliente import *
#from item import Item

class TestCliente(unittest.TestCase):

    def test_listar_menu(self):
        cliente = Cliente("321312", "2dfasdf", "")
        self.assertEqual(cliente.menu, cliente.listar_menu())

    def test_filtrar_menu_por_tipo(self):
        cliente = Cliente("321312", "2dfasdf", "")
        cliente.menu = [
                {"tipo": "foo"}
                ]
        filtrada = cliente.filtrar_menu_por_tipo("foo")

        passou = True
        for item in filtrada:
            if item["tipo"] != "foo":
                passou = False

        self.assertTrue(passou)

    def test_realizar_pedido(self):
        cliente = Cliente("321312", "2dfasdf", "")
        len_pedidos = len(cliente.pedidos)
        cliente.menu = [
                {"item_id": "foo",
                "nome": cliente.nome,
                "preco": 99,
                "tipo": "kkkk"}
                ]

        nome, cpf, pedidos = cliente.realizar_pedido("foo", 10)

        self.assertEqual(cpf, cliente.cpf)
        self.assertEqual(nome, cliente.nome)
        self.assertTrue(len_pedidos < len(cliente.pedidos))

    
if __name__ == '__main__':
    unittest.main()
