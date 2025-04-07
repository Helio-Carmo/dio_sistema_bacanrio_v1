menu = '''
*** Escolha uma operação ***

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair

****************************
: '''

saldo = 0 
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao.lower() == 'd':
        deposito = float(input('Qual valor deseja depositar?\nR$ '))
        if deposito > 0:
            saldo += deposito
            print(f'Deposito de R${deposito:.2f} realizado com sucesso!')
            extrato.append(f'Deposito de R${deposito:.2f}')
        else:
            print('Valor invalido para deposito.\nVoltando ao início...')
        
    elif opcao.lower() =='s':
        if numero_saques != LIMITE_SAQUES:
            saque = float(input('Qual valor deseja sacar?\nR$ '))
            if saque > 0:
                if saque < limite:
                    if saque < saldo:
                        saldo -= saque
                        print(f'Saque de R${saque:.2f} realizado com sucesso!')
                        extrato.append(f'Saque de R${saque:.2f}')
                        numero_saques += 1
                    else:
                        print('Saldo insuficiente para finalizar o saque.\nVoltando ao início...')
                else:
                    print('Valor inserido excede ao limite por saque.\nVoltando ao início...')
            else:
                print('Valor invalido para saque.\nVoltando ao início...')
        else:
            print('Você excedeu o limite de saque diário. Volte amanhã e tente novamente.\n\nVoltando ao início...')

    elif opcao.lower() == 'e':
        print('\n************* EXTRATO **************\n')
        if not extrato: 
            print('Sem movimentações recentes'.center(36))  
        else:
            for item in extrato:
                print(item.center(36))        
        print('\n************************************')
        print(f'Saldo Total: R${saldo:.2f}')
        
    elif opcao.lower() == 'q':
        print('Obrigado por utilizar nosso sistema! \nAté logo\n')
        break
    else:
        print('Opção invalida!! \nTente novamente.')


