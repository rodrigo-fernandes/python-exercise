# {} = Dicionário
# [] = Lista
joao = {'nome': 'joao', 'sobrenome':'pereira', 'profissão': 'programador python', 'filhos': ['pedro', 'maria']}

print(type(joao))

print(joao['sobrenome'])

print(joao['profissão'])

print(joao['filhos'])

# tamanho do elementos do dicionário
print(len(joao))

# exclui a lista filhos
del joao['filhos']
print(joao)

joao['profissão'] = 'aponsentado'
print(joao)

# verifica se existe uma chave dentro do dicionário
print('sobrenome' in joao)

# percorre todos os elementos de dentro do dicionário e imprimi
for x in joao:
    print(x)

for x in joao:
    print(x +': '+ joao[x])

print(joao.get('nome', 'Esta informacao não consta no dicionário'))
print(joao.get('idade', 'Esta informacao não consta no dicionário'))

# adiciona os filhos novamente
joao['filhos'] = ['pedro', 'maria']
print(joao)

# adiciona um item a lista
joao['filhos'].append('jorge')
print(joao)

# limpa o dicionário
joao.clear()
print(joao)