palabra="palabra"
print(palabra[0])

print(palabra[:-1])
## listas
lista1=[6,6,"ee",'p']
print(lista1)
print(lista1[-1])
print(lista1+lista1)
lista1[2] =966
print(lista1)
lista1.append(1)
print(lista1)
print(lista1[len(lista1)-1])
l2=[[1,3,4,5,6],[1,2,3,4,5],[4,5,6,3,7]]
print(l2)
print(l2[2][3])
##introducir valores por teclado

## 
print("Ejercicio")
matriz=[[1,1,1,2],
		[2,2,3,4],
		[5,6,4,1]]
print("matriz= ",matriz)
for x in range(0,3):
	val=0
	for y in range(0,3):
		val=val+matriz[x][y]
		pass
		#matriz[x][3]=val # el ultimo valor de cada fila es la suma de los anteriores
	#Metodo 2
		matriz[x][3]=sum(matriz[x][:-1])
	pass

print("matriz= ",matriz)
print(matriz[:][:2])
#listas
print("listas")
frutas = ['naranja', 'manzana', 'pera', 'banana', 'kiwi', 'manzana', 'banana']
print(frutas)
print(frutas.count('manzana'))
print(frutas.count('mandarina'))
print(frutas.index('banana'))
print(frutas.index('banana', 4))  # Find next banana starting a position 4
frutas.reverse()
print(frutas)
lista=["hola",20,30,40]
lista.reverse()
print(lista)
#actividad cadena
cadena="zereP nauj,01"
cadenainv=cadena[::-1]	#invertir cadena
print(cadenainv)
coma=cadenainv.index(",")	#lugar donde se encuentra la coma
print(cadenainv[coma+1:],"tiene:",cadenainv[:coma])
# while
valor=0
while valor<=3:
	print(valor)
	valor=valor+1
	pass
#logicos
print(1+1==2)

