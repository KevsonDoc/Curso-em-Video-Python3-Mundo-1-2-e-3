# Fça um programa que leia o nome completo de uma pessoa, e mostre em seguida
# o primeiro e o útimo nome separadamente.
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome) - 1]))