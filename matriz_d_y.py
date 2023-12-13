
m_funcion_y = list()
m_funcion_jacobiana_y = list()

for item in range(39):
        list_of_zeros = list(0 for i in range(39))
        m_funcion_jacobiana_y.append(list_of_zeros)
m_funcion_y.append(lambda U,V: (V[0] / 2)*(0 - 0) + (U[0] / 2)*(U[6] - 0) - 0 - 0 + 4*V[0] - V[6] - 0)
m_funcion_y.append(lambda U,V: (V[1] / 2)*(V[2] - 0) + (U[1] / 2 )*(V[7] - 0) - V[2] - 0 + 4*V[1] - V[7] - 0)
m_funcion_y.append(lambda U,V: (V[2] / 2)*(V[3] - V[1]) + (U[2] / 2 )*(V[8] - 0) - V[3] - V[1] + 4*V[2] - V[8] - 0)
m_funcion_y.append(lambda U,V: (V[3] / 2)*(V[4] - V[2]) + (U[3] / 2 )*(V[9] - 0) - V[4] - V[2] + 4*V[3] - V[9] - 0)
m_funcion_y.append(lambda U,V: (V[4] / 2)*(V[5] - V[3]) + (U[4] / 2 )*(V[10] - 0) - V[5] - V[3] + 4*V[4] - V[10] - 0)
#DUDA #V9,1/2(0-V8,1)+U9,1/2(0-0)-V8,1+4V9,1=0
m_funcion_y.append(lambda U,V: (V[5] / 2)*(0 - V[4]) + (U[5] / 2 )*(0 - 0) - V[4] + 4*V[5])
m_funcion_y.append(lambda U,V: (V[6] / 2)*(0 - 0) + (U[6] / 2 )*(V[11] - V[0]) - 0 - 1 + 4*V[6] - V[11] - V[0])
m_funcion_y.append(lambda U,V: (V[7] / 2)*(V[8] - 0) + (U[7] / 2 )*(V[15] - V[1]) - V[8] - 0 + 4*V[7] - V[15] - V[1])
m_funcion_y.append(lambda U,V: (V[8] / 2)*(V[9] - V[7]) + (U[8] / 2 )*(V[16] - V[2]) - V[9] - V[7] + 4*V[8] - V[16] - V[2])
m_funcion_y.append(lambda U,V: (V[9] / 2)*(V[10] - V[8]) + (U[9] / 2 )*(V[17] - V[3]) - V[10] - V[8] + 4*V[9] - V[17] - V[3])
m_funcion_y.append(lambda U,V: (V[10] / 2)*(0 - V[9]) + (U[10] / 2 )*(0 - V[4]) - 0 - V[9] + 4*V[10] - 0 - V[4])   
m_funcion_y.append(lambda U,V: (V[11] / 2)*(V[12] - 0) + (U[11] / 2 )*(V[18] - V[6]) - V[12] - 1 + 4*V[11] - V[18] - V[6])
m_funcion_y.append(lambda U,V: (V[12] / 2)*(V[13] - V[11]) + (U[12] / 2 )*(V[19] - 0) - V[13] - V[11] + 4*V[12] - V[19] - 0)
m_funcion_y.append(lambda U,V: (V[13] / 2)*(V[14] - V[12]) + (U[13] / 2 )*(V[20] - 0) - V[14] - V[12] + 4*V[13] - V[20] - 0)
m_funcion_y.append(lambda U,V: (V[14] / 2)*(V[15] - V[13]) + (U[14] / 2 )*(0 - 0) - V[15] - V[13] + 4*V[14] - 0 - 0)
m_funcion_y.append(lambda U,V: (V[15] / 2)*(V[16] - V[14]) + (U[15] / 2 )*(0 - V[7]) - V[16] - V[14] + 4*V[15] - 0 - V[7])
m_funcion_y.append(lambda U,V: (V[16] / 2)*(V[17] - V[15]) + (U[16] / 2 )*(0 - V[8]) - V[17] - V[15] + 4*V[16] - 0 - V[8])
m_funcion_y.append(lambda U,V: (V[17] / 2)*(0 - V[16]) + (U[17] / 2 )*(U[21] - V[9]) - 0 - V[16] + 4*V[17] - V[21] - V[9])
m_funcion_y.append(lambda U,V: (V[18] / 2)*(V[19] - 0) + (U[18] / 2 )*(U[22] - V[11]) - V[19] - 0 + 4*V[18] - V[22] - V[11])
m_funcion_y.append(lambda U,V: (V[19] / 2)*(V[20] - V[18]) + (U[19] / 2 )*(V[23] - V[12]) - V[20] - V[18] + 4*V[19] - V[23] - V[12])
m_funcion_y.append(lambda U,V: (V[20] / 2)*(0 - V[19]) + (U[20] / 2 )*(V[24] - V[13]) - 0 - V[19] + 4*V[20] - V[24] - V[13])
m_funcion_y.append(lambda U,V: (V[21] / 2)*(0 - 0) + (U[21] / 2 )*(V[25] - V[17]) - 0 - 0 + 4*V[21] - V[25] - V[17])
m_funcion_y.append(lambda U,V: (V[22] / 2)*(V[23] - 0) + (U[22] / 2 )*(V[27] - V[18]) - V[23] - 0 + 4*V[22] - V[27] - V[18])
m_funcion_y.append(lambda U,V: (V[23] / 2)*(V[24] - V[22]) + (U[23] / 2 )*(V[28] - V[19]) - V[24] - V[22] + 4*V[23] - V[28] - V[19])
m_funcion_y.append(lambda U,V: (V[24] / 2)*(0 - V[23]) + (U[24] / 2 )*(V[29] - V[20]) - 0 - V[23] + 4*V[24] - V[29] - V[20])
m_funcion_y.append(lambda U,V: (V[25] / 2)*(V[26] - 0) + (U[25] / 2 )*(V[30] - V[21]) - V[26] - 0 + 4*V[25] - V[30] - V[21])
m_funcion_y.append(lambda U,V: (V[26] / 2)*(0 - V[25]) + (U[26] / 2 )*(V[31] - 0) - 0 - V[25] + 4*V[26] - V[31] - 0)
m_funcion_y.append(lambda U,V: (V[27] / 2)*(V[28] - 0) + (U[27] / 2 )*(V[33] - V[22]) - V[28] - 0 + 4*V[27] - V[33] - V[22])
m_funcion_y.append(lambda U,V: (V[28] / 2)*(V[29] - V[27]) + (U[28] / 2 )*(V[34] - V[23]) - V[29] - V[27] + 4*V[28] - V[34] - U[23])
m_funcion_y.append(lambda U,V: (V[29] / 2)*(0 - V[28]) + (U[29] / 2 )*(V[35] - V[24]) - 0 - V[28] + 4*V[29] - V[35] - V[24])
m_funcion_y.append(lambda U,V: (V[30] / 2)*(V[31] - 0) + (U[30] / 2 )*(V[36] - V[25]) - V[31] - 0 + 4*V[30] - V[36] - V[25])
m_funcion_y.append(lambda U,V: (V[31] / 2)*(V[32] - V[30]) + (U[31] / 2 )*(V[37] - V[26]) - V[32] - V[30] + 4*V[31] - V[37] - V[26])
m_funcion_y.append(lambda U,V: (V[32] / 2)*(0 - V[31]) + (U[32] / 2 )*(U[38] - 0) - 0 - U[31] + 4*U[32] - U[38] - 0)
m_funcion_y.append(lambda U,V: (V[33] / 2)*(V[34] - 0) + (U[33] / 2 )*(0 - U[27]) - U[34] - 0 + 4*U[33] - 0 - U[27])
m_funcion_y.append(lambda U,V: (V[34] / 2)*(V[35] - V[33]) + (U[34] / 2 )*(0 - V[28]) - V[35] - V[33] + 4*V[34] - 0 - V[28])
m_funcion_y.append(lambda U,V: (V[35] / 2)*(0 - V[34]) + (U[35] / 2 )*(0 - V[29]) - 0 - V[34] + 4*V[35] - 0 - V[29])
m_funcion_y.append(lambda U,V: (V[36] / 2)*(V[37] - 0) + (U[36] / 2 )*(0 - V[30]) - V[37] - 0 + 4*V[36] - 0 - V[30])
m_funcion_y.append(lambda U,V: (V[37] / 2)*(V[38] - V[36]) + (U[37] / 2 )*(0 - V[31]) - V[38] - V[36] + 4*V[37] - 0 - V[31])
m_funcion_y.append(lambda U,V: (V[38] / 2)*(0 - V[37]) + (U[38] / 2 )*(0 - V[32]) - 0 - V[37] + 4*V[38] - 0 - V[32])


m_funcion_jacobiana_y[0][0] = lambda U,V: 4
m_funcion_jacobiana_y[0][6] = lambda U,V: (U[0]/2) - 1

m_funcion_jacobiana_y[1][1] = lambda U,V: (V[2] / 2) + 4 
m_funcion_jacobiana_y[1][2] = lambda U,V: (U[1] / 2) - 1 
m_funcion_jacobiana_y[1][7] = lambda U,V: (V[1] / 2) - 1 

m_funcion_jacobiana_y[2][2] = (lambda U,V: (V[3] - V[1]) / 2 + 4 )
m_funcion_jacobiana_y[2][3] = (lambda U,V: (V[2] / 2) - 1 )
m_funcion_jacobiana_y[2][1] = (lambda U,V: -1*(V[2] / 2) - 1 )
m_funcion_jacobiana_y[2][8] = (lambda U,V: (U[2] / 2) - 1 )

m_funcion_jacobiana_y[3][3] = (lambda U,V: (V[4] - V[2]) / 2 + 4 )
m_funcion_jacobiana_y[3][4] = (lambda U,V: (V[3] / 2) - 1 )
m_funcion_jacobiana_y[3][2] = (lambda U,V: -1*(V[3] / 2) - 1 )
m_funcion_jacobiana_y[3][9] = (lambda U,V: (U[3] / 2) - 1 )

m_funcion_jacobiana_y[4][4] = (lambda U,V: (V[5] - V[3]) / 2 + 4 )
m_funcion_jacobiana_y[4][5] = (lambda U,V: (V[4] / 2) - 1 )
m_funcion_jacobiana_y[4][3] = (lambda U,V: -(V[4] / 2) - 1 )
m_funcion_jacobiana_y[4][10] = (lambda U,V: (U[4] / 2) - 1 )

m_funcion_jacobiana_y[5][5] = (lambda U,V: -1*(V[4] / 2) + 4 )
m_funcion_jacobiana_y[5][4] = (lambda U,V: (V[5] / 2) - 1 )

m_funcion_jacobiana_y[6][6] = (lambda U,V: 3.5 )
m_funcion_jacobiana_y[6][7] = (lambda U,V: (U[6] / 2) - 1 )
m_funcion_jacobiana_y[6][0] = (lambda U,V: -1*(U[6] / 2) - 1 )

m_funcion_jacobiana_y[7][7] = (lambda U,V: (V[8] / 2) + 4 )
m_funcion_jacobiana_y[7][8] = (lambda U,V: (V[7] / 2) - 1 )
m_funcion_jacobiana_y[7][15] = (lambda U,V: (U[7] / 2) - 1 )
m_funcion_jacobiana_y[7][1] = (lambda U,V: -1*(U[7] / 2) - 1 )

m_funcion_jacobiana_y[8][8] = (lambda U,V: (V[9] - V[7]) / 2 + 4 )
m_funcion_jacobiana_y[8][9] = (lambda U,V: (V[8] / 2) - 1 )
m_funcion_jacobiana_y[8][7] = (lambda U,V: -1*(V[8] / 2) - 1 )
m_funcion_jacobiana_y[8][16] = (lambda U,V: (U[8] / 2) - 1 )
m_funcion_jacobiana_y[8][2] = (lambda U,V: -1*(U[8] / 2) - 1 )
    
m_funcion_jacobiana_y[9][9] = (lambda U,V: (V[10] - V[8]) / 2 + 4 )
m_funcion_jacobiana_y[9][9] = (lambda U,V: (V[9] / 2) - 1 )
m_funcion_jacobiana_y[9][7] = (lambda U,V: -1*(V[9] / 2) - 1 )
m_funcion_jacobiana_y[9][17] = (lambda U,V: (U[9] / 2) - 1 )
m_funcion_jacobiana_y[9][3] = (lambda U,V: -1*(U[9] / 2) - 1 )

m_funcion_jacobiana_y[10][10] = (lambda U,V: -1*(V[9]) + 4 )
m_funcion_jacobiana_y[10][9] = (lambda U,V: -1*(V[10] / 2) - 1 )
m_funcion_jacobiana_y[10][4] = (lambda U,V: -1*(U[10] / 2) - 1 )

m_funcion_jacobiana_y[11][11] = (lambda U,V: (V[12] / 2) + 3.5 )
m_funcion_jacobiana_y[11][12] = (lambda U,V: (V[11] / 2) - 1 )
m_funcion_jacobiana_y[11][18] = (lambda U,V: -1*(U[11] / 2) - 1 )
m_funcion_jacobiana_y[11][6] = (lambda U,V: -1*(U[11] / 2) - 1 )

m_funcion_jacobiana_y[12][12] = (lambda U,V: (V[13] - V[11]) / 2 + 4 )
m_funcion_jacobiana_y[12][13] = (lambda U,V: (V[12] / 2) - 1 )
m_funcion_jacobiana_y[12][11] = (lambda U,V: -1*(V[12] / 2) - 1 )
m_funcion_jacobiana_y[12][19] = (lambda U,V: (U[11] / 2) - 1 )

m_funcion_jacobiana_y[13][13] = (lambda U,V: (V[14] - V[12]) / 2 + 4 )
m_funcion_jacobiana_y[13][14] = (lambda U,V: (V[13] / 2) - 1 )
m_funcion_jacobiana_y[13][12] = (lambda U,V: -1*(V[13] / 2) - 1 )
m_funcion_jacobiana_y[13][20] = (lambda U,V: (U[13] / 2) - 1 )

m_funcion_jacobiana_y[14][14] = (lambda U,V: (V[15] - V[13]) / 2 + 4 )
m_funcion_jacobiana_y[14][15] = (lambda U,V: (V[14] / 2) - 1 )
m_funcion_jacobiana_y[14][13] = (lambda U,V: -1*(V[14] / 2) - 1 )

m_funcion_jacobiana_y[15][15] = (lambda U,V: (V[16] - V[14]) / 2 + 4 )
m_funcion_jacobiana_y[15][16] = (lambda U,V: (V[15] / 2) - 1 )
m_funcion_jacobiana_y[15][14] = (lambda U,V: -1*(V[15] / 2) - 1 )
m_funcion_jacobiana_y[15][7] = (lambda U,V: -1*(U[15] / 2) - 1 )

m_funcion_jacobiana_y[16][16] = (lambda U,V: (V[17] - V[15]) / 2 + 4 )
m_funcion_jacobiana_y[16][17] = (lambda U,V: (V[15] / 2) - 1 )
m_funcion_jacobiana_y[16][15] = (lambda U,V: -1*(V[15] / 2) - 1 )
m_funcion_jacobiana_y[16][8] = (lambda U,V: -1*(U[15] / 2) - 1 )

m_funcion_jacobiana_y[17][17] = (lambda U,V: -1*(V[16] / 2) + 4 )
m_funcion_jacobiana_y[17][16] = (lambda U,V: -1*(V[17] / 2) - 1 )
m_funcion_jacobiana_y[17][21] = (lambda U,V: (U[17] / 2) - 1 )
m_funcion_jacobiana_y[17][9] = (lambda U,V: -1*(U[17] / 2) - 1 )

m_funcion_jacobiana_y[18][18] = (lambda U,V: (V[19] / 2) + 3.5 )
m_funcion_jacobiana_y[18][19] = (lambda U,V: (V[18] / 2) - 1 )
m_funcion_jacobiana_y[18][22] = (lambda U,V: (U[18] / 2) - 1 )
m_funcion_jacobiana_y[18][11] = (lambda U,V: -1*(U[18] / 2) - 1 )
    
m_funcion_jacobiana_y[19][19] = (lambda U,V: (V[20] - V[18]) / 2 + 4 )
m_funcion_jacobiana_y[19][20] = (lambda U,V: (V[19] / 2) - 1 )
m_funcion_jacobiana_y[19][18] = (lambda U,V: -1*(V[19] / 2) - 1 )
m_funcion_jacobiana_y[19][23] = (lambda U,V: (U[19] / 2) - 1 )
m_funcion_jacobiana_y[19][12] = (lambda U,V: -1*(U[19] / 2) - 1 )

m_funcion_jacobiana_y[20][20] = (lambda U,V: -1*(V[19] / 2) + 4 )
m_funcion_jacobiana_y[20][19] = (lambda U,V: -1*(V[20] / 2) - 1 )
m_funcion_jacobiana_y[20][24] = (lambda U,V: (U[20] / 2) - 1 )
m_funcion_jacobiana_y[20][13] = (lambda U,V: -1*(U[20] / 2) - 1 )

m_funcion_jacobiana_y[21][21] = (lambda U,V:  4 )
m_funcion_jacobiana_y[21][25] = (lambda U,V: (U[21] / 2) - 1 )
m_funcion_jacobiana_y[21][17] = (lambda U,V: -1*(U[21] / 2) - 1 )

m_funcion_jacobiana_y[22][22] = (lambda U,V: (V[23] / 2) + 3.5 )
m_funcion_jacobiana_y[22][23] = (lambda U,V: (V[22] / 2) - 1 )
m_funcion_jacobiana_y[22][27] = (lambda U,V: (U[22] / 2) - 1 )
m_funcion_jacobiana_y[22][18] = (lambda U,V: -1*(U[22] / 2) - 1 )
    
m_funcion_jacobiana_y[23][23] = (lambda U,V: (V[24] - V[22]) / 2 + 4 )
m_funcion_jacobiana_y[23][24] = (lambda U,V: (V[23] / 2) - 1 )
m_funcion_jacobiana_y[23][22] = (lambda U,V: -1*(V[23] / 2) - 1 )
m_funcion_jacobiana_y[23][28] = (lambda U,V: (U[23] / 2) - 1 )
m_funcion_jacobiana_y[23][19] = (lambda U,V: -1*(U[23] / 2) - 1 )

m_funcion_jacobiana_y[24][24] = (lambda U,V: -1*(V[23] / 2) + 4 )
m_funcion_jacobiana_y[24][23] = (lambda U,V: -1*(V[14] / 2) - 1 )
m_funcion_jacobiana_y[24][29] = (lambda U,V: (U[24] / 2) - 1 )
m_funcion_jacobiana_y[24][20] = (lambda U,V: -1*(U[24] / 2) - 1 )

m_funcion_jacobiana_y[25][25] = (lambda U,V: (V[26] / 2) + 4 )
m_funcion_jacobiana_y[25][26] = (lambda U,V: (V[25] / 2) - 1 )
m_funcion_jacobiana_y[25][30] = (lambda U,V: (U[25] / 2) - 1 )
m_funcion_jacobiana_y[25][21] = (lambda U,V: -1*(U[25] / 2) - 1 )

m_funcion_jacobiana_y[26][26] = (lambda U,V: -1*(V[25] / 2) + 4 )
m_funcion_jacobiana_y[26][25] = (lambda U,V: -1*(V[26] / 2) - 1 )
m_funcion_jacobiana_y[26][31] = (lambda U,V: (U[26] / 2) - 1 )

m_funcion_jacobiana_y[27][27] = (lambda U,V: (V[28] / 2) + 3.5 )
m_funcion_jacobiana_y[27][28] = (lambda U,V: (V[27] / 2) - 1 )
m_funcion_jacobiana_y[27][33] = (lambda U,V: (U[27] / 2) - 1 )
m_funcion_jacobiana_y[27][22] = (lambda U,V: -1*(U[27] / 2) - 1 )
    #Quede aqui P28
    
m_funcion_jacobiana_y[28][28] = (lambda U,V: (V[29] - V[27]) / 2 + 4 )
m_funcion_jacobiana_y[28][29] = (lambda U,V: (V[28] / 2) - 1 )
m_funcion_jacobiana_y[28][27] = (lambda U,V: -1*(V[28] / 2) - 1 )
m_funcion_jacobiana_y[28][34] = (lambda U,V: (U[28] / 2) - 1 )
m_funcion_jacobiana_y[28][23] = (lambda U,V: -1*(U[28] / 2) - 1 )

m_funcion_jacobiana_y[29][29] = (lambda U,V: -1*(V[28] /2) + 4 )
m_funcion_jacobiana_y[29][28] = (lambda U,V: -1*(V[29] / 2) - 1 )
m_funcion_jacobiana_y[29][34] = (lambda U,V: (U[29] / 2) - 1 )
m_funcion_jacobiana_y[29][24] = (lambda U,V: -1*(U[29] / 2) - 1 )

m_funcion_jacobiana_y[30][30] = (lambda U,V: (V[31] / 2) + 4 )
m_funcion_jacobiana_y[30][31] = (lambda U,V: (V[30] / 2) - 1 )
m_funcion_jacobiana_y[30][36] = (lambda U,V: (U[30] / 2) - 1 )
m_funcion_jacobiana_y[30][25] = (lambda U,V: -1*(U[30] / 2) - 1 )

m_funcion_jacobiana_y[31][31] = (lambda U,V: (V[32] - V[30]) / 2 + 4 )
m_funcion_jacobiana_y[31][32] = (lambda U,V: (V[31] / 2) - 1 )
m_funcion_jacobiana_y[31][30] = (lambda U,V: -1*(V[31] / 2) - 1 )
m_funcion_jacobiana_y[31][37] = (lambda U,V: (U[31] / 2) - 1 )
m_funcion_jacobiana_y[31][26] = (lambda U,V: -1*(U[31] / 2) - 1 )

m_funcion_jacobiana_y[32][32] = (lambda U,V: -1*(V[31] / 2) + 4 )
m_funcion_jacobiana_y[32][31] = (lambda U,V: -1*(V[32] / 2) - 1 )
m_funcion_jacobiana_y[32][38] = (lambda U,V: (U[32] / 2) - 1 )

m_funcion_jacobiana_y[33][33] = (lambda U,V: (V[34] / 2) + 3.5 )
m_funcion_jacobiana_y[33][34] = (lambda U,V: (V[33] / 2) - 1 )
m_funcion_jacobiana_y[33][27] = (lambda U,V: -1*(U[33] / 2) - 1 )

m_funcion_jacobiana_y[34][34] = (lambda U,V: (V[35] - V[33]) / 2 + 4 )
m_funcion_jacobiana_y[34][35] = (lambda U,V: (V[34] / 2) - 1 )
m_funcion_jacobiana_y[34][33] = (lambda U,V: -1*(V[34] / 2) - 1 )
m_funcion_jacobiana_y[34][28] = (lambda U,V: -1*(U[34] / 2) - 1 )

m_funcion_jacobiana_y[35][35] = (lambda U,V: -1*(V[34] / 2) + 4 )
m_funcion_jacobiana_y[35][34] = (lambda U,V: -1*(V[35] / 2) - 1 )
m_funcion_jacobiana_y[35][29] = (lambda U,V: -1*(U[35] / 2) - 1 )

m_funcion_jacobiana_y[36][36] = (lambda U,V: (V[37] / 2) + 4 )
m_funcion_jacobiana_y[36][37] = (lambda U,V: (V[36] / 2) - 1 )
m_funcion_jacobiana_y[36][30] = (lambda U,V: -1*(U[36] / 2) - 1 )

m_funcion_jacobiana_y[37][37] = (lambda U,V: (V[38] - U[36]) / 2 + 4 )
m_funcion_jacobiana_y[37][38] = (lambda U,V: (V[37] / 2) - 1 )
m_funcion_jacobiana_y[37][36] = (lambda U,V: -1*(V[37] / 2) - 1 )
m_funcion_jacobiana_y[37][31] = (lambda U,V: -1*(U[37] / 2) - 1 )

m_funcion_jacobiana_y[38][38] = (lambda U,V: -1*(V[37] / 2) + 4 )
m_funcion_jacobiana_y[38][37] = (lambda U,V: -1*(V[38] / 2) - 1 )
m_funcion_jacobiana_y[38][32] = (lambda U,V: -1*(U[38] / 2) - 1 )

def m_y():
    return m_funcion_y

def m_j_y():
    return m_funcion_jacobiana_y
        