#inserindo matrizes randomicas

#import numpy as np NESTE CASO NAO IREMOS USAR ARRANJO NP não chamamos função
import random   #importando função ramdomica

def printLinha():
    print("-" * 60)
def printLinhavazia():
    print('\n')

def printMatriz(matriz):
    linhas = len(matriz)  # len = length = comprimento
    colunas = len(matriz[0])
    printLinha()    #print linha pontilhada

    print(matriz)   #printa MATRIZ de madeira Bruta

    printLinha()
    #print(nome)     #printa o nome da Matriz
    for i in range(linhas):      #printa a matriz de maneira REFINADA
        print("\n")
        
        for ii in range(colunas):
            
            print(matriz[i][ii], end = "(L{}C{}), " .format(i+1,ii+1))
        
    print('\n')

def CriaMatriz():
    print('\n vamos criar uma matriz dinamica em que voce nos diz as linhas e as colunas\n')
    printLinha()
    #nome = input("Diga um nome para esta matriz: ")

    linha = int(input("informe a quantidade de linhas para matriz: "))
    coluna = int(input("agora informe a quantidade de colunas da matriz: "))

    printLinha()
    print('A quantidade de linhas é:', linha)
    print('A quantidade de colunas é:', coluna)
    print('\nDefina o escopo para os numeros da matriz:')
    inicio = int(input('Qual decimal inicio do escopo? '))
    final = int(input('Qual decimal final do escopo? '))
    
    printLinha()

    if linha > 0 and coluna > 0:                   #teste se matriz é nula
        MATRIZ = []
        for i in range (linha):                    #Contador de linha
            LINHA = []
            for ii in range (coluna):              #Contador de coluna
                numero = random.randint(inicio,final)           #Função numero = Ramdom de 1 a 50
                LINHA.append(numero)                    #linha./Insert/(numero ramdom)
            MATRIZ.append(LINHA)                   #Matriz./insert/(LINHA)
        return MATRIZ
    else:
        print('\n\nvocê não pode gerar uma matriz nula!\n\n')

def ex1():
    printLinha()
    matriz1 = CriaMatriz()
    printMatriz(matriz1)

    printLinha()
    matriz2 = CriaMatriz()
    printMatriz(matriz2)

    printLinha()
    matriz3 = CriaMatriz()
    printMatriz(matriz3)

printLinhavazia()
print('bem vindo a lista de exercicios 1 de matrizes - ALUNO ANDREW 72409')
printLinha()

print('você tem as segintes opçoes para executar')
print('DIGITE ex1 PARA O PRIMEIRO EXERCICIO\n DIGITE cria para criar uma matriz randomica')
opcao = input('DIGITE SUA OPÇÃO: ')
if opcao == 'ex1':
    ex1()
if opcao == 'cria':
    printLinha()
    matriz0 = CriaMatriz()
    printMatriz(matriz0)
print('FINAL DA LINHA')