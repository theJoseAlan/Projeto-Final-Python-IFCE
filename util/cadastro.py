# Dados será uma lista de tuplas
# Tuplas: (id, nome, celular, email, idade)

dados = []

def novo_id():
    # Deve retornar o próximo valor de id dentro de dados
    # Verificar o maior id em dados e somar + 1

    return len(dados) + 1

def adicionar_cadastro(nome = '', celular = 0, email = '', idade = 0) -> tuple:
    novo_cadastro = ()
    id = novo_id()

    if (id < 1):
        print("'ID' gerado é inválido.")
        print("Cadastro não realizado.")
        return ()

    novo_cadastro = (id, nome, celular, email, idade)

    dados.append(novo_cadastro)

    return novo_cadastro

def pesquisar_cadastro_por_id(id: int) -> tuple:

    for cad in dados:
        if (cad[0] == id):
            print("\033[34m", end=' ')
            return cad


    print("\33[31mCadastro não encontrado para o id: \033[m",id)

    #return tuple() # tupla vazia

def pesquisar_cadastro_por_nome(nome: str) -> tuple:

    for cad in dados:
        if (cad[1] == nome):
            print("\033[34m", end=' ')
            return cad


    print("\33[31mCadastro não encontrado para o nome: \033[m",nome)

    #return tuple() # tupla vazia

def remover_por_id(id: int) -> bool:

    response = pesquisar_cadastro_por_id(id)

    if response is not None:

        confirm = str(input("\033[33mTem certeza que deseja remover\033[m "+response[1]+" \033[33mdo sistema?\033[m [S/N]: "))
        print("")
        if(confirm == "S" or confirm == "s"):
            print("\33[33mO usuário \033[m", response[1], "\033[33m foi removido com sucesso! \033[m")
            dados.remove(response)
            return True
        else:
            print("Cadastro de "+response[1]+" mantido no sistema")
    else:
        return False


def imprimir_dados():
    print("\033[34m")
    for dado in dados:
        #for c in range(0, len(dado)):
        print("{} -- {} -- {} -- {} -- {}".format(dado[0], dado[1], dado[2], dado[3], dado[4]))
    print("\033[m")
