
yi = [1,2,3,4,5,6,7,3,4,5,6,7,3,4,5,6,7, 3,1,2,3, 1,2,3 , 1,2,3,4,5,6,7, 1,2,5,6,7, 1,6,7]

yi_x1 = [1,2,3,4,5,6,7]
yi_x2 = [3,4,5,6,7]
yi_x3 = [3,4,5,6,7]
yi_x4 = 3
yi_x5 = [1,2,3]
yi_x6 = [1,2,3]
yi_x7 = [1,2,3,4,5,6,7]
yi_x8 = [1,2,5,6,7]
yi_x9 = [1,6,7]

funcion_vi_y = list()

# Para X = 1
# Para i = 0

funcion_vi_y.append(lambda y: 
                    ( (y - yi_x1[1]) / (yi_x1[0] - yi_x1[1]) )*
                    ( (y - yi_x1[2]) / (yi_x1[0] - yi_x1[2]) )*
                    ( (y - yi_x1[3]) / (yi_x1[0] - yi_x1[3]) )*
                    ( (y - yi_x1[4]) / (yi_x1[0] - yi_x1[4]) )*
                    ( (y - yi_x1[5]) / (yi_x1[0] - yi_x1[5]) )*
                    ( (y - yi_x1[6]) / (yi_x1[0] - yi_x1[6]) ) )

# Para i = 1
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x1[0]) / (yi_x1[1] - yi_x1[0]) )*
                    ( (y - yi_x1[2]) / (yi_x1[1] - yi_x1[2]) )*
                    ( (y - yi_x1[3]) / (yi_x1[1] - yi_x1[3]) )*
                    ( (y - yi_x1[4]) / (yi_x1[1] - yi_x1[4]) )*
                    ( (y - yi_x1[5]) / (yi_x1[1] - yi_x1[5]) )*
                    ( (y - yi_x1[6]) / (yi_x1[1] - yi_x1[6]) ) )

# Para i = 2
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x1[0]) / (yi_x1[2] - yi_x1[0]) )*
                    ( (y - yi_x1[1]) / (yi_x1[2] - yi_x1[1]) )*
                    ( (y - yi_x1[3]) / (yi_x1[2] - yi_x1[3]) )*
                    ( (y - yi_x1[4]) / (yi_x1[2] - yi_x1[4]) )*
                    ( (y - yi_x1[5]) / (yi_x1[2] - yi_x1[5]) )*
                    ( (y - yi_x1[6]) / (yi_x1[2] - yi_x1[6]) ) )

# Para i = 3
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x1[0]) / (yi_x1[3] - yi_x1[0]) )*
                    ( (y - yi_x1[1]) / (yi_x1[3] - yi_x1[1]) )*
                    ( (y - yi_x1[2]) / (yi_x1[3] - yi_x1[2]) )*
                    ( (y - yi_x1[4]) / (yi_x1[3] - yi_x1[4]) )*
                    ( (y - yi_x1[5]) / (yi_x1[3] - yi_x1[5]) )*
                    ( (y - yi_x1[6]) / (yi_x1[3] - yi_x1[6]) ) )

# Para i = 4
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x1[0]) / (yi_x1[4] - yi_x1[0]) )*
                    ( (y - yi_x1[1]) / (yi_x1[4] - yi_x1[1]) )*
                    ( (y - yi_x1[2]) / (yi_x1[4] - yi_x1[2]) )*
                    ( (y - yi_x1[3]) / (yi_x1[4] - yi_x1[3]) )*
                    ( (y - yi_x1[5]) / (yi_x1[4] - yi_x1[5]) )*
                    ( (y - yi_x1[6]) / (yi_x1[4] - yi_x1[6]) ) )

# Para i = 5
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x1[0]) / (yi_x1[5] - yi_x1[0]) )*
                    ( (y - yi_x1[1]) / (yi_x1[5] - yi_x1[1]) )*
                    ( (y - yi_x1[2]) / (yi_x1[5] - yi_x1[2]) )*
                    ( (y - yi_x1[3]) / (yi_x1[5] - yi_x1[3]) )*
                    ( (y - yi_x1[4]) / (yi_x1[5] - yi_x1[4]) )*
                    ( (y - yi_x1[6]) / (yi_x1[5] - yi_x1[6]) ) )

# Para i = 6
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x1[0]) / (yi_x1[6] - yi_x1[0]) )*
                    ( (y - yi_x1[1]) / (yi_x1[6] - yi_x1[1]) )*
                    ( (y - yi_x1[2]) / (yi_x1[6] - yi_x1[2]) )*
                    ( (y - yi_x1[3]) / (yi_x1[6] - yi_x1[3]) )*
                    ( (y - yi_x1[4]) / (yi_x1[6] - yi_x1[4]) )*
                    ( (y - yi_x1[5]) / (yi_x1[6] - yi_x1[5]) ) )


# Para X = 2
# Para i = 0

funcion_vi_y.append(lambda y: 
                    ( (y - yi_x2[1]) / (yi_x2[0] - yi_x2[1]) )*
                    ( (y - yi_x2[2]) / (yi_x2[0] - yi_x2[2]) )*
                    ( (y - yi_x2[3]) / (yi_x2[0] - yi_x2[3]) )*
                    ( (y - yi_x2[4]) / (yi_x2[0] - yi_x2[4]) ) )

# Para i = 1
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x2[0]) / (yi_x2[1] - yi_x2[0]) )*
                    ( (y - yi_x2[2]) / (yi_x2[1] - yi_x2[2]) )*
                    ( (y - yi_x2[3]) / (yi_x2[1] - yi_x2[3]) )*
                    ( (y - yi_x2[4]) / (yi_x2[1] - yi_x2[4]) ) )

# Para i = 2
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x2[0]) / (yi_x2[2] - yi_x2[0]) )*
                    ( (y - yi_x2[1]) / (yi_x2[2] - yi_x2[1]) )*
                    ( (y - yi_x2[3]) / (yi_x2[2] - yi_x2[3]) )*
                    ( (y - yi_x2[4]) / (yi_x2[2] - yi_x2[4]) ) )

# Para i = 3
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x2[0]) / (yi_x2[3] - yi_x2[0]) )*
                    ( (y - yi_x2[1]) / (yi_x2[3] - yi_x2[1]) )*
                    ( (y - yi_x2[2]) / (yi_x2[3] - yi_x2[2]) )*
                    ( (y - yi_x2[4]) / (yi_x2[3] - yi_x2[4]) ) )

# Para i = 4
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x2[0]) / (yi_x2[4] - yi_x2[0]) )*
                    ( (y - yi_x2[1]) / (yi_x2[4] - yi_x2[1]) )*
                    ( (y - yi_x2[2]) / (yi_x2[4] - yi_x2[2]) )*
                    ( (y - yi_x2[3]) / (yi_x2[4] - yi_x2[3]) ) )


# Para X = 3
# Para i = 0

funcion_vi_y.append(lambda y: 
                    ( (y - yi_x3[1]) / (yi_x3[0] - yi_x3[1]) )*
                    ( (y - yi_x3[2]) / (yi_x3[0] - yi_x3[2]) )*
                    ( (y - yi_x3[3]) / (yi_x3[0] - yi_x3[3]) )*
                    ( (y - yi_x3[4]) / (yi_x3[0] - yi_x3[4]) ) )

# Para i = 1
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x3[0]) / (yi_x3[1] - yi_x3[0]) )*
                    ( (y - yi_x3[2]) / (yi_x3[1] - yi_x3[2]) )*
                    ( (y - yi_x3[3]) / (yi_x3[1] - yi_x3[3]) )*
                    ( (y - yi_x3[4]) / (yi_x3[1] - yi_x3[4]) ) )

# Para i = 2
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x3[0]) / (yi_x3[2] - yi_x3[0]) )*
                    ( (y - yi_x3[1]) / (yi_x3[2] - yi_x3[1]) )*
                    ( (y - yi_x3[3]) / (yi_x3[2] - yi_x3[3]) )*
                    ( (y - yi_x3[4]) / (yi_x3[2] - yi_x3[4]) ) )

# Para i = 3
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x3[0]) / (yi_x3[3] - yi_x3[0]) )*
                    ( (y - yi_x3[1]) / (yi_x3[3] - yi_x3[1]) )*
                    ( (y - yi_x3[2]) / (yi_x3[3] - yi_x3[2]) )*
                    ( (y - yi_x3[4]) / (yi_x3[3] - yi_x3[4]) ) )

# Para i = 4
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x3[0]) / (yi_x3[4] - yi_x3[0]) )*
                    ( (y - yi_x3[1]) / (yi_x3[4] - yi_x3[1]) )*
                    ( (y - yi_x3[2]) / (yi_x3[4] - yi_x3[2]) )*
                    ( (y - yi_x3[3]) / (yi_x3[4] - yi_x3[3]) ) )

#Para X = 4
#Para i = 0
funcion_vi_y.append(lambda y: 
                    ( (y - 0) / (yi_x4 - 0) ) )


# Para X = 5
# Para i = 0

funcion_vi_y.append(lambda y: 
                    ( (y - yi_x5[1]) / (yi_x5[0] - yi_x5[1]) )*
                    ( (y - yi_x5[2]) / (yi_x5[0] - yi_x5[2]) ) )

# Para i = 1
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x5[0]) / (yi_x5[1] - yi_x5[0]) )*
                    ( (y - yi_x5[2]) / (yi_x5[1] - yi_x5[2]) ) )

# Para i = 2
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x5[0]) / (yi_x5[2] - yi_x5[0]) )*
                    ( (y - yi_x5[1]) / (yi_x5[2] - yi_x5[1]) ) )


# Para X = 6
# Para i = 0

funcion_vi_y.append(lambda y: 
                    ( (y - yi_x6[1]) / (yi_x6[0] - yi_x6[1]) )*
                    ( (y - yi_x6[2]) / (yi_x6[0] - yi_x6[2]) ) )

# Para i = 1
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x6[0]) / (yi_x6[1] - yi_x6[0]) )*
                    ( (y - yi_x6[2]) / (yi_x6[1] - yi_x6[2]) ) )

# Para i = 2
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x6[0]) / (yi_x6[2] - yi_x6[0]) )*
                    ( (y - yi_x6[1]) / (yi_x6[2] - yi_x6[1]) ) )


# Para X = 7
# Para i = 0

funcion_vi_y.append(lambda y: 
                    ( (y - yi_x7[1]) / (yi_x7[0] - yi_x7[1]) )*
                    ( (y - yi_x7[2]) / (yi_x7[0] - yi_x7[2]) )*
                    ( (y - yi_x7[3]) / (yi_x7[0] - yi_x7[3]) )*
                    ( (y - yi_x7[4]) / (yi_x7[0] - yi_x7[4]) )*
                    ( (y - yi_x7[5]) / (yi_x7[0] - yi_x7[5]) )*
                    ( (y - yi_x7[6]) / (yi_x7[0] - yi_x7[6]) ) )

# Para i = 1
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x7[0]) / (yi_x7[1] - yi_x7[0]) )*
                    ( (y - yi_x7[2]) / (yi_x7[1] - yi_x7[2]) )*
                    ( (y - yi_x7[3]) / (yi_x7[1] - yi_x7[3]) )*
                    ( (y - yi_x7[4]) / (yi_x7[1] - yi_x7[4]) )*
                    ( (y - yi_x7[5]) / (yi_x7[1] - yi_x7[5]) )*
                    ( (y - yi_x7[6]) / (yi_x7[1] - yi_x7[6]) ) )

# Para i = 2
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x7[0]) / (yi_x7[2] - yi_x7[0]) )*
                    ( (y - yi_x7[1]) / (yi_x7[2] - yi_x7[1]) )*
                    ( (y - yi_x7[3]) / (yi_x7[2] - yi_x7[3]) )*
                    ( (y - yi_x7[4]) / (yi_x7[2] - yi_x7[4]) )*
                    ( (y - yi_x7[5]) / (yi_x7[2] - yi_x7[5]) )*
                    ( (y - yi_x7[6]) / (yi_x7[2] - yi_x7[6]) ) )

# Para i = 3
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x7[0]) / (yi_x7[3] - yi_x7[0]) )*
                    ( (y - yi_x7[1]) / (yi_x7[3] - yi_x7[1]) )*
                    ( (y - yi_x7[2]) / (yi_x7[3] - yi_x7[2]) )*
                    ( (y - yi_x7[4]) / (yi_x7[3] - yi_x7[4]) )*
                    ( (y - yi_x7[5]) / (yi_x7[3] - yi_x7[5]) )*
                    ( (y - yi_x7[6]) / (yi_x7[3] - yi_x7[6]) ) )

# Para i = 4
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x7[0]) / (yi_x7[4] - yi_x7[0]) )*
                    ( (y - yi_x7[1]) / (yi_x7[4] - yi_x7[1]) )*
                    ( (y - yi_x7[2]) / (yi_x7[4] - yi_x7[2]) )*
                    ( (y - yi_x7[3]) / (yi_x7[4] - yi_x7[3]) )*
                    ( (y - yi_x7[5]) / (yi_x7[4] - yi_x7[5]) )*
                    ( (y - yi_x7[6]) / (yi_x7[4] - yi_x7[6]) ) )

# Para i = 5
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x7[0]) / (yi_x7[5] - yi_x7[0]) )*
                    ( (y - yi_x7[1]) / (yi_x7[5] - yi_x7[1]) )*
                    ( (y - yi_x7[2]) / (yi_x7[5] - yi_x7[2]) )*
                    ( (y - yi_x7[3]) / (yi_x7[5] - yi_x7[3]) )*
                    ( (y - yi_x7[4]) / (yi_x7[5] - yi_x7[4]) )*
                    ( (y - yi_x7[6]) / (yi_x7[5] - yi_x7[6]) ) )

# Para i = 6
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x7[0]) / (yi_x7[6] - yi_x7[0]) )*
                    ( (y - yi_x7[1]) / (yi_x7[6] - yi_x7[1]) )*
                    ( (y - yi_x7[2]) / (yi_x7[6] - yi_x7[2]) )*
                    ( (y - yi_x7[3]) / (yi_x7[6] - yi_x7[3]) )*
                    ( (y - yi_x7[4]) / (yi_x7[6] - yi_x7[4]) )*
                    ( (y - yi_x7[5]) / (yi_x7[6] - yi_x7[5]) ) )


# Para X = 8
# Para i = 0
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x8[1]) / (yi_x8[0] - yi_x8[1]) )*
                    ( (y - yi_x8[2]) / (yi_x8[0] - yi_x8[2]) )*
                    ( (y - yi_x8[3]) / (yi_x8[0] - yi_x8[3]) )*
                    ( (y - yi_x8[4]) / (yi_x8[0] - yi_x8[4]) ) )

# Para i = 1
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x8[0]) / (yi_x8[1] - yi_x8[0]) )*
                    ( (y - yi_x8[2]) / (yi_x8[1] - yi_x8[2]) )*
                    ( (y - yi_x8[3]) / (yi_x8[1] - yi_x8[3]) )*
                    ( (y - yi_x8[4]) / (yi_x8[1] - yi_x8[4]) ) )

# Para i = 2
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x8[0]) / (yi_x8[2] - yi_x8[0]) )*
                    ( (y - yi_x8[1]) / (yi_x8[2] - yi_x8[1]) )*
                    ( (y - yi_x8[3]) / (yi_x8[2] - yi_x8[3]) )*
                    ( (y - yi_x8[4]) / (yi_x8[2] - yi_x8[4]) ) )

# Para i = 3
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x8[0]) / (yi_x8[3] - yi_x8[0]) )*
                    ( (y - yi_x8[1]) / (yi_x8[3] - yi_x8[1]) )*
                    ( (y - yi_x8[2]) / (yi_x8[3] - yi_x8[2]) )*
                    ( (y - yi_x8[4]) / (yi_x8[3] - yi_x8[4]) ) )

# Para i = 4
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x8[0]) / (yi_x8[4] - yi_x8[0]) )*
                    ( (y - yi_x8[1]) / (yi_x8[4] - yi_x8[1]) )*
                    ( (y - yi_x8[2]) / (yi_x8[4] - yi_x8[2]) )*
                    ( (y - yi_x8[3]) / (yi_x8[4] - yi_x8[3]) ) )


# Para X = 9
# Para i = 0

funcion_vi_y.append(lambda y: 
                    ( (y - yi_x9[1]) / (yi_x9[0] - yi_x9[1]) )*
                    ( (y - yi_x9[2]) / (yi_x9[0] - yi_x9[2]) ) )

# Para i = 1
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x9[0]) / (yi_x9[1] - yi_x9[0]) )*
                    ( (y - yi_x9[2]) / (yi_x9[1] - yi_x9[2]) ) )

# Para i = 2
funcion_vi_y.append(lambda y: 
                    ( (y - yi_x9[0]) / (yi_x9[2] - yi_x9[0]) )*
                    ( (y - yi_x9[1]) / (yi_x9[2] - yi_x9[1]) ) )