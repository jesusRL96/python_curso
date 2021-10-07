##tuplas, usa metodos muy similares a las listas pero no pueden ser modificadas
tupla=(10,[1,2,3],"hola",-50);
print(tupla,"\n",tupla[0],"\n",tupla[1],"\n",tupla[1:],) ## No se puede redefinir el valor de una tupla
print(len(tupla),len(tupla[1]))
print(tupla.index(-50))	## dice el indice en donde se encuentra el valor -50
print(tupla.count(-50))	## Cuenta las veces que esta -50 en la tupla

## Conjuntos
print("conjuntos\n")
conjuntoV=set()	##Conjunto vacio
conjunto={1,2,3}	## Conjunto inicializado 
conjunto.add(4)	# Metodo para agregar valores
print(conjunto)
conjunto.add(0)	# Agrega elementos al conjunto en colecciones desordenadas
print(conjunto)
conjunto.add('A')
conjunto.add('H')
conjunto.add('Z')
conjunto.discard('A')
print(conjunto)
test={"jesus","jesus","jesus"}	## Elimina los valores repetidos
print(test)
l=[1,2,5,5,2,3,1]
c=set(l)	#transforma la lista l a un conjunto
print(c)	#los valores repetidos son eliminados
l=list(c)	#transforma conjunto a lista
l=list(set(l))	#hace todo lo anterior
cad="hola mundo"	# Se puede hacer lo mismo con cadenas
c=set(cad)
print(c)
## Diccionarios
diccionarioVacio={}
type(diccionarioVacio)	#muestra el tipo de variable
colores={"amarillo":"yellow","azul":"blue","verde":"green"}
print(colores)	# No es ordenado
print(colores["amarillo"])	#se usa la palabra clave "amarillo" para ingresar al valor ("yellow")
numeros={1:"numero1",2:"numero2",3:"numero3"}
print(numeros[2])			#tambien se pueden usar numeros
colores["amarillo"]="amarillow"	#se pueden modificar los valores refiriendonos a la palabra clave
print(colores)
del(colores["azul"])	#se pueden borrar lo valores
print(colores)
edades={"jesus":22,"juan":33,"mario":22,"oscar":50}
edades["jesus"]+=1
print(edades)
for clave in edades:	## acceder a valores de un diccionario
	print(clave," tiene: ",edades[clave])		## la variable edad hace referencia a las palabras clave
## Otro metodo para hacerlo (uso de items)
print("lo mismo pero con items")
for clave,valor in edades.items():
	print(clave,valor)
## Personajes
personajes=[]	#lista vacia
p1={"Nombre":"Jesus","Pais":"Mexico","ocupacion":"estudiante"}
p2={"Nombre":"juan","Pais":"guatemala","ocupacion":"huachicolero"}
p3={"Nombre":"maria","Pais":"colombia","ocupacion":"estudiante"}
personajes.append(p1)
personajes.append(p2)
personajes.append(p3)
print(personajes)
for p in personajes:
	#print(p)
	print(p["Nombre"],p["Pais"],p["ocupacion"])


