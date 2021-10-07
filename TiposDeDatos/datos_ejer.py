usuarios={"juan","pedro","maria","roberto"}
administradores={"maria","pedro","marco"}
administradores.discard("marco")
for usuario in usuarios:
	if usuario in administradores:
		print(usuario," es un administrador")
	else:
		print(usuario," no es un administrador") 
## personajes (diccionario)
guerrero={"vida":2,"ataque":2,"defensa":2,"alcance":2}
caballero={"vida":2,"ataque":2,"defensa":2,"alcance":2}
arquero={"vida":2,"ataque":2,"defensa":2,"alcance":2}
#
caballero["vida"]=guerrero["vida"]*2
caballero["defensa"]=guerrero["defensa"]*2

guerrero["ataque"]=caballero["ataque"]*2
guerrero["alcance"]=caballero["alcance"]*2

arquero["vida"]=guerrero["vida"]
arquero["ataque"]=guerrero["ataque"]
arquero["defensa"]=guerrero["defensa"]/2
arquero["alcance"]=guerrero["alcance"]*2
print("caballero:\t",caballero)
print("guerrero:\t",guerrero)
print("arquero:\t",arquero)
## Tareas 
tareas=[
		[6,'tareas'],
		[2,'diseño'],
		[1,'concepcion'],
		[7,'mantenimiento'],
		[4,'producion'],
		[3,'planificacion'],
		[5,'pruebas']]
print("lista desordenada:")
for tarea in tareas:
	print(tarea[0],tarea[1])
	pass
from collections import deque

tareas.sort()	# ordena la lista
print(tareas)
# ordenamiento
cola=deque()
for tarea in tareas:
	cola.append(tarea[1])
	pass
print("lista ordenada:")
for tarea in cola:
	print(tarea)
	pass
actividad=cola.popleft()
print("actividad a hacer:",actividad)
print(cola)