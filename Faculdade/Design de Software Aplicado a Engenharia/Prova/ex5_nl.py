""" Implemente um programa que determine se um número é primo. Um número primo é aquele que é 
divisível somente por ele mesmo e por 1. """
num = int(input("Digite um número inteiro: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "Não é primo")
            break
    else:
        print(num, "É primo")
 
else:
    print(num, "Não é primo")