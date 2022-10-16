vetorA=[1,2,3,4,5,6,7,8,9,10]
vetorB=[11,12,13,14,15,16,17,18,19,20]
vetorC=[0]*20

for i in range(20):
    if (i%2==0):
        vetorC[0]=vetorA[0]
        vetorC[2]=vetorA[1]
        vetorC[4]=vetorA[2]
        vetorC[6]=vetorA[3]
        vetorC[8]=vetorA[4]
        vetorC[10]=vetorA[5]
        vetorC[12]=vetorA[6]
        vetorC[14]=vetorA[7]
        vetorC[16]=vetorA[8]
        vetorC[18]=vetorA[9]
    else:
        vetorC[1]=vetorB[0]
        vetorC[3]=vetorB[1]
        vetorC[5]=vetorB[2]
        vetorC[7]=vetorB[3]
        vetorC[9]=vetorB[4]
        vetorC[11]=vetorB[5]
        vetorC[13]=vetorB[6]
        vetorC[15]=vetorB[7]
        vetorC[17]=vetorB[8]
        vetorC[19]=vetorB[9]

print(vetorC)