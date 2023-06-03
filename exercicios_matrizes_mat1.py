#inserindo matrizes randomicas
import random


print('\n vamos criar uma matriz dinamica em que voce nos dis as linhas e as colunas\n')
linha = int(input("informe a quantidade de linhas para matriz: "))
coluna = int(input("agora informe a quantidade de colunas da matriz: "))

if linha > 0 and coluna > 0:
    MATRIZ = []
    for i in range (linha):
        LINHA = []
        for ii in range (coluna):
            numero = random.randint(1,50)
            LINHA.append(numero)
        MATRIZ.append(LINHA)
else:
    print('\n\nvocê não pode gerar uma matriz nula!\n\n')
    SyntaxError

print(MATRIZ)

for i in range(linha):
    print("\n")
    for ii in range(coluna):
        print(MATRIZ[i][ii], end = ", ")
print('\n')



            

    
