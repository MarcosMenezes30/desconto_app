from src.models.pedido import Pedido

class PedidoService:

    def __init__(self,):
        self.pedido = []

    def adicionar_pedido(self, pedido : Pedido):
        self.pedido.append(pedido)

    def processar_pedidos(self):
        for pedido in self.pedido:
            print(f"Cliente: {pedido.cliente}")
            print(f"Valor final: {pedido.valor_final(pedido.valor_original)}")
