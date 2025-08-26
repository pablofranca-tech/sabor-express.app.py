import os

restaurantes = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def finalizar_app():
    limpar_tela()
    print('Finalizando app...')

def exibir_menu():
    print("""
    ██████████████████████████████████████████████████████████████████████████
    █─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
    █▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
    ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
    """)
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def cadastrar_restaurante():
    nome = input('Digite o nome do restaurante: ')
    categoria = input('Digite a categoria (ex: Japonesa, Brasileira, Italiana): ')
    restaurante = {'nome': nome, 'categoria': categoria, 'ativo': False}
    restaurantes.append(restaurante)
    print(f'Restaurante "{nome}" cadastrado com sucesso!')

def listar_restaurantes():
    if not restaurantes:
        print('Nenhum restaurante cadastrado.')
    else:
        print('\nLista de Restaurantes:')
        for i, r in enumerate(restaurantes, start=1):
            status = 'Ativo' if r['ativo'] else 'Inativo'
            print(f"{i}. {r['nome']} ({r['categoria']}) - {status}")

def ativar_restaurante():
    listar_restaurantes()
    try:
        escolha = int(input('\nDigite o número do restaurante para ativar: '))
        restaurantes[escolha - 1]['ativo'] = True
        print(f'Restaurante "{restaurantes[escolha - 1]["nome"]}" ativado com sucesso!')
    except (IndexError, ValueError):
        print('Opção inválida.')

# Loop principal
while True:
    limpar_tela()
    exibir_menu()
    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        cadastrar_restaurante()
    elif escolha == '2':
        listar_restaurantes()
    elif escolha == '3':
        ativar_restaurante()
    elif escolha == '4':
        finalizar_app()
        break
    else:
        print('Opção inválida.')

    input('\nPressione Enter para continuar...')



