cont=0
dados=[]
while cont<=14:
    dados.append(int(input("Insira um valor: ")))
    del(dados[0])
    cont+=1

for i in range(15):
    dados.insert(i,i+1)

print(dados)