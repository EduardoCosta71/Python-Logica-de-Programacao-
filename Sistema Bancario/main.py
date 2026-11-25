# Sistema Bancario

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


contaBanco = []

while True:

    print("============ Sistema Bancario ============")
    print("1 - Cadastrar cliente")


    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        criar_conta(contaBanco)

    else:

        print("Opção Invalida!")

