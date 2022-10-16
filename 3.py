vetor=[]
numero=0

while True:
    numero=int(input("Insira um número: "))
    if numero<0:
        break
    else: 
        vetor.append(numero)

#Letra a
print(vetor)

#Letra b, c, d
numeroPar=[]
numeroImpar=[]
for valor in vetor:
    if valor % 2 == 0:
        numeroPar.append(valor)
    else:
        numeroImpar.append(valor)
print(f"{numeroPar}")
print(f"{numeroImpar}")
print(len(vetor))

