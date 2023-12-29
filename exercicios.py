# Listas

# Exercício 1

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nomes = ['Laura', 'Luiza', 'Leandro', 'Larissa']

anos = [2005, 2023]

# Exercicio 2

pais_de_cabeça = ['Oxóssi', 'Iemanja', 'Xango', 'Oxum']

for pai_de_cabeca in pais_de_cabeça:
    print(pai_de_cabeca)

# Exercício 3

soma_numeros = 0

for n in range(1, 11, 2):
    soma_numeros += n

print(soma_numeros)

# Exercicio 4

numeros_ordem_decrescente = []

for n in range(10, 0, -1):
    numeros_ordem_decrescente.append(n)

print(numeros_ordem_decrescente)

# Exercício 5

numero_escolhido = int(input('Digite o número que você deseja ver a tabuada: '))

for n in range(1, 11):
    resultado = numero_escolhido * n
    print(f'{numero_escolhido} x {n} = {resultado}')

# Exercício 6

soma = 0
numeros = [5, 16, 84, 13]


try:
    for n in numeros:
        soma += n
    print(f'O resultado da soma é {soma}')
except Exception as e:
    print(f'Ocorreu um erro: {e}')

# Exercicio 7

soma = 0
numeros = [7, 8, 10, 3, 5]

try:
    for n in numeros:
        soma += n
    media = soma/len(numeros)
    print(f'A média dos valores é {media}')

except ZeroDivisionError:
    print('A lista está vazia, não é possível tirar a média')

except Exception as e:
    print(f'Ocorreu um erro: {e}')

# Dicionarios

# Exercicio 1

pessoa = {'nome':'Laura', 'idade': 18, 'cidade':'São Paulo'}
print(pessoa)

# Exercicio 2

pessoa['idade'] = 19
print(pessoa)
pessoa.update({'profissao':'Advogada'})
print(pessoa)
pessoa.pop('cidade')
print(pessoa)

# Exercicio 3

numero_quadrados = {x**2 for x in range(1, 6)}
print(numero_quadrados)

# Exercicio 4

if 'nome' in pessoa:
    print('A chave "nome" existe no dicionario.')
else:
    print('A chave "nome" não existe no dicionário')

# Exercicio 5
    
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)


