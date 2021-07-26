import unittest

from src.garcom import *
from src.cliente import *

#garcom = Garcom()

class TestGarcom(unittest.TestCase):

    def test_adicionar_cliente(self):
        garcom = Garcom()
        cliente = garcom.adicionar_cliente(
                Cliente("123.27449480", "iiiii", ""))

        test_lista = cliente in garcom.clientes
        self.assertTrue(test_lista)

    def test_remover_cliente(self):
        
        garcom = Garcom()
        cliente = Cliente("12312321", "ewrfsdiofjs", "")
        cliente = garcom.adicionar_cliente(cliente)

        cliente = garcom.remover_cliente(cliente)
        
        test_lista = cliente in garcom.clientes
        self.assertFalse(test_lista)

if __name__ == '__main__':
    unittest.main()
