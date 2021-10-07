n1=float(input("Ingresa el primer numero: "))
n2=float(input("Ingresa el segundo numero: "))
print("Son iguales?",n1==n2)
print("Son iguales?",n1!=n2)
##
cadena=input("Escribe una cadena")
lon=len(cadena)
print("es mayor que 3 y menor que 10?",3<lon<10)
##
NumeroMagico=12345679
NumeroUsuario=int(input("ingresa un numero entero entre 1 y 9: "))
NumeroUsuario*=9
NumeroMagico*=NumeroUsuario
print("Numero Magico: ",NumeroMagico)
##
comando="Salir"
if comando=="Entrar":
	print("Entrar")
elif comando=="saluda":
	print("hola")
elif comando=="Salir":
	print("Salir")
else:
	print("comando no reconocido")
pass