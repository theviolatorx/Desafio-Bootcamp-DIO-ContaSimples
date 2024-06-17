import os

menu = """
#####################################################

MENU PRINCIPAL:

[ D ] - Depósito
[ S ] - Saque
[ E ] - Extrato
[ Q ] - Sair

#####################################################

Escolha a sua opção:
"""

saldo = 0
extrato = "\n"
saques_realizados = 0
LIMITE_SAQUE = 500
LIMITES_SAQUE_DIARIO = 3

while True:
    os.system("cls")
    print(menu)
    opcao = input()

    print()

    if (opcao.lower() == "d"):
        print("Informe o valor a ser depositado: ")
        valor_deposito = input()
        if (valor_deposito.isnumeric() and float(valor_deposito) > 0):
            valor_deposito = float(valor_deposito)
            saldo += valor_deposito
            print("Deposito realizado com sucesso!")
            extrato += f'Deposito R$  {valor_deposito:.2f}\n'
            extrato += f'Saldo    R$  {saldo:.2f}\n'
        else:
            print("Valor informado inválido!")
    elif (opcao.lower() == "s"):
        if (saques_realizados < LIMITES_SAQUE_DIARIO):
            print("Informe o valor a ser sacado: ")
            valor_saque = input()
            if (valor_saque.isnumeric() and float(valor_saque) > 0):
                valor_saque = float(valor_saque)
                if (valor_saque > LIMITE_SAQUE):
                    print(f'Valor de saque excedeu o valor de R$ {
                        LIMITE_SAQUE:.2f}!')
                elif (valor_saque > saldo):
                    print(f'Valor de saque excedeu o saldo em conta!')
                else:
                    saldo -= valor_saque
                    print("Saque realizado com sucesso!")
                    saques_realizados += 1
                    extrato += f'Saque    R$ -{valor_saque:.2f}\n'
                    extrato += f'Saldo    R$  {saldo:.2f}\n'
            else:
                print("Valor informado inválido!")
        else:
            print(f'Você já excedeu o limite de saques diários! {
                  LIMITES_SAQUE_DIARIO} por dia!')
    elif (opcao.lower() == "e"):
        print("EXTRATO")
        print(extrato)
        print()
    elif (opcao.lower() == "q"):
        print("Obrigado por utilizar o nosso banco!")
        break
    else:
        print("Opção inválida!")

    print()
    print("Precione qualquer [ENTER] para retornar ao menu principal!")
    opcao = input()
