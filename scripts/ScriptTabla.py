import sys
# python ScriptTabla.py [int] [int]
if len(sys.argv)==3:
	filas=int(sys.argv[1])
	columnas=int(sys.argv[2])
	print(sys.argv[0])
	for fila in range(filas):
		for columna in range(columnas):
			print("*",end='')		# end es para no agregar salto de linea
		print()	#salto de linea
else:
	print("error")