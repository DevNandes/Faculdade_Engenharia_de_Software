""" Utilizando a função range, escreva uma lista que contenha os múltiplos de 7 entre 1 e 50.
• Imprima a lista final
• Considereando a lista final (não o contador do loop) indique quantos números 
compreendem a lista
• Utilizando a lista anteriormente criada, continúe a lista até o número 100
• Verifique se os seguintes valores pertencem à lista: i) 37; ii) 53; iii) 81
• Imprima a lista em ordem descendente """
l=[]
l2 = []
for i in range (1,50):
    if i%7==0:
        l.append(i)
print(len(l))
for x in range (50,100):
    if x%7==0:
        l2.append(x)
l.extend(l2)
print(len(l))
print(37 in l)
print(53 in l)
print(81 in l)
l.reverse()
print(l)
    
    