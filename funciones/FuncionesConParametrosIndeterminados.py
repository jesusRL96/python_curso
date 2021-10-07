# por posicion (tupla)
def indeterminados_posicion(*args):
    for arg in args:
        print(arg)

indeterminados_posicion(5,"Hola",[1,2,3,4,5])
# por nombre (Diccionario)
def indeterminados_nombre(**kwargs):
    print(kwargs)
indeterminados_nombre(n=5, c="Hola", l=[1,2,3,4,5])

def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])
indeterminados_nombre(n=5, c="Hola", l=[1,2,3,4,5])

# Por nombre y por posicion
def super_funcion(*args,**kwargs):
    total = 0
    for arg in args:		# suma los argumentos por posicion
        total += arg
    print("sumatorio => ", total)
    for kwarg in kwargs:	# muestara los valores por nombre
        print(kwarg, "=>", kwargs[kwarg])

super_funcion(10, 50, -1, 1.56, 10, 20, 300, nombre="Hector", edad=27)
# Los nombres args y kwargs no son obligatorios, pero se suelen utilizar por convencion.
