# Pilas
pila=[1,2,3,4]
pila.append(5)
print(pila)
V=pila.pop()	# Saca el ultimo elemento y tambien lo elimina, guardandolo en V
print(V)
print(pila)
# Colas
from collections import deque
cola=deque()
cola=deque(["juan","jose","jesus"])
print(cola)
cola.append("maria")
cola.append("josefa")
print(cola)
C=cola.popleft()	# elimina el elemento de la izquierda y lo guarda en C
print(C)
print(cola)
