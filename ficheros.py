from io import open
texto = "Una linea con texto\nOtra linea con texto"
fichero = open('fichero.txt','w')	# Modo escritura (borra toda la informacion del fichero y escribe desde el inicio)
fichero.write(texto)
fichero.close()
##
del(fichero)
fichero = open('fichero.txt','r')	# Modo lectura
texto = fichero.read()
fichero.close()
print(texto)
##
fichero = open('fichero.txt','r')
lineas = fichero.readlines()
fichero.close()
print(lineas)
##
fichero = open('fichero.txt','a')	# Modo append (permite escribir en el fichero sin eliminar la informacion)
fichero.write('\nUltima linea')		# tambien permite crear un documento que no existe
fichero.close()
##
with open('fichero.txt','r') as fichero:	# Recorrer cada linea de un fichero
	for linea in fichero:
		print(linea)
fichero.close()
## Puntero
fichero = open('fichero.txt','r')
fichero.seek(10)					# posiciona el puntero en el caracter #10
print(fichero.read())
fichero.seek(0)
print(fichero.read(5))				# Lee solo 5 caracteres
fichero.seek(0)
texto = fichero.read()
fichero.seek(len(texto)/2)			# Posiciona el puntero a la mitad del texto
print(fichero.read())
fichero.seek(0)
fichero.seek(len(fichero.readline()))	# Posiciona el puntero al final de la primer linea
print(fichero.read())
fichero.close()
##
fichero = open('fichero.txt','r+')	# Modo lectura/escritura (permite escribir desde el inicio del fichero)
fichero.write('*********')
fichero.close()
## Modificar linea #3
fichero = open('fichero.txt','r+')
lineas = fichero.readlines()
lineas[2] = 'linea modificada\n'
fichero.seek(0)
fichero.writelines(lineas)
fichero.close()
