from fun import *
import numpy as np
import os
import time

salir = 1
while salir !=0:
    os.system('cls')

    list = np.array([[0,0,0],[0,0,0],[0,0,0]])
    cont = 0
    for i in range(0,3):
        for j in range(0,3):
            print("----- Matriz transpose -----")
            
            print("\n  Matriz actual:")
            print(list)

            user = int(input("\nIngrese el "+ str(cont+1) + "° número de su matriz: "))
            list[i][j] = user

            cont+=1
            os.system('cls')

    print("Su matriz:")
    print(list)
    print("\nMatriz transpuesta")
    final = transpose_no_np(list)
    print(final[0])
    print(final[1])
    print(final[2])

    print("---------------------------")
    salir=int(input("Si desea salir marque 0, \nsi no, marque cualquier otra tecla: "))
    print("---------------------------")

os.system('cls')
print('(V)\n(. .)\nc(”)(”) Adios')
time.sleep(2)
os.system('cls')

