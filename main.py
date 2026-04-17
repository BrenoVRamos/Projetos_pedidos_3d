#importando as funções dos pedidos 
from pedidos import criar_pedidos, listar_pedidos 

#Loop infinito que não encerra o programa até ativar o break na parte de 'sair' 
while True :
    print('\n1 - Criar pedidos')
    print('\n2 - Listar pedidos')
    print('\n3 - Sair') 

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        cliente = input('Nome do cliente: ')
        descricao = input('Descrição do pedido: ')
        criar_pedidos(cliente, descricao)

    elif opcao == '2':
        for pedido in listar_pedidos():
            print(pedido)

    elif opcao == '3':
        break