def CuentaAtras(num):
	num-=1
	if num>0:
		print(num)
		CuentaAtras(num)				# Funcion llamada a si misma
	else:
		print("fin de la cuenta")
	print(f"fin de la funcion {num}")	# el mensaje se muestra al final de cada ocacion 
										# que se llamo la funcion a si misma

CuentaAtras(5)	

## Factorial
def Factorial(num):
	print(f"Valor inicial = {num}")
	if num>1:
		num=num*Factorial(num-1)
	print(f"Valor final = {num}")
	return num
n=5
print(f"factorial de {n} = {Factorial(n)}")