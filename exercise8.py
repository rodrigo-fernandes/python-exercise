# {} = Dicionário
# [] = Lista
cores = {'verde': 'green', 'vermelho':'red', 'preto':'black', 'branco':'whilte'}

# pega o que o usuário digitou e já transforma a letra em minúscula
cor = input('Escolha a cor que deseja traduzir: ').lower()

traducao = cores.get(cor, 'Esta cor não consta no dicionário')

print(traducao)