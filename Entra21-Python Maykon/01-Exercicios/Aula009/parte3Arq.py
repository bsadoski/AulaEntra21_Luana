import parte1Arq

def listarPessoas():
    idInvalida = False
    arquivoPessoas = open('pessoas.txt', 'a')

    print("-" * 45)
    print("""
    1) Listar Todos
    2) Listar específico
    """)
    print("-" * 45)
    escolhaUserListar = int(input("Qual opção você deseja? "))
    if (escolhaUserListar == 1):
        arquivoPessoas = open('pessoas.txt', 'r')
        for pessoa in arquivoPessoas:
            linhaLimpa = pessoa.strip()
            listaDados = linhaLimpa.split(';')
            print(f"Nome: {listaDados[0]} - Sobrenome: {listaDados[1]} - Idade: {listaDados[2]} - ID: {listaDados[3]}")
        arquivoPessoas.close()
    elif (escolhaUserListar == 2):
        idPesquisa = input("Digite o id da pessoa desejada: ")

        arquivoPessoas = open('pessoas.txt', 'r')
        for pesquisa in arquivoPessoas:
            linhaLimpa = pesquisa.strip()
            listaDados = linhaLimpa.split(';')
            if (idPesquisa == listaDados[3]):
                print(f"Nome: {listaDados[0]} - Sobrenome: {listaDados[1]} - Idade: {listaDados[2]} - ID: {listaDados[3]}")
                idInvalida = False
                break
            else:
                idInvalida = True
        
        if (idInvalida):
            print("ID informado inválido.")
        arquivoPessoas.close()
    else:
        print("Opção inválida.")