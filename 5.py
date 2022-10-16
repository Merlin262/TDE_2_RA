dados=[]
cont=0
valores = []
repetidos = set()

while cont<=9:
    dados.append(int(input("Insira um valor: ")))
    cont+=1


for dado in dados:
    if dado not in valores:
        valores.append(dado)
    else:
        repetidos.add(dado)
print(f'Valores = {valores}')
print(f'Repetidos = {repetidos}')