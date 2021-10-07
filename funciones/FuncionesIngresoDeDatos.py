def resta(a=None,b=None):
	if a == None or b== None:
		print("error, debes pasar dos numeros")
		return
	else:
		return a-b
a=4
b=3
resta()
print(f"resta = {resta(b,a)}")
## Paso por valor o por referencia
def doblar_valor(numero):
    numero *= 2

n = 10
doblar_valor(n)
print(n)		# la variable 'n' no es afectada (paso por valor)
#
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

ns = [10,50,100]
doblar_valores(ns)
print(ns)		# la variable ns si se afecta (aplica listas) (paso por referencia) 
## evitar el paso por referencia
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

ns = [10,50,100]
doblar_valores(ns[:])	# lo que se envia a la funcion no es la lista si no una copia
print(ns)				# por eso la lista ns no se modifica
## evitar paso por valor
def doblar_valor(numero):
    return numero * 2
n = 10
n = doblar_valor(n)		# La variable n es modificada, asignando su valor a la copia
print(n)		