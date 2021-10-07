import math 
def AreaCirculo(radio):
	return math.pi*(radio**2)

print("area del circulo",AreaCirculo(5))

def intermedio(a,b):
	return (a-b)/2

print(intermedio(-20,-5))

def recortar(numero, minimo, maximo):
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    return numero

print( recortar(15, 0, 10) )

numeros = [-12, 84, 13, 20, -33, 101, 9]

# Completa el ejercicio aquí

def separar(lista):
    lista.sort()
    pares = []
    impares = []
    for n in lista:
        if n%2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares, impares

pares, impares = separar(numeros)
print(pares)
print(impares)