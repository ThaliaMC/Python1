
import random

def array_aleatorio(n):
    array =[0]*n
    for i in range (n) :
        array[i]=random.randint(0,100)
    return array

print("Ingrese del tamaño del array ")
n= int(input())

aleatorio=array_aleatorio(n)
print(aleatorio)


