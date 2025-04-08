import textwrap

def menu():
    menu = '''\n
        *** Escolha uma operação ***

                [d]\tDepositar
                [s]\tSacar
                [e]\tExtrato
                [nc]\tNova Conta
                [lc]\tListar Conta
                [nu]\tNovo Usuário
                [q]\tSair

        ****************************
        : '''
    return input(textwrap.dedent(menu))
    

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f'Deposito de R${valor:.2f}')
        print(f'\nDeposito de R${valor:.2f} realizado com sucesso!')
    else:
        print('\nValor inválido para concluir a operação.\n\nVoltando ao início...')

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques != limite_saques:        
        if valor > 0:
            if valor < limite:
                if valor < saldo:
                    saldo -= valor
                    print(f'Saque de R${valor:.2f} realizado com sucesso!')
                    extrato.append(f'Saque de R${valor:.2f}')
                    numero_saques += 1
                else:
                    print('Saldo insuficiente para finalizar o saque.\nVoltando ao início...')
            else:
                print('Valor inserido excede ao limite por saque.\nVoltando ao início...')
        else:
            print('Valor invalido para saque.\nVoltando ao início...')
    else:
        print('Você excedeu o limite de saque diário. Volte amanhã e tente novamente.\n\nVoltando ao início...')

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print('\n************* EXTRATO **************\n')
    if not extrato: 
        print('Sem movimentações recentes'.center(36))
        print('\n************************************')  
    else:
        for item in extrato:
            print(item.center(36))        
    print('\n************************************')
    print(f'Saldo Total: R${saldo:.2f}')


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF (Somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\nConta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('\nUsuário não cadastrado!\nVoltando ao início...')


def listar_contas(contas):
    for conta in contas:
        linha = f'''
                Agência:\t{conta['agencia']}
                C/C:\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            '''
        print('=' * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0 
    limite = 500
    extrato = []
    numero_saques = 0
    usuarios = []
    contas = []
        

    while True:

        opcao = menu().lower()

        if opcao.lower() == 'd':
            deposito = float(input('Qual valor deseja depositar?\nR$ '))

            saldo, extrato = depositar(saldo, deposito, extrato)

        elif opcao.lower() =='s':
            saque = float(input('Qual valor deseja sacar?\nR$ '))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao.lower() == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao.lower() == 'nu':
            criar_usuario(usuarios)
            
        elif opcao.lower() == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao.lower() == 'lc':
            listar_contas(contas)
            
        elif opcao.lower() == 'q':
            print('Obrigado por utilizar nosso sistema! \nAté logo\n')
            break
        else:
            print('Opção invalida!! \nTente novamente.')


main()
