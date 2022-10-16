from random import randint

vetor=[0]*50
maior=0
menor=0

for i in range(50):
    vetor[i]=randint(0, 20)
    soma=sum(vetor)
    
    print(f"{vetor[i]}")
    
    cont=vetor.count(9)

    if (vetor[i] > maior): 
        maior = vetor[i]
    
    if (vetor[i] < menor): 
        menor = vetor[i]

#Letra a
print(soma)

#Letra b
print(cont)

#Letra c
print(maior)

#Letra d
print(menor)