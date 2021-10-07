v='texto'
n=10
c="un texto '{}'' un numero '{}'".format(v,n) # las llaves dicen el lugar donde se agregaran las variables de forma ordenada
print(c)
print("un texto '{1}'' un numero '{0}'".format(v,n)) # con numeros en las llaves se puede cambiar el orden
print("un texto '{v}'' un numero '{n}'".format(n=n,v=v)) # tambien se pueden referenciar con variables
##
print("un texto '{v:>30}'".format(v="palabra")) # alinear a la derecha con 30 caracteres
print("un texto '{v:30}'".format(v="palabra")) # alinear a la izquierda con 30 caracteres
print("un texto '{v:^30}''".format(v="palabra")) # centrar con 30 caracteres
print("un texto '{v:.5}'".format(v="palabra")) # Truncamiento 5 caracteres
print("un texto '{v:^30.4}''".format(v="palabra")) # centrar con 30 caracteres y truncamiento a 4
## Formateo de numeros enteros rellenando con ceros
print("rellenando con ceros")
print("{:04d}".format(100))
print("{:04d}".format(10))
print("{:04d}".format(1000))
## Formateo de numeros enteros rellenando con espacio
print("rellenando con espacios")
print("{:4d}".format(100))
print("{:4d}".format(10))
print("{:4d}".format(1000))
## Formateo de numeros flotantes rellenando con ceros
print("flotantes rellenando con ceros")
print("{:07.3f}".format(3.1416))	
print("{:07.3f}".format(200.12))	#se usa el 7 por que es el numero maximo de digitos
## metodo simplificado
nombre="Jesus"
print(f"nombre: {nombre}")
print(f"nombre: {nombre:^20}")
