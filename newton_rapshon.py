import numpy as np 
import matplotlib as plt



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

if __name__ == "__main__":

    m_funcion_x = list()
    m_funcion_jacobiana_x = list()

    m_funcion_x.append(lambda U,V: (U[0] / 2)*(0 - 1) + (V[0] / 2)*(U[6] - 0) - 0 - 1 + 4*U[0] - U[6] - 0)
    m_funcion_x.append(lambda U,V: (U[1] / 2)*(U[2] - 0) + (V[1] / 2 )*(U[7] - 0) - U[2] - 0 + 4*U[1] - U[7] - 0)
    m_funcion_x.append(lambda U,V: (U[2] / 2)*(U[3] - U[1]) + (V[2] / 2 )*(U[8] - 0) - U[3] - U[1] + 4*U[2] - U[8] - 0)
    m_funcion_x.append(lambda U,V: (U[3] / 2)*(U[4] - U[2]) + (V[3] / 2 )*(U[9] - 0) - U[4] - U[2] + 4*U[3] - U[9] - 0)
    m_funcion_x.append(lambda U,V: (U[4] / 2)*(U[5] - U[3]) + (V[4] / 2 )*(U[10] - 0) - U[5] - U[3] + 4*U[4] - U[10] - 0)
    m_funcion_x.append(lambda U,V: (U[5] / 2)*(0 - U[4]) + (V[5] / 2 )*(0 - 0) - U[4] - 0 + 4*U[5] - 0 - 0)
    m_funcion_x.append(lambda U,V: (U[6] / 2)*(0 - 1) + (V[6] / 2 )*(U[11] - U[0]) - 0 - 1 + 4*U[6] - U[11] - U[0])
    m_funcion_x.append(lambda U,V: (U[7] / 2)*(U[8] - 0) + (V[7] / 2 )*(U[15] - U[1]) - U[8] - U[3] + 4*U[7] - U[15] - U[1])
    m_funcion_x.append(lambda U,V: (U[8] / 2)*(U[9] - U[7]) + (V[8] / 2 )*(U[16] - U[2]) - U[9] - U[7] + 4*U[8] - U[16] - U[2])
    m_funcion_x.append(lambda U,V: (U[9] / 2)*(U[10] - U[8]) + (V[9] / 2 )*(U[17] - U[3]) - U[10] - U[8] + 4*U[9] - U[17] - U[3])
    m_funcion_x.append(lambda U,V: (U[10] / 2)*(0 - U[9]) + (V[10] / 2 )*(0 - U[4]) - 0 - U[9] + 4*U[10] - 0 - U[4])    
    m_funcion_x.append(lambda U,V: (U[11] / 2)*(U[12] - 1) + (V[4] / 2 )*(U[18] - U[6]) - U[12] - 1 + 4*U[11] - U[18] - U[6])
    m_funcion_x.append(lambda U,V: (U[12] / 2)*(U[13] - U[11]) + (V[12] / 2 )*(U[19] - 0) - U[13] - U[11] + 4*U[12] - U[19] - 0)
    m_funcion_x.append(lambda U,V: (U[13] / 2)*(U[14] - U[12]) + (V[13] / 2 )*(U[20] - 0) - U[14] - U[12] + 4*U[13] - U[20] - 0)
    m_funcion_x.append(lambda U,V: (U[14] / 2)*(U[15] - U[13]) + (V[14] / 2 )*(0 - 0) - U[15] - U[13] + 4*U[14] - 0 - 0)
    m_funcion_x.append(lambda U,V: (U[15] / 2)*(U[16] - U[14]) + (V[15] / 2 )*(0 - U[7]) - U[16] - U[14] + 4*U[15] - 0 - U[7])
    m_funcion_x.append(lambda U,V: (U[16] / 2)*(U[17] - U[15]) + (V[16] / 2 )*(0 - U[8]) - U[17] - U[15] + 4*U[16] - 0 - U[8])
    m_funcion_x.append(lambda U,V: (U[17] / 2)*(0 - U[16]) + (V[17] / 2 )*(U[21] - U[9]) - 0 - U[16] + 4*U[17] - U[21] - U[9])
    m_funcion_x.append(lambda U,V: (U[18] / 2)*(U[19] - 1) + (V[18] / 2 )*(U[22] - U[11]) - U[19] - 1 + 4*U[18] - U[11] - U[11])
    m_funcion_x.append(lambda U,V: (U[19] / 2)*(U[20] - U[18]) + (V[19] / 2 )*(U[23] - U[12]) - U[20] - U[18] + 4*U[19] - U[23] - U[12])
    m_funcion_x.append(lambda U,V: (U[20] / 2)*(0 - U[19]) + (V[20] / 2 )*(U[24] - U[13]) - 0 - U[19] + 4*U[20] - U[24] - U[13])
    m_funcion_x.append(lambda U,V: (U[21] / 2)*(0 - 0) + (V[21] / 2 )*(U[25] - U[17]) - 0 - 0 + 4*U[21] - U[25] - U[17])
    m_funcion_x.append(lambda U,V: (U[22] / 2)*(U[23] - 1) + (V[22] / 2 )*(U[27] - U[18]) - U[23] - 1 + 4*U[22] - U[27] - U[18])
    m_funcion_x.append(lambda U,V: (U[23] / 2)*(U[24] - U[22]) + (V[23] / 2 )*(U[28] - U[19]) - U[24] - U[22] + 4*U[23] - U[28] - U[19])
    m_funcion_x.append(lambda U,V: (U[24] / 2)*(0 - U[23]) + (V[24] / 2 )*(U[29] - U[20]) - 0 - U[23] + 4*U[24] - U[29] - U[20])
    m_funcion_x.append(lambda U,V: (U[25] / 2)*(U[26] - 0) + (V[25] / 2 )*(U[30] - U[21]) - U[26] - 0 + 4*U[25] - U[30] - U[21])
    m_funcion_x.append(lambda U,V: (U[26] / 2)*(0 - U[25]) + (V[26] / 2 )*(U[31] - 0) - 0 - U[25] + 4*U[26] - U[31] - 0)
    m_funcion_x.append(lambda U,V: (U[27] / 2)*(U[28] - 1) + (V[27] / 2 )*(U[33] - U[22]) - U[28] - 1 + 4*U[27] - U[33] - U[22])
    m_funcion_x.append(lambda U,V: (U[28] / 2)*(U[29] - U[27]) + (V[28] / 2 )*(U[34] - U[23]) - U[29] - U[27] + 4*U[28] - U[34] - U[23])
    m_funcion_x.append(lambda U,V: (U[29] / 2)*(0 - U[28]) + (V[29] / 2 )*(U[35] - U[24]) - 0 - U[28] + 4*U[29] - U[35] - U[24])
    m_funcion_x.append(lambda U,V: (U[30] / 2)*(U[31] - 0) + (V[30] / 2 )*(U[36] - U[25]) - U[31] - 0 + 4*U[30] - U[36] - U[25])
    m_funcion_x.append(lambda U,V: (U[31] / 2)*(U[32] - U[30]) + (V[31] / 2 )*(U[37] - U[26]) - U[32] - U[30] + 4*U[31] - U[37] - U[26])
    m_funcion_x.append(lambda U,V: (U[32] / 2)*(0 - U[31]) + (V[32] / 2 )*(U[38] - 0) - 0 - U[31] + 4*U[32] - U[38] - 0)
    m_funcion_x.append(lambda U,V: (U[33] / 2)*(U[34] - 1) + (V[33] / 2 )*(0 - U[27]) - U[34] - 1 + 4*U[33] - 0 - U[27])
    m_funcion_x.append(lambda U,V: (U[34] / 2)*(U[35] - U[33]) + (V[34] / 2 )*(0 - U[28]) - U[35] - U[33] + 4*U[34] - 0 - U[28])
    m_funcion_x.append(lambda U,V: (U[35] / 2)*(0 - U[34]) + (V[35] / 2 )*(0 - U[29]) - 0 - U[34] + 4*U[35] - 0 - U[29])
    m_funcion_x.append(lambda U,V: (U[36] / 2)*(U[37] - 0) + (V[36] / 2 )*(0 - U[30]) - U[37] - 0 + 4*U[36] - 0 - U[30])
    m_funcion_x.append(lambda U,V: (U[37] / 2)*(U[38] - U[36]) + (V[37] / 2 )*(0 - U[31]) - U[38] - U[36] + 4*U[37] - 0 - U[31])
    m_funcion_x.append(lambda U,V: (U[38] / 2)*(0 - U[37]) + (V[38] / 2 )*(0 - U[32]) - 0 - U[37] + 4*U[38] - 0 - U[32])

    for item in range(39):
        list_of_zeros = list(0 for i in range(39))
        m_funcion_jacobiana_x.append(list_of_zeros)
    
    # Primera derivada parcia
    m_funcion_jacobiana_x[0][0] = (lambda U,V: 3.5)
    m_funcion_jacobiana_x[0][6] = (lambda U,V: (V[0]/2) - 1)

    m_funcion_jacobiana_x[1][1] = (lambda U,V: (U[2] / 2) + 4 )
    m_funcion_jacobiana_x[1][2] = (lambda U,V: (U[1] / 2) - 1 )
    m_funcion_jacobiana_x[1][7] = (lambda U,V: (V[1] / 2) - 1 )

    m_funcion_jacobiana_x[2][2] = (lambda U,V: (1/2)*(U[3] - U[1]) + 4 )
    m_funcion_jacobiana_x[2][3] = (lambda U,V: (U[2] / 2) - 1 )
    m_funcion_jacobiana_x[2][1] = (lambda U,V: -1*(U[2] / 2) - 1 )
    m_funcion_jacobiana_x[2][8] = (lambda U,V: (V[2] / 2) - 1 )

    m_funcion_jacobiana_x[3][3] = (lambda U,V: (1/2)*(U[4] - U[2]) + 4 )
    m_funcion_jacobiana_x[3][4] = (lambda U,V: (U[3] / 2) - 1 )
    m_funcion_jacobiana_x[3][2] = (lambda U,V: -1*(U[3] / 2) - 1 )
    m_funcion_jacobiana_x[3][9] = (lambda U,V: (V[3] / 2) - 1 )

    m_funcion_jacobiana_x[4][4] = (lambda U,V: (1/2)*(U[5] - U[3]) + 4 )
    m_funcion_jacobiana_x[4][5] = (lambda U,V: (U[4] / 2) - 1 )
    m_funcion_jacobiana_x[4][3] = (lambda U,V: -1*(U[4] / 2) - 1 )
    m_funcion_jacobiana_x[4][10] = (lambda U,V: (V[4] / 2) - 1 )

    m_funcion_jacobiana_x[5][5] = (lambda U,V: -1*(U[4] / 2) + 4 )
    m_funcion_jacobiana_x[5][4] = (lambda U,V: (U[5] / 2) - 1 )

    m_funcion_jacobiana_x[6][6] = (lambda U,V: 3.5 )
    m_funcion_jacobiana_x[6][7] = (lambda U,V: (V[6] / 2) - 1 )
    m_funcion_jacobiana_x[6][0] = (lambda U,V: -1*(V[6] / 2) - 1 )

    m_funcion_jacobiana_x[7][4] = (lambda U,V: (1/2)*(U[5] - U[3]) + 4 )
    m_funcion_jacobiana_x[7][5] = (lambda U,V: (U[4] / 2) - 1 )
    m_funcion_jacobiana_x[7][3] = (lambda U,V: -1*(U[4] / 2) - 1 )
    m_funcion_jacobiana_x[7][10] = (lambda U,V: (V[4] / 2) - 1 )
   
    

    x0 = np.ones(39)
    y0 = np.ones(39)
    print(poblar_funciones(m_funcion_x, x0, y0))
    