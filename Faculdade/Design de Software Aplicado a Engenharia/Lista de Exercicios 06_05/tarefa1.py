""" Tarefa 1
1. Escreva um programa que imprima as seguintes informações da lista:
• Tamanho da lista.
• Maior valor da lista.
• Menor valor da lista.
• Soma de todos os elementos da lista.
• Lista em ordem crescente.
• Lista em ordem decrescente. """

Lista_ex = [1, 30, 40, 10, 70, 71, 100]
print(len(Lista_ex))
print(max(Lista_ex))
print(min(Lista_ex))
print(sum(Lista_ex))
Lista_ex.sort()
print(Lista_ex)
Lista_ex.reverse()
print(Lista_ex)
