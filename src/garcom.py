from typing import Type
from src.observador import Observador

class Garcom:

    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, cliente: Type[Observador]):
        if(all(cliente.cpf != c.cpf for c in self.clientes)):
            self.clientes.append(cliente)
        return cliente

    def remover_cliente(self, cliente: Type[Observador]):
        self.clientes.remove(cliente)
        return cliente
    
    def notificar_observadores(self):
        for cliente in self.clientes:
            cliente.update()
    
