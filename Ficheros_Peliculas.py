from io import open
import pickle
fichero = open("catalogo.pckl","wb")
fichero.close()
class Pelicula:

    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:',self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)


class Catalogo:

    peliculas = []

    # Constructor de clase
    def __init__(self):
        self.cargar()

    def agregar(self,p):
        self.peliculas.append(p)
        self.guardar()

    def mostrar(self):
        if len(self.peliculas) == 0:
            print("El catálogo está vacío")
            return
        for p in self.peliculas:
            print(p)

    def cargar(self):
        fichero = open("catalogo.pckl","ab+")
        fichero.seek(0)
        try:
            self.peliculas = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            del(fichero)
            print("Se han cargado {} películas".format(len(self.peliculas)))

    def guardar(self):
        fichero = open("catalogo.pckl","wb")
        pickle.dump(self.peliculas, fichero) 
        fichero.close()
        print("guardado")




# Creamos un catálogo
c = Catalogo()

# Mostramos el contenido
c.mostrar()

# Agregamos unas películas
c.agregar( Pelicula("El Padrino", 175, 1972) )
c.agregar( Pelicula("El Padrino: Parte 2", 202, 1974) )

# Mostramos el catálogo de nuevo
c.mostrar()

# Borramos el catálogo de la memoria ram (persistirá el fichero)
del(c)

# Creamos un catálogo
c = Catalogo()

# Mostramos el contenido
c.mostrar()

# Agregamos una película
c.agregar( Pelicula("Prueba", 100, 2005) )

# Mostramos el catálogo de nuevo
c.mostrar()        