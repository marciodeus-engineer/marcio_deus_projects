import os

clientes = [{"nome": "Aline Stramandinoli", "categoria": "Doceria", "ativo": False}, 
                {"nome": "Luamar", "categoria": "Pizzaria", "ativo": True},
                {"nome": "Boca Rosa", "categoria": "Maquiagem", "ativo": False}]

def exibir_nome_do_programa():
    print("""
    Ｍ．Ｉ．　ＭＡＣＤ
ＡＩ　＆　Ａｕｔｏｍａｔｉｏｎｓ
""")
    print("Seja bem vindo ao ambiente automatizado de Cadastro de Cliente da MACD Automations!\n")
    print("O que deseja fazer hoje?\n")


def exibir_opcoes_do_menu():
    print("1. Cadastrar Cliente")
    print("2. Listar Cliente")
    print("3. Ativar Cliente")
    print("4. Sair\n")

def finalizar_app():
    exibir_subtitulo("Finalizando o App.")

def voltar_ao_menu_principal():
    input("\nTecle enter para voltar ao menu. ")
    main_menu()

def exibir_subtitulo(texto):
    os.system("cls" if os.name == "nt" else "clear")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastar_novo_cliente():
    exibir_subtitulo("Cadastro de novos clientes.")
    nome_do_cliente = input("Digite o nome do cliente que você deseja cadastrar: ")
    categoria_do_cliente = input(f"Digite a categoria do cliente {nome_do_cliente}: ")
    dados_do_cliente = {
        "nome": nome_do_cliente,
        "categoria": categoria_do_cliente,
        "ativo": False,
    }
    clientes.append(dados_do_cliente)
    print(f"Cliente {nome_do_cliente} cadastrado com sucesso!\n")
    voltar_ao_menu_principal()


def listar_clientes():
    exibir_subtitulo("Lista de clientes cadastrados.")
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.\n")
    else:
        for n, cliente in enumerate(clientes):
            nome_do_cliente = cliente["nome"]
            categoria_do_cliente = cliente["categoria"]
            ativo_cliente = "Ativado" if cliente["ativo"] else "Desativado"
            print(f"{n + 1}. {nome_do_cliente} | {categoria_do_cliente} | {ativo_cliente}")
        print()
    voltar_ao_menu_principal()


def alternar_estado_do_cliente():
    exibir_subtitulo("Alternando estado do cliente.")
    nome_do_cliente = input("Digite o nome do cliente que você deseja alternar o estado: ")
    cliente_encontrado = False
    for cliente in clientes:
        if nome_do_cliente == cliente["nome"]:
            cliente_encontrado = True
            cliente["ativo"] = not cliente["ativo"]
            mensagem = (
                f"O cliente {nome_do_cliente} foi ativado com sucesso."
                if cliente["ativo"]
                else f"O cliente {nome_do_cliente} foi desativado com sucesso."
            )
            print(mensagem)
            break
    if not cliente_encontrado:
        print("Cliente não encontrado.")
    voltar_ao_menu_principal()


def escolher_opcao_do_menu():
    try:
        opcao_escolhida = int(input("Digite o número da ação que deseja realizar: "))
        match opcao_escolhida:
            case 1:
                print("Cadastrar Cliente")
                cadastar_novo_cliente()
            case 2:
                print("Listar Cliente")
                listar_clientes()
            case 3:
                print("Ativar Cliente")
                alternar_estado_do_cliente()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida()

def opcao_invalida():
    exibir_subtitulo("Opção inválida.")
    voltar_ao_menu_principal()

def main_menu():
    os.system("cls"if os.name == "nt" else "clear") #Função para limpar a tela do terminal.
    exibir_nome_do_programa()
    exibir_opcoes_do_menu()
    escolher_opcao_do_menu()

if __name__ == "__main__":
    main_menu()