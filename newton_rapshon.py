import numpy as np 
import matplotlib.pyplot as plt
from matriz_d_x import m_x, m_j_x
from matriz_d_y import m_y, m_j_y
from interpolacion_d_x import funcion_ui_x
from interpolacion_d_y import funcion_vi_y

def polinomio_resultante_d_x(x0, v_x, v_y):

    result = ( (funcion_ui_x[0](v_x)
                *( 
                   x0[0]*funcion_vi_y[0](v_y) + 
                   x0[6]*funcion_vi_y[1](v_y) +
                   x0[11]*funcion_vi_y[2](v_y) +
                   x0[18]*funcion_vi_y[3](v_y) +
                   x0[22]*funcion_vi_y[4](v_y) +
                   x0[27]*funcion_vi_y[5](v_y) +
                   x0[33]*funcion_vi_y[6](v_y) 
                   #x0[0]*funcion_vi_y[7](v_y) +
                   #x0[0]*funcion_vi_y[8](v_y) 
                 )) + 
                  (funcion_ui_x[1](v_x)
                *( 
                   x0[1]*funcion_vi_y[0](v_y) + 
                   x0[7]*funcion_vi_y[1](v_y) +
                   x0[12]*funcion_vi_y[2](v_y) +
                   x0[19]*funcion_vi_y[3](v_y) +
                   x0[23]*funcion_vi_y[4](v_y) +
                   x0[28]*funcion_vi_y[5](v_y) +
                   x0[34]*funcion_vi_y[6](v_y) 
                   #x0[0]*funcion_vi_y[7](v_y) +
                   #x0[0]*funcion_vi_y[8](v_y) 
                 )) +
                  (funcion_ui_x[2](v_x)
                *( 
                   x0[3]*funcion_vi_y[0](v_y) + 
                   x0[8]*funcion_vi_y[1](v_y) +
                   x0[13]*funcion_vi_y[2](v_y) +
                   x0[20]*funcion_vi_y[3](v_y) +
                   x0[24]*funcion_vi_y[4](v_y) +
                   x0[29]*funcion_vi_y[5](v_y) +
                   x0[35]*funcion_vi_y[6](v_y) 
                   #x0[0]*funcion_vi_y[7](v_y) +
                   #x0[0]*funcion_vi_y[8](v_y) 
                 )) + 
                  (funcion_ui_x[3](v_x)
                *( 
                   x0[4]*funcion_vi_y[0](v_y) + 
                   x0[9]*funcion_vi_y[1](v_y) +
                   x0[14]*funcion_vi_y[2](v_y) +
                   x0[21]*funcion_vi_y[3](v_y) +
                   x0[25]*funcion_vi_y[4](v_y) +
                   x0[30]*funcion_vi_y[5](v_y) +
                   x0[36]*funcion_vi_y[6](v_y) 
                   #x0[0]*funcion_vi_y[7](v_y) +
                   #x0[0]*funcion_vi_y[8](v_y) 
                 )) + 
                 (funcion_ui_x[4](v_x)
                *( 
                   x0[5]*funcion_vi_y[0](v_y) + 
                   x0[10]*funcion_vi_y[1](v_y) +
                   x0[15]*funcion_vi_y[2](v_y) +
                   x0[22]*funcion_vi_y[3](v_y) +
                   x0[26]*funcion_vi_y[4](v_y) +
                   x0[31]*funcion_vi_y[5](v_y) +
                   x0[37]*funcion_vi_y[6](v_y) 
                   #x0[0]*funcion_vi_y[7](v_y) +
                   #x0[0]*funcion_vi_y[8](v_y) 
                 )) + 
                 (funcion_ui_x[5](v_x)
                *( 
                   x0[6]*funcion_vi_y[0](v_y) + 
                   x0[11]*funcion_vi_y[1](v_y) +
                   x0[16]*funcion_vi_y[2](v_y) +
                   x0[23]*funcion_vi_y[3](v_y) +
                   x0[27]*funcion_vi_y[4](v_y) +
                   x0[32]*funcion_vi_y[5](v_y) +
                   x0[38]*funcion_vi_y[6](v_y) 
                   #x0[0]*funcion_vi_y[7](v_y) +
                   #x0[0]*funcion_vi_y[8](v_y) 
                 )) + 
                 (funcion_ui_x[6](v_x)
                *( 
                   x0[7]*funcion_vi_y[0](v_y) + 
                   x0[12]*funcion_vi_y[1](v_y) +
                   x0[17]*funcion_vi_y[2](v_y) +
                   x0[24]*funcion_vi_y[3](v_y) +
                   x0[28]*funcion_vi_y[4](v_y) +
                   x0[33]*funcion_vi_y[5](v_y) +
                   x0[38]*funcion_vi_y[6](v_y) 
                   #x0[0]*funcion_vi_y[7](v_y) +
                   #x0[0]*funcion_vi_y[8](v_y) 
                 )))

    return result

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
    #print("Los valores obtenidos por Gauss Seidel {}".format(X))
    return X

def conjugate_gradient(A, b, tolera = 1e-5, iteramax = 17):
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
    return [x, iter]

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
            result = []
            print(x)
            for i in range(len(x)):
                 result.append(x[i])
            return [result, k]
            
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
    iteramax = 4

    while np.linalg.norm(x0) > tolera and np.linalg.norm(y0) > tolera and iter <= iteramax:
        funciones_pobladas_x = poblar_funciones(m_x(), x0, y0)
        jacobiano_poblado_x = poblar_jacobiano(m_j_x(), x0, y0)

        funciones_pobladas_y = poblar_funciones(m_y(), x0, y0)
        jacobiano_poblado_y = poblar_jacobiano(m_j_y(), x0, y0)
       
        gauss_seidel_x = resolver_gaus_seidel(jacobiano_poblado_x, -funciones_pobladas_x)
        gauss_seidel_y = resolver_gaus_seidel(jacobiano_poblado_y, -funciones_pobladas_y)


        #[x, i] = conjugate_gradient(jacobiano_poblado_x, -funciones_pobladas_x)
        #[m_jacobi, k] = jacobim(jacobiano_poblado_x, -funciones_pobladas_x)
        #gc2 = gradienteConjugado(jacobiano_poblado_x, -funciones_pobladas_x)


        x0 = x0 - gauss_seidel_x
        y0 = y0 - gauss_seidel_y
        
        iter = iter + 1
        #print(f'Iteración {iter}:')
#        print(np.linalg.norm(x0))
#        print(x0)
        #print(np.linalg.norm(y0))
        #print(y0)
        #print('---------------------')

    result = [
         polinomio_resultante_d_x(x0, 0, 0),
         polinomio_resultante_d_x(x0, 1, 0),
         polinomio_resultante_d_x(x0, 2, 0),
         polinomio_resultante_d_x(x0, 3, 0),
         polinomio_resultante_d_x(x0, 4, 0),
         polinomio_resultante_d_x(x0, 5, 0),
         polinomio_resultante_d_x(x0, 6, 0),
         polinomio_resultante_d_x(x0, 7, 0),
         polinomio_resultante_d_x(x0, 8, 0),
         polinomio_resultante_d_x(x0, 9, 0),
         polinomio_resultante_d_x(x0, 10, 0),
         polinomio_resultante_d_x(x0, 2, 1),
         polinomio_resultante_d_x(x0, 3, 1),
         polinomio_resultante_d_x(x0, 4, 1),
         polinomio_resultante_d_x(x0, 10, 1),
         polinomio_resultante_d_x(x0, 2, 2),
         polinomio_resultante_d_x(x0, 3, 2),
         polinomio_resultante_d_x(x0, 4, 2),
         polinomio_resultante_d_x(x0, 10, 2),
    ]

    print(result)

    Solucion1 = [
        [result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10]],
        [1, x0[0], result[11], result[12], result[13], x0[1], x0[2], x0[3], x0[4], x0[5], result[14]],
        [1, x0[6], result[15], result[16], result[17], x0[7], x0[8], x0[9], x0[10], result[18], 0],
        [1, x0[11], x0[12], x0[13], x0[14], x0[15], x0[16], x0[17], 0, 0, 0],
        [1, x0[18], x0[19], x0[20], 0, 0, 0, x0[21], 0, 0, 0],
        [1, x0[22], x0[23], x0[24], 0, 0, 0, x0[25], x0[26], 0, 0],
        [1, x0[27], x0[28], x0[29], 0, 0, 0, x0[30], x0[31], x0[32], 0],
        [1, x0[33], x0[34], x0[35], 0, 0, 0, x0[36], x0[37], x0[38], 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    Solucion2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, y0[0], 0, 0, 0, y0[1], y0[2], y0[3], y0[4], y0[5], 0],
        [0, y0[6], 0, 0, 0, y0[7], y0[8], y0[9], y0[10], 0, 0],
        [0, y0[11], y0[12], y0[13], y0[14], y0[15], y0[16], y0[17], 0, 0, 0],
        [0, y0[18], y0[19], y0[20], 0, 0, 0, y0[21], 0, 0, 0],
        [0, y0[22], y0[23], y0[24], 0, 0, 0, y0[25], y0[26], 0, 0],
        [0, y0[27], y0[28], y0[29], 0, 0, 0, y0[30], y0[31], y0[32], 0],
        [0, y0[33], y0[34], y0[35], 0, 0, 0, y0[36], y0[37], y0[38], 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    
    plt.figure()
    plt.imshow(Solucion1)
    plt.title( "2-D Heat Map" )
    plt.colorbar()
    plt.show()