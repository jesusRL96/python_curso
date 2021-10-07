c=0
while c<=6:
	c+=1
	if c==4:
		print("rompemos el bucle cuando c vale 4")
		break	## Rompe un bucle (tampoco se ejecuta el else)
	print(c)
else:
	print("se ah completado la iteracion y c vale: ",c)
##
print("\n")
c=0
while c<=7:
	c+=1
	if (c==4 or c==6):
		print("deberia ser: ",c)
		continue	## continua con el bucle pero se salta los valores las lineas siguientes a 
		print("este no se ejecuta, ni lo de abajo hasta el siguiente bucle")
	print(c)
else:
	print("se ah completado la iteracion y c vale: ",c)
pass
##Menu
print("\n")
print("Bienvenido al menu interactivo")
while(True):
	print("""¿Que quieres hacer?
		1)Saludar
		2)Sumar
		3)Salir""")
	opcion=int(input())
	if opcion==1:
		print("Hola")
	elif opcion==2:
		n1=input("ingresar valor 1")
		n2=input("ingresar valor 2")
		print("la suma es: ",n1+n2)
	elif opcion==3:
		print("salir")
		break
	else:
		print("Comando desconocido")
## FOR
numeros=[1,2,3,4,5,6,7,8,9,10]
indice=0
while indice<len(numeros):
	print(numeros[indice])
	indice+=1
	pass
print("\n")

for numero in numeros:
	print(numero," ",numeros[numero-1])
	numeros[numero-1]*=10
	pass
print("numeros multiplicados:",numeros)

numeros2=[]
for indice,numero in enumerate(numeros):	## enumerate regresa un indice y un numero de la lista
	numeros[indice]*=10
	numeros2.append(numeros[indice])
print("numeros multiplicados:",numeros)
print("numeros2:",numeros2)

palabra="holaa"
contraseña=""
for caracter in palabra:
	print(caracter)
	contraseña+="*"
print(contraseña)

for i in range(10):
	print(i)
## ejercicios
## 1
print("\n")
print("Bienvenido al menu interactivo")
n1=int(input("ingresar valor 1:"))
n2=int(input("ingresar valor 2:"))
v=True
while(v):
	print("""¿Que quieres hacer?
		1)Sumar
		2)Restar
		3)multiplicar
		4)Salir""")
	opcion=input("ingrese una opcion")
	if opcion=="1":
		print("la suma es: ",n1+n2)
	elif opcion=="2":
		print("la resta es: ",n1-n2)
	elif opcion=='3':
		print("la multiplicacion es: ",n1*n2)
	elif opcion=="4":
		v=False
	else:
		print("Comando desconocido")
##2.
v=0
while v%2==0:
	v=int(input("ingrese un numero impar: "))
else:
	print("adios")
#sumar numeros pares de una lista
lista=range(0,101,2)
print("suma= ",sum(lista))
#media aritmetica
numeros=int(input("cuantos numeros quieres introducir: "))
suma=0
for i in range(numeros):
	suma+=float(input("ingresa el numero "))
print("suma= ",suma,"y la media es: ",suma/numeros )
##
numeros=[1,5,7,8]
while True:
	numero=int(input("escribe un numero del 0 al 9: "))
	if 0<=numero<=9:
		break
if numero in numeros:
	print("se encuentra en la lista")
else:
	print("no se encuentra en la lista")
#range
print("range de 0 a 10", list(range(0,11)))
print("range de -10 a 0", list(range(-10,1)))
print("range de 0 al 20 con saltos de 2", list(range(0,21,2)))
