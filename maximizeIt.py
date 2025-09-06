from itertools import product

K, M = map(int, input().split())
listas = []
for _ in range(K):
    datos = list(map(int, input().split()))
    listas.append(datos[1:])

maximo = 0
for combinacion in product(*listas):
    valor = sum(x**2 for x in combinacion) % M
    if valor > maximo:
        maximo = valor

print(maximo)
