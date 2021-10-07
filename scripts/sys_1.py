
## script, abrir con cmd ejemplo: python sys_1.py "palabra" 5
import sys
print("hola")
if len(sys.argv)==3:
	texto=sys.argv[1]
	repeticiones=int(sys.argv[2])
	for r in range(repeticiones):
		print(texto)
else:
	print("introduce los argumentos correctamente")
