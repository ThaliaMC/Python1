numero = []

print("Digite el tamaño :")
n = int(input())
i=0
while i<n:
    print("Ingrese un digito",i+1)
    valor=float(input())
    numero.append(valor)
    i+=1
prom = sum(numero) / len(numero)
print("El promedio de los numero es :",prom)


