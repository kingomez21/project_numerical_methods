
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
# Paara i = 0

funcion_vi_y.append(lambda y: 
                    ( (y - yi_x1[1]) / (yi_x1[0] - yi_x1[1]) )*
                    ( (y - yi_x1[2]) / (yi_x1[0] - yi_x1[2]) )*
                    ( (y - yi_x1[3]) / (yi_x1[0] - yi_x1[3]) )*
                    ( (y - yi_x1[4]) / (yi_x1[0] - yi_x1[4]) )*
                    ( (y - yi_x1[5]) / (yi_x1[0] - yi_x1[5]) )*
                    ( (y - yi_x1[6]) / (yi_x1[0] - yi_x1[6]) ) )
