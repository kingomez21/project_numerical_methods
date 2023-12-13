import numpy as np 
import matplotlib.pyplot as plt
from matriz_d_x import m_x, m_j_x


def poblar_funciones(matriz_funciones, X, Y):
    nueva_matriz_funciones = list()
    for index, item in enumerate(matriz_funciones):
        nueva_matriz_funciones.append(item(X, Y))
    return np.array(nueva_matriz_funciones)

def poblar_jacobiano(matriz_jacobiana, X, Y):
    nueva_matriz_jacobiana = list()
    for row_index, row in enumerate(matriz_jacobiana):
        new_row = list()
        for column_index, column in enumerate(row):
            if callable(column):
                new_row.append(column(X, Y))
            else:
                new_row.append(column)
        nueva_matriz_jacobiana.append(new_row)
    return np.array(nueva_matriz_jacobiana)

def resolver_gaus_seidel(A, B, iteramax = 25):
    tolera = 0.0001

    # PROCEDIMIENTO
    # Gaus-Seidel
    tamano = np.shape(A)
    n = tamano[0] # número de filas
    m = tamano[1] # número de columnas

    X0 = np.zeros(n, dtype = float)
    # valores iniciales
    X = np.copy(X0)
    diferencia = np.ones(n, dtype = float)
    errado = 2*tolera

    i = 0
    itera = 0

    while not(errado <= tolera or itera > iteramax):
        for i in range(0, n, 1):
            suma = 0
            for j in range(0, m, 1):
                if (j != i):
                    suma = suma + A[i,j]*X[j]

            nuevo = (B[i] - suma)/A[i,i] # Esta sería la forma de obtener el nuevo valor de X[i]
            diferencia[i] = np.abs(nuevo - X[i]) # Es para calcular el error
            X[i] = nuevo

        #print(f'Iteración {itera}')
        #print(X)
        test = np.dot(A, X)
        #print(test)
        errado = np.max(diferencia)
        itera = itera + 1
    

    # revisa convergencia
    if (itera > iteramax):
        X = 0
    print("Los valores obtenidos por Gauss Seidel {}".format(X))
    return X

def conjugate_gradient(A, b, tolera = 1e-5, iteramax = 13):
    iter = 0
    n = A.shape[0]
    x = np.zeros(n)
    r = b - np.dot(A, x) # El gradiente negativo
    d = r # Dirección conjugada
    while np.linalg.norm(r) > tolera and iter <= iteramax:
        # Alpha controla la velocidad de convergencia
        alpha = np.divide(np.dot(np.transpose(r), r), np.dot(np.dot(np.transpose(d), A), d))
        x = x + np.dot(alpha, d)
        r_new = r - np.dot(np.dot(alpha, A), d)
        beta = np.divide(np.dot(np.transpose(r_new), r_new), np.dot(np.transpose(r), r))
        d = r_new + np.dot(beta, d)
        r = r_new
        iter = iter + 1
        #print(r)
    #print(x)
    #print("Valores de gradiente conjugado {}".format(x))
    return (x, iter)

def jacobi(a,b,x):
	n=len(x)
	t=x.copy()
	for  i  in  range(n):
		s=0
		for j in range(n):
			if i!=j:
				s=s+a[i,j]*t[j]
				x[i]=(b[i]-s)/a[i,i]
	return x


def jacobim(a,b):
    m =100
    x = np.zeros(39)
    e = 1.e-14
    #n = len(x)
    t = x.copy()
    for  k  in  range(m):
        x=jacobi(a,b,x)
        d=np.linalg.norm(np.array(x)-np.array(t),np.inf)
            #print ("Para la iteración "+str(k+1)+": X = "+str(np.transpose(x.round(7)))+"\tError: "+str(abs(d)))
        if d<e:
            return [x,k]
        else:
            t=x.copy()
    return [[],m]

if __name__ == "__main__":

    x0 = np.ones(39)
    y0 = np.ones(39)

    tolera = 0.0001
    diferencia = np.ones(39, dtype = float)
    errado = 2*tolera
    iter = 0
    iteramax = 13

    while np.linalg.norm(x0) > tolera and np.linalg.norm(y0) > tolera and iter <= iteramax:
        funciones_pobladas_x = poblar_funciones(m_x(), x0, y0)
        jacobiano_poblado_x = poblar_jacobiano(m_j_x(), x0, y0)
       
        gauss_seidel = resolver_gaus_seidel(jacobiano_poblado_x, -funciones_pobladas_x)
        #[x, i] = conjugate_gradient(jacobiano_poblado_x, -funciones_pobladas_x)
        #[x, k] = jacobim(jacobiano_poblado_x, -funciones_pobladas_x)

        x0 = x0 - gauss_seidel
        #x0 = x0 - x
        
        iter = iter + 1
        print(f'Iteración {iter}:')
        print(np.linalg.norm(x0))
        print(x0)
        print('---------------------')

    Solucion1 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, x0[0], 0, 0, 0, x0[1], x0[2], x0[3], x0[4], x0[5], 0],
        [1, x0[6], 0, 0, 0, x0[7], x0[8], x0[9], x0[10], 0, 0],
        [1, x0[11], x0[12], x0[13], x0[14], x0[15], x0[16], x0[17], 0, 0, 0],
        [1, x0[18], x0[19], x0[20], 0, 0, 0, x0[21], 0, 0, 0],
        [1, x0[22], x0[23], x0[24], 0, 0, 0, x0[25], x0[26], 0, 0],
        [1, x0[27], x0[28], x0[29], 0, 0, 0, x0[30], x0[31], x0[32], 0],
        [1, x0[33], x0[34], x0[35], 0, 0, 0, x0[36], x0[37], x0[38], 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    
    plt.figure()
    plt.imshow(Solucion1)
    plt.title( "2-D Heat Map" )
    plt.colorbar()
    plt.show()
    