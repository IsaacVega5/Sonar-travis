import numpy as np


def transpose_np(x):
    y=np.transpose(x)
    return y

def transpose_no_np(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    matrix_T = []
    for j in range(rows):
        row = []
        for i in range(rows):
           row.append(matrix[i][j])
        matrix_T.append(columns)

    return matrix_T

def create_mx(a,b,c,d,e,f,g,h,i):
    x = np.array ([[a, d, g],
                   [b, e, h],
                   [c, f, i]])
    return x

def transpose_mx_gui(user, result):
    x = create_mx(user[0].get(),user[1].get(), user[2].get(),
                  user[3].get(),user[4].get(), user[5].get(),
                  user[6].get(),user[7].get(), user[8].get(),)

    y = transpose_no_np(x)
    cont = 0;
    for i in range(0,3):
        for x in range(0,3):
            result[cont].config(state= "normal")
            result[cont].delete(0, "end")
            result[cont].insert(0, y[i][x])
            result[cont].config(state= "disabled")
            cont+=1

def clear_txt(user, result):
    for i in range(0,len(user)):
        user[i].delete(0, "end")
        result[i].config(state= "normal")
        result[i].delete(0, "end")
        result[i].config(state= "disabled")
    
