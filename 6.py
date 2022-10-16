dados=[]
cont=0
valores = []
repetidos = set()

while cont<=19:
    dados.append(int(input("Insira um valor: ")))
    cont+=1


for dado in dados:
    if dado not in valores:
        valores.append(dado)

print(f'Valores = {valores}')
