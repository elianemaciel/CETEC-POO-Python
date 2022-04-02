from cliente import Cliente
from contas import Conta

joao = Cliente(cpf="234456567-90", nome="João Luiz Tavares")
maria = Cliente(cpf="908786987-09", nome="Maria da Silva")

#joao.imprime_dados_cliente()

#maria.imprime_dados_cliente()

# cria conta

conta_joao = Conta(joao, 2000)

conta_joao.resumo()
