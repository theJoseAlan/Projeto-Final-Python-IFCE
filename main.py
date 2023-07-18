from consolemenu import *
from consolemenu.items import *

from util.cadastro import *

def menu_adicionar_cadastro():
    print(" -- Adicionar novo usuário -- ")

    while True:

        caracteres = "1234567890!@#$%¨&*()\|,<>.;:?/^~`´-_=+[{}]"
        temCaracterInvalido = False

        nome = input("Informe o nome: ")

        if nome == '':
            print("\033[33mO campo NOME não pode estar vazio.\033[m")
            continue

        
        for erro in nome:
            for caracter in caracteres:
                if erro == caracter:
                    temCaracterInvalido = True
                    break
            if temCaracterInvalido:
                break

        if temCaracterInvalido:
            print("\033[31mO nome inserido contém caracteres inválidos.\033[m Tente novamente.")
            continue

        break


    while(True):

        try:
            celular = int(input("Informe o celular (Apenas números): "))

            if(celular < 11111111111 or celular > 99999999999):
                print("\033[31mNúmero inválido!\033[m Números a mais ou a menos! Tente novamente")
                print("Formato: DDD912345678")
            else:
                break

        except:
            print("\033[31mNumero de celular inválido!\033[m Tente novamente")
            continue

    while(True):
        temArroba = False

        email = input("Informe o email: ")

        if(email==''):
            print("O campo EMAIL não pode estar vazio")
            continue

        for arroba in email:
            if arroba == "@":
                temArroba = True
                break

        if not temArroba:
            print("\033[31mO email informado não contém formato válido!\033[m Tente novamente.")
            continue

        break

    while(True):
        try:
            idade = int(input("Informe a idade: "))

            if(idade<=0 or idade>=170):
                print("\033[31m Idade inválida! \033[m Tente novamente")
                continue
            else:
                break
        except:
            print("\033[31mIdade com formato inválido! \033[m Tente novamente")
            continue



    item_adicionado = adicionar_cadastro(nome, email, celular, idade)


    print(item_adicionado, " -- adicionado com sucesso.")
    input('Pressione uma tecla para continuar')

def menu_remover_cadastro():
    print(" -- Remover Cadastro -- ")
    id_para_remover = int(input("Informe o 'ID' para remover: "))

    operacao_deu_certo = remover_por_id(id_para_remover)

    '''if operacao_deu_certo:
        print("Cadastro '{}' removido com sucesso.".format(id_para_remover))
    else:
                
        #Informe aqui uma mensagem caso tenha dado erro na remoção
        #do cadastro
        '''
    pass

    input('Pressione uma tecla para continuar')

def menu_pesquisar_cadastro():
    print(" -- Pesquisar por ID -- ")
    id_para_pesquisar = int(input("Informe o 'ID' para pesquisar: "))
    cadastro = pesquisar_cadastro_por_id(id_para_pesquisar)
    print(cadastro)
    print("\033[m")
    input('Pressione uma tecla para continuar')

def menu_pesquisar_nome():
    print(" -- Pesquisar por NOME -- ")
    nome_para_pesquisar = str(input("Informe o 'NOME' para pesquisar: "))
    cadastro = pesquisar_cadastro_por_nome(nome_para_pesquisar)
    print(cadastro)
    print("\033[m")
    input('Pressione uma tecla para continuar')


def menu_imprimir_cadastros():
    print(" -- Itens cadastrados -- ")
    imprimir_dados()
    input('Pressione uma tecla para continuar')


# Cria o menu
menu = ConsoleMenu("Cadastro de Usuários")

# Cria itens do menu
menu_item_adicionar = FunctionItem("Adicionar cadastro.", menu_adicionar_cadastro)
'''
Adicione o menu_item_imprimir
'''
menu_item_pesquisar = FunctionItem("Pesquisar cadastro.", menu_pesquisar_cadastro)
menu_item_remover = FunctionItem("Remover cadastro.", menu_remover_cadastro)
menu_item_listar = FunctionItem("Listar cadastros.", menu_imprimir_cadastros)
menu_item_pesquisar_nome = FunctionItem("Pesquisar por nome.", menu_pesquisar_nome)

menu.append_item(menu_item_adicionar)
'''
Adicione o "menu.append_item(menu_item_imprimir)"
'''

menu.append_item(menu_item_pesquisar)
menu.append_item(menu_item_pesquisar_nome)
menu.append_item(menu_item_listar)
menu.append_item(menu_item_remover)
menu.show()






