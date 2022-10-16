numero=[]
cont=0
while cont<=5:
    numero.append(int(input("Insira um valor: ")))
    cont+=1
numero.reverse()
print(numero)