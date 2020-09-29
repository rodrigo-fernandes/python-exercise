# imutáveis, ou seja, nunca é alterado
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)
print(type(meses))

# mutáveis, ou seja, a qualquer momento posso alterar
alunos = ['Rodrigo', 'Ana', 'Pedro', 'Helena']
print(alunos)
print(type(alunos))

print(len(meses))
print(len(alunos))

print(meses[11])
print(alunos[1])

alunos[1] = 'AnA'
print(alunos)

alunos.append('Joao')
print(alunos)

# adiciona no índice desejado
alunos.insert(1, 'Ricardo')
print(alunos)

alunos.sort()
print(alunos)

# excluí o índice
alunos.pop(1)
print(alunos)

# excluí pelo nome
alunos.remove('Ricardo')
print(alunos)

alunos2 = ['Joana', 'Jorge']
print(alunos2)

total = alunos + alunos2
print(total)
print(type(total))

print(total[2])

indice = 3
print(total[indice])