# Gerenciamento de funcionarios.

#Dicionario com cadastro dos funcionarios.
cadastro = {

    "cpf": 0,
    "nome": "Nome Funcionario",
    "idade": 0,
    "cargo": "Cargo Funcionario",
    "salario": 0
}

#Lista dos funcionarios que vamos usar com o For
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

            cpf = int(input("CPF do Funcionário: "))
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

                #Guarda os dados do cadastro na lista funcionarios.
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


    #Listando todos os funcionarios da empresa
    elif opcao == "2":

        print("Listando todos os funcionários.")

        for func in funcionarios:

            print(f"Cpf: {func['cpf']}")
            print(f"Nome: {func['nome']}")  
            print(f"Idade: {func['idade']}")
            print(f"Cargo: {func['cargo']}")
            print(f"Salario: {func['salario']}")
            print("===========================")

    #Listando funcionario 1 por 1 com CPF        
    elif opcao == "3":

        while True:

            print("Buscar funcionário por CPF")

            cpf_func = int(input("Digite o CPF do funcionário: "))

            for func in funcionarios:

                if func["cpf"] == cpf_func:

                    print(f"Nome: {func['nome']}")  
                    print(f"Idade: {func['idade']}")
                    print(f"Cargo: {func['cargo']}")
                    print(f"Salario: {func['salario']}")

                else: 

                    print("Erro: CPF inválido.")


            print("Deseja realizar outra consulta?")
                
            resposta = input("Digite 's' para sim ou 'n' para não: ")
                
            if resposta.lower() == 's':
                continue
                
            elif resposta.lower() == 'n':
                print("Voltando a menu principal....")  
                break
                
            else:
                print("Resposta Inválida.")

    #Calculando todos os salários
    elif opcao == "4":

        print("Calculando todos os salários.")

        total = sum(func["salario"] for func in funcionarios)
        print("A soma de todos os salários ficam em: R$ ", total)

    elif opcao == "5":

        print("Funcionário com maior salário.")

        maior = max(func["salario"] for func in funcionarios)

        for func in funcionarios:

            if func["salario"] == maior:

                print("Funcionário com o maior salário: ")
                print(f"Nome: {func['nome']}")  
                print(f"Idade: {func['idade']}")
                print(f"Cargo: {func['cargo']}")
                print(f"Salario: {func['salario']}")


    elif opcao == "6":

        print("Funcionário com menor salário.")

        menor = min(func["salario"] for func in funcionarios)
        
        for func in funcionarios:

            if func["salario"] == menor:

                print("Funcionário com o maior salário: ")
                print(f"Nome: {func['nome']}")  
                print(f"Idade: {func['idade']}")
                print(f"Cargo: {func['cargo']}")
                print(f"Salario: {func['salario']}")


    elif opcao == "7":

        print("Programa encerrado.")
        break


    else:

        print("Opção Inválida!")

        


            

            


