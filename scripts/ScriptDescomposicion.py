# python ScriptDescomposicion.py [int]
import sys
if len(sys.argv)==2:
	numero=sys.argv[1]
	longitud=len(numero)
	unidades={1:"unidad",2:"decena",3:"centena",4:"unidad de millar",5:"decena de millar"}
	numero=numero[::-1]
	for i in range(longitud):
		num=int(numero[i]) * 10**i # numero*(10^i)
		print(f"{num:5d} {unidades[i+1]}")
else:
	print("error")