# Gerenciamento de funcionarios.

cadastro = {

    "nome": "Nome Funcionario",
    "idade": 0,
    "cargo": "Cargo Funcionario",
    "salario": 0
}


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

            nome = input("Nome do Funcionário: ")
            idade = int(input("Idade do Funcionário: "))
            cargo = input("Cargo do Funcionário: ")
            salario = float(input("Salário atual do Funcionário: "))

            cadastro["nome"] = nome
            cadastro["idade"] = idade
            cadastro["cargo"] = cargo
            cadastro["salario"] = salario

            if idade <= 16:

                print("A idade não pode ser inferior a 16 anos.")

                if salario < 0:

                    print("Salário acima de 0!")

            else: 
                print("cadastro feito com sucesso!")
                print(f"Nome: {nome}")
                print(f"Idade: {idade}")
                print(f"Cargo: {cargo}")
                print(f"Salario: {salario}")


            print("Deseja realizar outro cadastro?")

            resposta = input("Digite 's' para sim ou 'n' para não: ")

            if resposta.lower() == 's':
                continue

            elif resposta.lower() == 'n':
                print("Voltando a menu principal....")  
                break

            else:
                print("Resposta Inválida.")



    if opcao == "7":

        print("Programa encerrado.")
        break

        


            

            


