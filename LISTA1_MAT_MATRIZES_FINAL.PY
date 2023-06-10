#inserindo matrizes randomicas

#mport numpy as np NESTE CASO NAO IREMOS USAR ARRANJO NP não chamamos função
import random   #importando função ramdomica

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
    if linha > 0 and coluna > 0:                   #teste se matriz é nula
        MATRIZ = []
        for i in range (linha):                    #Contador de linha
            LINHA = []
            for ii in range (coluna):              #Contador de coluna
                numero = random.randint(1,50)           #Função numero = Ramdom de 1 a 50
                LINHA.append(numero)                    #linha./Insert/(numero ramdom)
            MATRIZ.append(LINHA)                    #Matriz./insert/(LINHA)
    else:
        print('\n\nvocê não pode gerar uma matriz nula!\n\n')
        SyntaxError
    printLinha()    #print linha pontilhada

    print(MATRIZ)   #printa MATRIZ de madeira Bruta

    printLinha()
    print(nome)     #printa o nome da Matriz
    for i in range(linha):      #printa a matriz de maneira REFINADA
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
