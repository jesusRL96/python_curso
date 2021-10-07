def saludar():
	print("hola desde funcion")

saludar()
## retornando valores
def test():
	return "valor regresado"

print(test())
## con listas
def test():
	return [1,2,3,4,5]
print(test()[0])
## con tupla
def test():
	return "cadena",10,[10,20,50]
print(test())
cadena,num,lis=test()
print(f"una cadena '{cadena}'\n un numero '{num}'\n una lista '{lis}'")
