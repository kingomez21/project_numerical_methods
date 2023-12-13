
xi = [1,5,6,7,8,9,1,5,6,7,8,1,2,3,4,5,6,7,1,2,3,7,1,2,3,7,8,1,2,3,7,8,9,1,2,3,7,8,9]
xi_j1 = [1,5,6,7,8,9]
xi_j2 = [1,5,6,7,8]

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