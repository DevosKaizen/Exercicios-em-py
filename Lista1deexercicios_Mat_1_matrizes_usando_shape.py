import numpy as np           #import biblioteca

def CriarMat():
    A = np.array([[1, 2, 4],
                  [-3, 0,-1],
                  [2, 1, 2]])

    B = np.array([[2, 0, 0],
                  [1, -4, 3],
                  [-1, 3, 2]])
    print('matriz A :\n', A)
    print('matriz B :\n', B)
    
    print('\n(usando shape) As dimençôes da Matriz A é:', A.shape)
    print('(usando size) A quantidade de dados da Matriz A é:', A.size)
    print('(usando ndim) As dimençôes no total da Matriz A é:', A.ndim)
    print('\n')
    print('\n(usando shape) As dimençôes da Matriz B é:', B.shape)
    print('(usando size) A quantidade de dados da Matriz B é:', B.size)
    print('(usando ndim) As dimençôes no total da Matriz B é:', B.ndim)
    print('\n')

    A23 = A[2, 2]
    print('o valor da matriz A[2, 2] é:',A23)
    #if np.array(A[4, 5]) =/ true
        #A45 = np.array(A[4, 5]) 
    #else print('valor A[4, 5] nao existe na matriz A')
    #A17 = A[1, 7] valor nao existe na matriz A
    #A33 = A[3, 3] valor nao existe na matriz A
    print('valor A[4, 5] nao existe na matriz A')
    print('valor A[1, 7] nao existe na matriz A')
    print('valor A[3, 3] nao existe na matriz A')

    #print('a busca da matriz A23 é {}\n da matriz A45 é {} \nda matriz A17 é {}\n da matriz A33 é' .format(A23))
    print('\n o unico valor possivel de acessar na matriz A é' ,np.array(A[2,2]))

    


CriarMat()