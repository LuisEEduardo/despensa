"""
Implemente um controle simples de mercadorias em uma despensa doméstica. Para
cada produto armazene um codigo numérico, descrição e quantidade atual. O programa
deve ter opções para entrada e retirada de produtos, bem como um relátorio geral e um
de um produtos não disponíveis. Armazene os dados em arquivo binário.


Produto:
    - Deve ter:
        -> codigo numérico
        -> descrição
        -> quantidade atual

-> Funções
- Cadastrar um produto
- Retirar produto
- Atualizar (qtd de produto)
- Gerar relátorio
    - de produtos não disponiveis
    - geral (mostrando todos os produtos)
- Armazenamento
    - os dados devem estar em binário
"""


def define_codigo_numerico():
    from random import randint
    return randint(1, 100)


def get_retira_qtd_atual(conteudo):
    pos1 = conteudo.index('-') + 1
    pos2 = conteudo.index('-', pos1 + 1)
    conteudo_novo = conteudo[:pos2]
    return  conteudo_novo


def get_qtd_atual(conteudo):
    pos1 = conteudo.index('-') + 1
    pos2 = conteudo.index('-', pos1 + 1)
    qtd = conteudo[pos2 + 2:].strip().replace('\n', '')
    return int(qtd)


def get_descricao(conteudo):
    pos1 = conteudo.index('-') + 1
    pos2 = conteudo.index('-', pos1 + 1)
    descricao = conteudo[pos1:pos2].strip()
    return descricao.strip()


def get_codigo_produto(conteudo):
    pos = conteudo.index('-')
    return int(conteudo[:pos].strip())


# Cadastrar Produto ------------------------------------
def cadastrar_produto(descricao, qtd):
    with open('despensa.txt', 'a') as arq:
        cod = define_codigo_numerico()
        arq.write(f'{cod} - {descricao} - {qtd}\n')
    print('Produto Cadastrado')


# Retirar Produto -------------------------------------
def retirar_produto(nome_produto):
    nova_lista_de_produtos = []
    with open('despensa.txt', 'r') as arq:
        arq_ref = arq.readlines()
        for produto in arq_ref:
            if get_descricao(produto).lower() != nome_produto.lower():
                nova_lista_de_produtos.append(produto)
    with open('despensa.txt', 'w') as arq:
        arq.writelines(nova_lista_de_produtos)
        print("Retirada com sucesso")


# Atualizar Produto------------------------------------
def atualizar_produto(nome_produto, qtd_nova):
    nova_lista_de_produtos = []
    with open('despensa.txt', 'r') as arq:
        arq_ref = arq.readlines()
        for produto in arq_ref:
            if get_descricao(produto).lower() == nome_produto:
                nova_lista_de_produtos.append(f'{get_retira_qtd_atual(produto)} - {qtd_nova}')
            else:
                nova_lista_de_produtos.append(produto)
    with open('despensa.txt', 'w') as arq:
        arq.writelines(nova_lista_de_produtos)
    print('Atualização realizada com sucesso')


# Relatório -----------------------------------------
def gerar_relatorio_de_produto_n_disponiveis():
    with open('despensa.txt', 'r') as arq:
        arq_ref = arq.readlines()
        print('Código  |  Descrição  | Quantidade')
        for produto in arq_ref:
            if get_qtd_atual(produto) == 0:
                print(produto, end='')


# Relatório Geral ------------------------------------
def gerar_relatorio_geral():
    with open('despensa.txt', 'r') as arq:
        arq_ref = arq.readlines()
        print('Código  |  Descrição  | Quantidade')
        for produto in arq_ref:
            print(produto, end='')


# Clean ----------------------------------------------
def clean():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


# Rotina Principal -----------------------------------
clean()
print("""Bem-vindo a dispensa =)
Escolha a opção desejada: 
1 - Cadastrar um produto
2 - Retirar produto
3 - Atualizar produto
4 - Gerar relátorio completo   
5 - Gerar relátorio parcial
6 - sair  
""")
op = int(input('Insira a opção desejada: '))
while op != 6:
    clean()
    if op == 1:
        nome_produto = input('Insira o nome do produto: ')
        qtd = int(input('Insira a quantidade de produtos: '))
        cadastrar_produto(nome_produto, qtd)
    elif op == 2:
        nome_produto = input('Insira o nome do produto: ')
        retirar_produto(nome_produto)
    elif op == 3:
        nome_produto = input('Insira o nome do produto: ')
        qtd = int(input('Insira a nova quantidade: '))
        atualizar_produto(nome_produto, qtd)
    elif op == 4:
        gerar_relatorio_geral()
    elif op == 5:
        gerar_relatorio_de_produto_n_disponiveis()
    else:
        print('Número Incorreto')
    print('\n')
    op = int(input('Insira a opção desejada: '))
print("Até mais =)")
