from cliente import Cliente
from garcom import Garcom

menu = [{"item_id": "0",
         "nome": "Refrigerante",
         "tipo": "bebida",
         "preco": 3.00},
        {"item_id": "1",
         "nome": "Pastel 4 Queijos",
         "tipo": "salgado", 
         "preco": 10.0}]

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
