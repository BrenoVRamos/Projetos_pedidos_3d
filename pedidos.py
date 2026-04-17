#Criando a lista de pedidos 
pedidos = [] 

def criar_pedidos (cliente, descricao):
    pedido = {
        'cliente': cliente,
        'descricao' : descricao,
        'status' : 'Recebido'
    }
    pedidos.append(pedido)

def listar_pedidos(): 
    return pedidos