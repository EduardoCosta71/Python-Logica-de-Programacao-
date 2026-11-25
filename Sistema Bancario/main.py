# Sistema Bancario

# == Criação da conta == 
def criar_conta(conta_criada):

    titular = input("Digite o nome do titular: ").strip()

    while titular == "":

        print("O titular não pode ficar vazio!")

        titular = input("Digiteo nome do titular: ").strip()

    while True:

        try:

            numeroConta = int(input("Digite o número da conta: "))

            if numeroConta <= 0:

                print("O número da conta deve ser maior que zero!")

            elif any(c["numeroConta"] == numeroConta for c in conta_criada):

                print("Erro: já exite um cadastro com esse número!")

            else:
                break

        except ValueError:

            print("Erro! Digite um apenas números inteiros para a conta")
    
    #dicionario para criação da conta  
    conta = {

        "titular": titular,
        "numeroConta": numeroConta,
        "saldo": 0.0

        }

    #As informações do dadas pelos usuarios dentro da função, são armazenas neste dicionario Conta.
    conta_criada.append(conta)
    print(f"Cadastro do(e) {titular} feito com sucesso!")


# == Consultar o saldo ==
def consultar_saldo(conta_criada):

    while True:
        
        numeroC = int(input("Digite seu número de conta para consultar seu saldo:  "))
        encontrado = False

        for c in conta_criada:

            if c["numeroConta"] == numeroC:

                encontrado = True

                print(f"Titular: {c['titular']}")
                print(f"Número da Conta: {c['numeroConta']}")
                print(f"Saldo: {c['saldo']}")

        if encontrado == False:

            print("Conta não encontrada")

        print("Deseja realizar outra consulta?")
                        
        resposta = input("Digite 's' para sim ou 'n' para não: ")
                        
        if resposta.lower() == 's':
            continue
                        
        elif resposta.lower() == 'n':
            print("Voltando a menu principal....")  
            break
                        
        else:
            print("Resposta Inválida.")



def depositar(conta_criada):

    while True:

        numeroC = int(input("Digite seu número de conta para depositar o dinheiro :  "))

        if numeroC <= 0:
            print("O número da conta não pode ser menor ou igual a 0.")

            
        encontrado = False

        for c in conta_criada:
        
            if c["numeroConta"] == numeroC:
        
                encontrado = True

                while True:

                    try:

                        valor = float(input("Deposite o valor desejado: "))

                        if valor <= 0:

                            print("o valor depositado não pode ser abaixo de 0 ou negativo.")

                        else:
                            break

                    except ValueError:

                        print("Erro! Digite um valor numérico valido.")


                saldo_anterior = c['saldo']
                c['saldo'] += valor

                print(f"Titular: {c['titular']}")
                print(f"Número da Conta: {c['numeroConta']}")
                print("Saldo anterior: R$ ", saldo_anterior)
                print(f"Saldo atual: R$ {c['saldo']}")
                
        
        if encontrado == False:
        
            print("Conta não encontrada")
        
            print("Deseja realizar outra consulta?")
                                
        resposta = input("Digite 's' para sim ou 'n' para não: ")
                                
        if resposta.lower() == 's':
            continue
                                
        elif resposta.lower() == 'n':
            print("Voltando a menu principal....")  
            break
                                
        else:
            print("Resposta Inválida.")



contaBanco = []

while True:

    print("============ Sistema Bancario ============")
    print("1 - Cadastrar cliente")
    print("2 - Consultar saldo")
    print("3 - Depositar dinheiro")
    print("8 - Sair")


    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        criar_conta(contaBanco)

    elif opcao == '2':

        consultar_saldo(contaBanco)

    elif opcao == '3':

        depositar(contaBanco)

    elif opcao == "8":

        print("Saindo da conta..")
        break

    else:

        print("Opção Invalida!")

