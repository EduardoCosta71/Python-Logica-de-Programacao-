# Gerenciamento de funcionarios.

cadastro = {

    "cpf": 0,
    "nome": "Nome Funcionario",
    "idade": 0,
    "cargo": "Cargo Funcionario",
    "salario": 0
}

funcionarios = []


while True:

    #Menu de Escolha
    print("====== SISTEMA DE FUNCIONÁRIOS ======")
    print("1 - Cadastrar funcionário")
    print("2 - Listar funcionários")
    print("3 - Buscar funcionário")
    print("4 - Calcular folha salarial")
    print("5 - Mostrar funcionário com maior salário")
    print("6 - Mostrar funcionário com menor salário")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        print("Cadastro de Funcionário!")

        while  True:
            cpf = int(input("CPF do Funcionário"))
            nome = input("Nome do Funcionário: ")
            idade = int(input("Idade do Funcionário: "))

            if idade <= 16:

                print("A idade não pode ser inferior a 16 anos.")
                break

            cargo = input("Cargo do Funcionário: ")
            salario = float(input("Salário atual do Funcionário: "))

            if salario < 0:
                    print("Salário acima de 0!")
                    break

            else: 

                cadastro["cpf"] = cpf
                cadastro["nome"] = nome
                cadastro["idade"] = idade
                cadastro["cargo"] = cargo
                cadastro["salario"] = salario

                print("cadastro feito com sucesso!")

                print(f"cpf: {cpf}")
                print(f"Nome: {nome}")
                print(f"Idade: {idade}")
                print(f"Cargo: {cargo}")
                print(f"Salario: {salario}")

                funcionarios.append(cadastro.copy())


            print("Deseja realizar outro cadastro?")

            resposta = input("Digite 's' para sim ou 'n' para não: ")

            if resposta.lower() == 's':
                continue

            elif resposta.lower() == 'n':
                print("Voltando a menu principal....")  
                break

            else:
                print("Resposta Inválida.")

    if opcao == "2":

        print("Listando todos os funcionários.")

        for func in funcionarios:

            print(f"Cpf: {func['cpf']}")
            print(f"Nome: {func['nome']}")  
            print(f"Idade: {func['idade']}")
            print(f"Cargo: {func['cargo']}")
            print(f"Salario: {func['salario']}")
            print("===========================")
            
    if opcao == "3":

        print("Buscar funcionário por CPF")

        cpf = int(input("Digite o CPF do funcionário "))





    if opcao == "7":

        print("Programa encerrado.")
        break

        


            

            


