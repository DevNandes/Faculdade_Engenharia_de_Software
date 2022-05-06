""" Utilizando While, implemente o programa anterior considerando N números. Isto quer dizer, tantos 
números como o usuário desejar. Criar um critério de parada para evitar ciclo infinito. """
tam= int(input('Quantos números você deseja adicionar na sua lista: '))
lista=[]
while len(lista) < tam:
    n = int(input('Digite um numero: '))
    lista.append(n)

max_value = max(lista)
print(f'O maior valor de seus números é:{max_value}')
soma = sum(lista)
print(f'A soma dos seus valores é de:{soma}')
len = len(lista)
média = soma/len
print(f'A média de seus valores é:{média}')
numbers_filter= [number for number in lista if number <=100]
print(f'Os números menores que 100 são: {numbers_filter}')

