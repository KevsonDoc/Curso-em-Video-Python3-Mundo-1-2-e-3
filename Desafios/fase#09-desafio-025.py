# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome dela
nome = str(input('Digite o seu nome: ')).strip()
print('Seu nome tem Silva {}'.format('silva' in nome.lower()))
