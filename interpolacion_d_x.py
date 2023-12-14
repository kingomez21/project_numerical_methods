
xi = [1,5,6,7,8,9,1,5,6,7,8,1,2,3,4,5,6,7,1,2,3,7,1,2,3,7,8,1,2,3,7,8,9,1,2,3,7,8,9]
xi_j1 = [1,5,6,7,8,9]
xi_j2 = [1,5,6,7,8]
xi_j3 = [1,2,3,4,5,6,7]
xi_j4 = [1,2,3,7]
xi_j5 = [1,2,3,7,8]
xi_j6 = [1,2,3,7,8,9]
xi_j7 = [1,2,3,7,8,9]


funcion_ui_x = list()

# para i = 0
funcion_ui_x.append(lambda x: 
                    ( (x - xi_j1[1]) / (xi_j1[0] - xi_j1[1]) )*
                    ( (x - xi_j1[2]) / (xi_j1[0] - xi_j1[2]) )*
                    ( (x - xi_j1[3]) / (xi_j1[0] - xi_j1[3]))*
                    ( (x - xi_j1[4]) / (xi_j1[0] - xi_j1[4]) )*
                    ( (x - xi_j1[5]) / (xi_j1[0] - xi_j1[5]) )  )

#para i = 1
funcion_ui_x.append(lambda x: 
                    ( (x - xi_j1[0]) / (xi_j1[1] - xi_j1[0]) )*
                    ( (x - xi_j1[2]) / (xi_j1[1] - xi_j1[2]) )*
                    ( (x - xi_j1[3]) / (xi_j1[1] - xi_j1[3]))*
                    ( (x - xi_j1[4]) / (xi_j1[1] - xi_j1[4]) )*
                    ( (x - xi_j1[5]) / (xi_j1[1] - xi_j1[5]) )  )

#para i = 2
funcion_ui_x.append(lambda x: 
                    ( (x - xi_j1[0]) / (xi_j1[2] - xi_j1[0]) )*
                    ( (x - xi_j1[1]) / (xi_j1[2] - xi_j1[1]) )*
                    ( (x - xi_j1[3]) / (xi_j1[2] - xi_j1[3]))*
                    ( (x - xi_j1[4]) / (xi_j1[2] - xi_j1[4]) )*
                    ( (x - xi_j1[5]) / (xi_j1[2] - xi_j1[5]) )  )

#para i = 3
funcion_ui_x.append(lambda x: 
                    ( (x - xi_j1[0]) / (xi_j1[3] - xi_j1[0]) )*
                    ( (x - xi_j1[1]) / (xi_j1[3] - xi_j1[1]) )*
                    ( (x - xi_j1[2]) / (xi_j1[3] - xi_j1[2]))*
                    ( (x - xi_j1[4]) / (xi_j1[3] - xi_j1[4]) )*
                    ( (x - xi_j1[5]) / (xi_j1[3] - xi_j1[5]) )  )

#para i = 4
funcion_ui_x.append(lambda x: 
                    ( (x - xi_j1[0]) / (xi_j1[4] - xi_j1[0]) )*
                    ( (x - xi_j1[1]) / (xi_j1[4] - xi_j1[1]) )*
                    ( (x - xi_j1[2]) / (xi_j1[4] - xi_j1[2]))*
                    ( (x - xi_j1[3]) / (xi_j1[4] - xi_j1[3]) )*
                    ( (x - xi_j1[5]) / (xi_j1[4] - xi_j1[5]) )  )

#para i = 4
funcion_ui_x.append(lambda x: 
                    ( (x - xi_j1[0]) / (xi_j1[5] - xi_j1[0]) )*
                    ( (x - xi_j1[1]) / (xi_j1[5] - xi_j1[1]) )*
                    ( (x - xi_j1[2]) / (xi_j1[5] - xi_j1[2]))*
                    ( (x - xi_j1[3]) / (xi_j1[5] - xi_j1[3]) )*
                    ( (x - xi_j1[4]) / (xi_j1[5] - xi_j1[4]) )  )


# para J = 2

#para i = 0
funcion_ui_x.append(lambda x: 
                    ( (x - xi_j2[1]) / (xi_j2[0] - xi_j2[1]) )*
                    ( (x - xi_j2[2]) / (xi_j2[0] - xi_j2[2]) )*
                    ( (x - xi_j2[3]) / (xi_j2[0] - xi_j2[3]))*
                    ( (x - xi_j2[4]) / (xi_j2[0] - xi_j2[4]) )  )

#para i = 1
funcion_ui_x.append(lambda x: 
                    ( (x - xi_j2[0]) / (xi_j2[1] - xi_j2[0]) )*
                    ( (x - xi_j2[2]) / (xi_j2[1] - xi_j2[2]) )*
                    ( (x - xi_j2[3]) / (xi_j2[1] - xi_j2[3]) )*
                    ( (x - xi_j2[4]) / (xi_j2[1] - xi_j2[4]) )  )

#para i = 2
funcion_ui_x.append(lambda x: 
                    ( (x - xi_j2[0]) / (xi_j2[2] - xi_j2[0]) )*
                    ( (x - xi_j2[1]) / (xi_j2[2] - xi_j2[1]) )*
                    ( (x - xi_j2[3]) / (xi_j2[2] - xi_j2[3]) )*
                    ( (x - xi_j2[4]) / (xi_j2[2] - xi_j2[4]) )  )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j2[0]) / (xi_j2[3] - xi_j2[0]) )*
                    ( (x - xi_j2[1]) / (xi_j2[3] - xi_j2[1]) )*
                    ( (x - xi_j2[2]) / (xi_j2[3] - xi_j2[2]) )*
                    ( (x - xi_j2[4]) / (xi_j2[3] - xi_j2[4]) )  )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j2[0]) / (xi_j2[4] - xi_j2[0]) )*
                    ( (x - xi_j2[1]) / (xi_j2[4] - xi_j2[1]) )*
                    ( (x - xi_j2[2]) / (xi_j2[4] - xi_j2[2]) )*
                    ( (x - xi_j2[3]) / (xi_j2[4] - xi_j2[3]) )  )

#Para j = 3

#para i = 0

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j3[1]) / (xi_j3[0] - xi_j3[1]) )*
                    ( (x - xi_j3[2]) / (xi_j3[0] - xi_j3[2]) )*
                    ( (x - xi_j3[3]) / (xi_j3[0] - xi_j3[3]) )*
                    ( (x - xi_j3[4]) / (xi_j3[0] - xi_j3[4]) )*
                    ( (x - xi_j3[5]) / (xi_j3[0] - xi_j3[5]) )*
                    ( (x - xi_j3[6]) / (xi_j3[0] - xi_j3[6]) )  )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j3[0]) / (xi_j3[1] - xi_j3[0]) )*
                    ( (x - xi_j3[2]) / (xi_j3[1] - xi_j3[2]) )*
                    ( (x - xi_j3[3]) / (xi_j3[1] - xi_j3[3]) )*
                    ( (x - xi_j3[4]) / (xi_j3[1] - xi_j3[4]) )*
                    ( (x - xi_j3[5]) / (xi_j3[1] - xi_j3[5]) )*
                    ( (x - xi_j3[6]) / (xi_j3[1] - xi_j3[6]) )  )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j3[0]) / (xi_j3[2] - xi_j3[0]) )*
                    ( (x - xi_j3[1]) / (xi_j3[2] - xi_j3[1]) )*
                    ( (x - xi_j3[3]) / (xi_j3[2] - xi_j3[3]) )*
                    ( (x - xi_j3[4]) / (xi_j3[2] - xi_j3[4]) )*
                    ( (x - xi_j3[5]) / (xi_j3[2] - xi_j3[5]) )*
                    ( (x - xi_j3[6]) / (xi_j3[2] - xi_j3[6]) )  )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j3[0]) / (xi_j3[3] - xi_j3[0]) )*
                    ( (x - xi_j3[1]) / (xi_j3[3] - xi_j3[1]) )*
                    ( (x - xi_j3[2]) / (xi_j3[3] - xi_j3[2]) )*
                    ( (x - xi_j3[4]) / (xi_j3[3] - xi_j3[4]) )*
                    ( (x - xi_j3[5]) / (xi_j3[3] - xi_j3[5]) )*
                    ( (x - xi_j3[6]) / (xi_j3[3] - xi_j3[6]) )  )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j3[0]) / (xi_j3[4] - xi_j3[0]) )*
                    ( (x - xi_j3[1]) / (xi_j3[4] - xi_j3[1]) )*
                    ( (x - xi_j3[2]) / (xi_j3[4] - xi_j3[2]) )*
                    ( (x - xi_j3[3]) / (xi_j3[4] - xi_j3[3]) )*
                    ( (x - xi_j3[5]) / (xi_j3[4] - xi_j3[5]) )*
                    ( (x - xi_j3[6]) / (xi_j3[4] - xi_j3[6]) )  )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j3[0]) / (xi_j3[5] - xi_j3[0]) )*
                    ( (x - xi_j3[1]) / (xi_j3[5] - xi_j3[1]) )*
                    ( (x - xi_j3[2]) / (xi_j3[5] - xi_j3[2]) )*
                    ( (x - xi_j3[3]) / (xi_j3[5] - xi_j3[3]) )*
                    ( (x - xi_j3[4]) / (xi_j3[5] - xi_j3[4]) )*
                    ( (x - xi_j3[6]) / (xi_j3[5] - xi_j3[6]) )  )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j3[0]) / (xi_j3[6] - xi_j3[0]) )*
                    ( (x - xi_j3[1]) / (xi_j3[6] - xi_j3[1]) )*
                    ( (x - xi_j3[2]) / (xi_j3[6] - xi_j3[2]) )*
                    ( (x - xi_j3[3]) / (xi_j3[6] - xi_j3[3]) )*
                    ( (x - xi_j3[4]) / (xi_j3[6] - xi_j3[4]) )*
                    ( (x - xi_j3[5]) / (xi_j3[6] - xi_j3[5]) )  )

#Para J=4
#Para i = 0

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j4[1]) / (xi_j4[0] - xi_j4[1]) )*
                    ( (x - xi_j4[2]) / (xi_j4[0] - xi_j4[2]) )*
                    ( (x - xi_j4[3]) / (xi_j4[0] - xi_j4[3]) ) )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j4[0]) / (xi_j4[1] - xi_j4[0]) )*
                    ( (x - xi_j4[2]) / (xi_j4[1] - xi_j4[2]) )*
                    ( (x - xi_j4[3]) / (xi_j4[1] - xi_j4[3]) ) )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j4[0]) / (xi_j4[2] - xi_j4[0]) )*
                    ( (x - xi_j4[1]) / (xi_j4[2] - xi_j4[1]) )*
                    ( (x - xi_j4[3]) / (xi_j4[2] - xi_j4[3]) ) )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j4[0]) / (xi_j4[3] - xi_j4[0]) )*
                    ( (x - xi_j4[1]) / (xi_j4[3] - xi_j4[1]) )*
                    ( (x - xi_j4[2]) / (xi_j4[3] - xi_j4[2]) ) )

#Para J= 5
#Para i=0

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j5[1]) / (xi_j5[0] - xi_j5[1]) )*
                    ( (x - xi_j5[2]) / (xi_j5[0] - xi_j5[2]) )*
                    ( (x - xi_j5[3]) / (xi_j5[0] - xi_j5[3]) )*
                    ( (x - xi_j5[4]) / (xi_j5[0] - xi_j5[4]) ) )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j5[0]) / (xi_j5[1] - xi_j5[0]) )*
                    ( (x - xi_j5[2]) / (xi_j5[1] - xi_j5[2]) )*
                    ( (x - xi_j5[3]) / (xi_j5[1] - xi_j5[3]) )*
                    ( (x - xi_j5[4]) / (xi_j5[1] - xi_j5[4]) ) )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j5[0]) / (xi_j5[2] - xi_j5[0]) )*
                    ( (x - xi_j5[1]) / (xi_j5[2] - xi_j5[1]) )*
                    ( (x - xi_j5[3]) / (xi_j5[2] - xi_j5[3]) )*
                    ( (x - xi_j5[4]) / (xi_j5[2] - xi_j5[4]) ) )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j5[0]) / (xi_j5[3] - xi_j5[0]) )*
                    ( (x - xi_j5[1]) / (xi_j5[3] - xi_j5[1]) )*
                    ( (x - xi_j5[2]) / (xi_j5[3] - xi_j5[2]) )*
                    ( (x - xi_j5[4]) / (xi_j5[3] - xi_j5[4]) ) )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j5[0]) / (xi_j5[4] - xi_j5[0]) )*
                    ( (x - xi_j5[1]) / (xi_j5[4] - xi_j5[1]) )*
                    ( (x - xi_j5[2]) / (xi_j5[4] - xi_j5[2]) )*
                    ( (x - xi_j5[3]) / (xi_j5[4] - xi_j5[3]) ) )

#Para j = 6
#Para i = 0

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j6[1]) / (xi_j6[0] - xi_j6[1]) )*
                    ( (x - xi_j6[2]) / (xi_j6[0] - xi_j6[2]) )*
                    ( (x - xi_j6[3]) / (xi_j6[0] - xi_j6[3]))*
                    ( (x - xi_j6[4]) / (xi_j6[0] - xi_j6[4]) )*
                    ( (x - xi_j6[5]) / (xi_j6[0] - xi_j6[5]) )  )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j6[0]) / (xi_j6[1] - xi_j6[0]) )*
                    ( (x - xi_j6[2]) / (xi_j6[1] - xi_j6[2]) )*
                    ( (x - xi_j6[3]) / (xi_j6[1] - xi_j6[3]))*
                    ( (x - xi_j6[4]) / (xi_j6[1] - xi_j6[4]) )*
                    ( (x - xi_j6[5]) / (xi_j6[1] - xi_j6[5]) )  )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j6[0]) / (xi_j6[2] - xi_j6[0]) )*
                    ( (x - xi_j6[1]) / (xi_j6[2] - xi_j6[1]) )*
                    ( (x - xi_j6[3]) / (xi_j6[2] - xi_j6[3]))*
                    ( (x - xi_j6[4]) / (xi_j6[2] - xi_j6[4]) )*
                    ( (x - xi_j6[5]) / (xi_j6[2] - xi_j6[5]) )  )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j6[0]) / (xi_j6[3] - xi_j6[0]) )*
                    ( (x - xi_j6[1]) / (xi_j6[3] - xi_j6[1]) )*
                    ( (x - xi_j6[2]) / (xi_j6[3] - xi_j6[2]))*
                    ( (x - xi_j6[4]) / (xi_j6[3] - xi_j6[4]) )*
                    ( (x - xi_j6[5]) / (xi_j6[3] - xi_j6[5]) )  )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j6[0]) / (xi_j6[4] - xi_j6[0]) )*
                    ( (x - xi_j6[1]) / (xi_j6[4] - xi_j6[1]) )*
                    ( (x - xi_j6[2]) / (xi_j6[4] - xi_j6[2]))*
                    ( (x - xi_j6[3]) / (xi_j6[4] - xi_j6[3]) )*
                    ( (x - xi_j6[5]) / (xi_j6[4] - xi_j6[5]) )  )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j6[0]) / (xi_j6[5] - xi_j6[0]) )*
                    ( (x - xi_j6[1]) / (xi_j6[5] - xi_j6[1]) )*
                    ( (x - xi_j6[2]) / (xi_j6[5] - xi_j6[2]))*
                    ( (x - xi_j6[3]) / (xi_j6[5] - xi_j6[3]) )*
                    ( (x - xi_j6[4]) / (xi_j6[5] - xi_j6[4]) )  )


#Para j = 7
#Para i = 0

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j7[1]) / (xi_j7[0] - xi_j7[1]) )*
                    ( (x - xi_j7[2]) / (xi_j7[0] - xi_j7[2]) )*
                    ( (x - xi_j7[3]) / (xi_j7[0] - xi_j7[3]))*
                    ( (x - xi_j7[4]) / (xi_j7[0] - xi_j7[4]) )*
                    ( (x - xi_j7[5]) / (xi_j7[0] - xi_j7[5]) )  )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j7[0]) / (xi_j7[1] - xi_j7[0]) )*
                    ( (x - xi_j7[2]) / (xi_j7[1] - xi_j7[2]) )*
                    ( (x - xi_j7[3]) / (xi_j7[1] - xi_j7[3]))*
                    ( (x - xi_j7[4]) / (xi_j7[1] - xi_j7[4]) )*
                    ( (x - xi_j7[5]) / (xi_j7[1] - xi_j7[5]) )  )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j7[0]) / (xi_j7[2] - xi_j7[0]) )*
                    ( (x - xi_j7[1]) / (xi_j7[2] - xi_j7[1]) )*
                    ( (x - xi_j7[3]) / (xi_j7[2] - xi_j7[3]))*
                    ( (x - xi_j7[4]) / (xi_j7[2] - xi_j7[4]) )*
                    ( (x - xi_j7[5]) / (xi_j7[2] - xi_j7[5]) )  )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j7[0]) / (xi_j7[3] - xi_j7[0]) )*
                    ( (x - xi_j7[1]) / (xi_j7[3] - xi_j7[1]) )*
                    ( (x - xi_j7[2]) / (xi_j7[3] - xi_j7[2]))*
                    ( (x - xi_j7[4]) / (xi_j7[3] - xi_j7[4]) )*
                    ( (x - xi_j7[5]) / (xi_j7[3] - xi_j7[5]) )  )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j7[0]) / (xi_j7[4] - xi_j7[0]) )*
                    ( (x - xi_j7[1]) / (xi_j7[4] - xi_j7[1]) )*
                    ( (x - xi_j7[2]) / (xi_j7[4] - xi_j7[2]))*
                    ( (x - xi_j7[3]) / (xi_j7[4] - xi_j7[3]) )*
                    ( (x - xi_j7[5]) / (xi_j7[4] - xi_j7[5]) )  )

funcion_ui_x.append(lambda x: 
                    ( (x - xi_j7[0]) / (xi_j7[5] - xi_j7[0]) )*
                    ( (x - xi_j7[1]) / (xi_j7[5] - xi_j7[1]) )*
                    ( (x - xi_j7[2]) / (xi_j7[5] - xi_j7[2]))*
                    ( (x - xi_j7[3]) / (xi_j7[5] - xi_j7[3]) )*
                    ( (x - xi_j7[4]) / (xi_j7[5] - xi_j7[4]) )  )