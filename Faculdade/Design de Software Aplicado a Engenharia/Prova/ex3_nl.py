""" Utilizando FOR, implemente um programa que leia 5 números de um usuário e informe:
• O número maior
• O valor acumulado
• A média dos números
• Os números entre 0 e 100 """
count = 0
lista=[]
print("Você poderá digitar 5 numeros diferente!")
for count in range(0,5):
    n = int(input('Digite um número: '))
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