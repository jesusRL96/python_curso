class A:
    def __init__(self):
        print("Soy de clase A")
    def a(self):
        print("Este método lo heredo de A")

class B:
    def __init__(self):
        print("Soy de clase B")
    def b(self):
        print("Este método lo heredo de B")

class C(B,A):
    def c(self):
        print("Este método es de C")


c = C()     # Se ejecuta el metodo __init__ de la clase B por que fue declarado a la izquierda al definir la clace C
c.a()
c.b()
c.c()