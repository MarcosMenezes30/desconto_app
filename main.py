from src.controllers.pedido_controller import PedidoController
from src.repositories.pedido_repository import PedidoRepository
from src.services.pedido_service import PedidoService
from src.database.connection import DatabaseConnection
from src.models.pedido import Pedido
from src.models.desconto import DescontoNormal, DescontoPremium, DescontoVIP

if __name__ == "__main__":

    """ 
    Por algum motivo o código comentado abaixo está funcionando mas o do professor não.

    Sigo investigando para tentar entender o motivo.

    pedido = Pedido("Leonardo", DescontoVIP())
    pedido.valor_original = 100.0

    service = PedidoService()
    service.adicionar_pedido(pedido)
    service.processar_pedidos()

    print(f"Valor original do pedido: {pedido.valor_original}")
    print(f"Valor final do pedido: {pedido.valor_final(pedido.valor_original)}")
    """

    database = DatabaseConnection()
    repo = PedidoRepository(database)
    service = PedidoService(repo)
    controller = PedidoController(service)
    # Perguntar ao professor: Qual a diferença entre pedido_service e pedido_controller?
    # Motivo da pergunta: Ambas tem def adicionar_pedidos/processar_pedidos

    # """Criando pedidos e aplicando descontos"""
    pedido1 = Pedido("Cliente A", DescontoNormal())
    pedido1.valor_orginal = 100.0 # Definindo o valor original do pedido

    pedido2 = Pedido("Cliente B", DescontoVIP())
    pedido2.valor_orginal = 200.0 # Definindo o valor original do pedido

    pedido3 = Pedido("Cliente C", DescontoPremium())
    pedido3.valor_orginal = 300.0 # Definindo o valor original do pedido

    # Aqui você pode criar pedidos, aplicar descontos e processar os pedindos

    # Perguntar ao professor: Qual a diferença de usar "service."" e "controller."?
    controller.adicionar_pedidos(pedido1)
    controller.adicionar_pedidos(pedido2)
    controller.adicionar_pedidos(pedido3)

    controller.processar_pedidos()
