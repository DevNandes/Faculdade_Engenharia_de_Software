""" Ex3. Verifique o funcionamento do seguinte programa
senha = "54321"                                 # Senha a ser ingressada
leitura =" "                                    # Inicializa variável como vacía
while (leitura != senha):                       # Compara duas sequências de carateres.Somente realiza o ciclo caso sejam diferentes
    leitura = input("Digite a senha: ")            # Variável Leitura recebe a entrada ingressada pelo usuário
    if leitura == senha :                          # Verifica se as duas sequências de carateres são iguais
        print('Acesso liberado ')                      # Caso sejam iguais
    else: 
        print('Senha incorreta. Tente novamente')      # Caso sejam diferentes
Tarefa
• Modifique o programa para que se encerre após realizar 5 tentativas erradas. """

contador = 5
senha = "54321"
leitura = " "
while (leitura != senha):
    contador = contador - 1
    if contador >= 0: 
        leitura = input("Digite a senha: ")
        if leitura == senha:
            print('Acesso liberado ')
        else:
            print('Senha incorreta. Tente novamente')
    else:
        print("Você esgotou as tentativas, volte mais tarde!")
        break