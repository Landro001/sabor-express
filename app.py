import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_do_programa():
    ''' Essa opção é responsável por exibir o nome da aplicação '''
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibir_opcoes():
    ''' Essa função é responsável por exibir as opções do menu principal '''
    print('[1]. Cadastrar restaurante')
    print('[2]. Listar restaurante')
    print('[3]. Alternar estado do restaurante')
    print('[4]. Sair\n')

def finalizar_app():
    ''' Essa função é responsável por finalizar a aplicação '''
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    ''' Essa função é responsável por retornar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    input('\nDigite uma tecla para voltar para o menu principal ')
    main()

def opcao_invalida():
    ''' Essa função é responsável por informar quando uma opção é inválida 
    
    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção Inválida!')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    ''' Essa função é responsável por exibir o subtítulo
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante: str
    - Categoria: str

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes 

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Essa função é responsável por listar todos os restaurantes cadastrados 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('Listando os restaurantes')

    print(f'{"Nome do Restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    ''' Essa função é responsável por alternar o estado do restaurante entre 'ativado' e 'desativado' 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mesagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mesagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcaos():
    ''' Solicita e executa a opção escolhida pelo usuário
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()
        
def main():
    ''' Essa função é responsável por iniciar a aplicação '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcaos()

if __name__ == '__main__':
    main()