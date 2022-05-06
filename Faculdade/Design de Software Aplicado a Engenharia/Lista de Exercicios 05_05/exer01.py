""" Ex1. Verifique o funcionamento do seguinte programa
nome = input("Digite seu nome: ") # Recebe um valor Str
idade = int(input("Digite sua idade: ")) # Recebe um valor Str e o converte 
para int
print("Bem vindo ", nome,"!") # Imprime como saída (no Terminal) um texto e o 
valor da variável “nome”
print("Sua é idade é ",idade)
# Forma alternativa para imprimir valores de variáveis dentro do texto
print(f"\nBem vindo {nome}! \nSua idade {idade}")
Tarefa:
• Implemente um programa que receba os dados referentes a Nome, Peso (kg) e Altura (cm)]
• Cada dado deve ser atribuído a variáveis de tipo inteira, float e string, respectivamente
• Imprima novamente os valores numa única frase.  
int= numeros inteiros
float= numeros quebrados
"""
nome = input("Digite seu nome: ")
altura = int(input(f"Digite sua altura em centimetros, {nome}: "))
peso = float(input(f"Digite seu peso em kilogramas, {nome}: "))

print(f"\nBem vindo, {nome}! \nSua altura é de {altura} cm! \nSeu peso é de {peso} kg")