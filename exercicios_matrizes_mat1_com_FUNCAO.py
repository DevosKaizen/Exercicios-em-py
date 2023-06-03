#inserindo matrizes randomicas
import random

def printLinha():
    print("-" * 60)
def printLinhavazia():
    print('\n')

def CriaMatriz():
    print('\n vamos criar uma matriz dinamica em que voce nos dis as linhas e as colunas\n')
    printLinha()
    nome = input("Diga um nome para esta matriz: ")

    linha = int(input("informe a quantidade de linhas para matriz: "))
    coluna = int(input("agora informe a quantidade de colunas da matriz: "))

    printLinha()
    print(' o nome desta matriz é:', nome)
    print(' a quantidade de linhas é:', linha)
    print(' a quantidade de colunas é:', coluna)
    
    printLinha()

    print(nome)
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
    printLinha()

    print(MATRIZ)

    printLinha()
    print(nome)
    for i in range(linha):
        print("\n")
        for ii in range(coluna):
            print(MATRIZ[i][ii], end = ", ")
    print('\n')

printLinha()
CriaMatriz()
printLinha()
CriaMatriz()
printLinha()
CriaMatriz()
