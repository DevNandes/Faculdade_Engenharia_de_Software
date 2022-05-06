""" Ex2. Verifique o funcionamento do seguinte programa """
""" contador = 0 # Inicializa o contador
somador = 0 # Inicializa o somador
while contador < 5: # Executa sempre que o contador seja menor que 5.
# Observação. Se contador é igual a 5 o seguinte código não será executado
 # Inicio do código dentro do while. Verifique a indentação
 contador = contador + 1
 valor = float(input(f'Digite o {contador}º valor: '))
 somador = somador + valor
 # Final do código do while.
# Linhas de código a serem executadas somente quando finalizar o while 
(contador >=5)
print('Soma = ', somador) """
""" Tarefa:
• Inicialize a variável contador em 10
• Modifique a expressão do while para que o programa se repita sempre que o contador seja maior 
que zero.
• Modifique o programa de modo que decremente a variável contador em vez de inctementar.
• Execute o programa, verifique o valor da variável somador e confira o resultado
• Novamente modifique o programa para que o programa se repita sempre que o contador seja maior 
ou igual que 5 e menor ou igual que 10 """

cont = 0
contador = 10
somador = 0
while contador >= 5 and contador <= 10:
    contador = contador - 1
    cont = cont + 1
    valor = float(input(f'Digite o {cont}º valor: '))
    somador = somador + valor
print('Soma = ', somador)