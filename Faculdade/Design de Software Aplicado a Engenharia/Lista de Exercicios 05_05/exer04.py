""" Ex4. Verifique o funcionamento do seguinte programa
nums = [10, 20, 30, 40, 50, 100, 200, 500]
for i in nums:
 print('Estado de i: ',i) 
Tarefa
Modifique o programa para que no lugar dos número, imprima como estado de i os seguintes dados:
• Nome
• Curso
• Período
• Ano de início
• Data de hoje """

Nome = input('Digite seu nome: ')
Curso = input(f'Digite seu curso, {Nome}: ')
Período = int(input(f'Digite o número do seu periodo, {Nome}: '))
Ano_de_início = int(input(f'Digite o número do seu ano de inicio, {Nome}: '))
Data_de_hoje = input(f'Digite a data e hoje, {Nome}: ')

lista = [Nome, Curso, Período, Ano_de_início, Data_de_hoje]
for i in lista:
    print(i)
