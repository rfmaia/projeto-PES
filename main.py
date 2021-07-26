from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from src.cliente import Cliente
from src.garcom import Garcom

menu = [{"item_id": "0",
         "nome": "Refrigerante",
         "tipo": "bebida",
         "preco": 3.00},
        {"item_id": "1",
         "nome": "Pastel 4 Queijos",
         "tipo": "salgado", 
         "preco": 10.0}]

garcom = Garcom()

app = FastAPI()

class ClienteAPI(BaseModel):
    name: str

@app.get("/cliente/{cpf}")
def busca_cliente(cpf: str):
    return {"cliente": [cliente for cliente in garcom.clientes if cliente.cpf == cpf]}

@app.put("/cliente/{cpf}")
def cadastra_cliente(cpf: str, cliente: ClienteAPI):
    garcom.adicionar_cliente(Cliente(cliente.name, cpf, menu))
    return {"cliente": [cliente for cliente in garcom.clientes if cliente.cpf == cpf]}

@app.get("/cliente/{cpf}/menu")
def cliente_lista_menu(cpf: str):
    return {"menu": [cliente.listar_menu() for cliente in garcom.clientes if cliente.cpf == cpf]}

@app.get("/cliente/{cpf}/menu/{tipo}")
def cliente_lista_menu_filtrado(cpf: str, tipo: str):
    return {"menu": [cliente.filtrar_menu_por_tipo(tipo) for cliente in garcom.clientes if cliente.cpf == cpf]}

@app.put("/cliente/{cpf}/pedido/{idItem}/{quantidade}")
def cliente_realiza_pedido(cpf: str, idItem: str, quantidade: int):
    return {"Pedido": [cliente.realizar_pedido(idItem, quantidade) for cliente in garcom.clientes if cliente.cpf == cpf]}

@app.put("/cliente/{cpf}/preco")
def cliente_solicita_encerramento_da_conta(cpf: str):
    garcom.notificar_observadores()
    return {"cpf": cpf , "Total": [cliente.totalConta for cliente in garcom.clientes if cliente.cpf == cpf]}

@app.get("/garcom")
def garcom_lista_pedidos():
    return {"Garcom": [(cliente.nome,cliente.pedidos) for cliente in garcom.clientes]}












'''
g1 = Garcom() # Inicialização do Garçom 1 (Subject)

c1 = Cliente("João", "123456789", menu) # Inicialização do Cliente 1 (Observer 1)
c2 = Cliente("Maria", "987654321", menu) # Inicialização do Cliente 2 (Observer 2)

g1.adicionar_cliente(c1) # Inscrever cliente 1 para o Garçom 1
g1.adicionar_cliente(c2) # Inscrever cliente 2 para o Garçom 1

# Cliente 1 ver o menu
c1.listar_menu()

# Pedidos do Cliente 1
c1.realizar_pedido("0", 1)
c1.realizar_pedido("1", 2)

# Cliente 2 filtra menu por tipo
c2.filtrar_menu_por_tipo("salgado")

# Pedidos do Cliente 2
c2.realizar_pedido("1", 10)

print("-" * 50)

print(f"Cliente 1: Pedido Confirmado pelo Garçom? {c1.pedidoConfirmado}")
print(f"Cliente 2: Pedido Confirmado pelo Garçom? {c1.pedidoConfirmado}")
g1.notificar_observadores('pedidos') # Garçom 1 confirma os pedidos dos clientes que estão lhe observando
print(f"Cliente 1: Pedido Confirmado pelo Garçom? {c1.pedidoConfirmado}")
print(f"Cliente 2: Pedido Confirmado pelo Garçom? {c1.pedidoConfirmado}")

print("-" * 50)

print(c1.totalConta)
print(c2.totalConta)
g1.notificar_observadores('conta') # Garçom 1 entrega o total da conta para os clientes
print(c1.totalConta)
print(c2.totalConta)
'''
