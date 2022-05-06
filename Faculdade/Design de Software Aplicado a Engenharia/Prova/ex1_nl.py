""" Implemente um programa que determine as seguintes operações:
• Nome: maior que 3 caracteres;
• Idade: entre 0 e 150;
• Salário: maior que 1000;
• Sexo: 'F' ou 'M';
• Estado Civil: 's', 'c', 'v', 'd'. """

#Nome
nome=str(input("informe um nome--> "))
while ( len(nome) <= 3 ):
    nome=str(input("informe um nome--> "))
#Idade
idade=int(input("informe a idade--> "))
while ( idade > 150 or idade < 0 ):
    idade=int(input("informe a idade--> "))
#Salario
salario=int(input("seu salário --> "))
while ( salario < 1000 ):
    salario=int(input("informe um salario--> "))
#Sexo: 
sexo=str(input("informe a inicial do seu sexo--> "))
while sexo !="f" and sexo!="m" :
    sexo=str(input("informe a inicial do seu sexo--> "))
#Estado Civil: 
estado_civil= str(input("informe a inicial do seu estado civil-->"))
while ( estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d" ):
    estado_civil=str(input("informe a inicial do seu estado civil-->"))

