class caballo:
    def __init__(self, tiempo, nombre):
        self.tiempo = tiempo
        self.nombre = nombre
        self.izquierda = None
        self.derecha = None 
        
class Arbol:
    def __init__(self, tiempo, nombre):
        self.raiz = caballo(tiempo, nombre)

    def _privagregar(self, nodo, tiempo, nombre):
        if tiempo < nodo.tiempo:
            if nodo.izquierda is None:
                nodo.izquierda = caballo(tiempo, nombre)
            else:
                self._privagregar(nodo.izquierda, tiempo, nombre)
        else:
            if nodo.derecha is None:
                nodo.derecha = caballo(tiempo, nombre)
            else:
                self._privagregar(nodo.derecha, tiempo, nombre)

    def _privlista(self, nodo):
        if nodo is not None:
            self._privlista(nodo.derecha)
            print(nodo.nombre, "-", nodo.tiempo,"pts")
            self._privlista(nodo.izquierda)
            
    def __buscar(self, nodo, tiempo):
       if nodo is None:
           return None
       if nodo.tiempo == tiempo:
           return nodo
       if tiempo < nodo.tiempo:
           return self.__buscar(nodo.izquierda, tiempo)
       else:
           return self.__buscar(nodo.derecha, tiempo)
            
    def agregar(self, tiempo, nombre):
        self._privagregar(self.raiz, tiempo, nombre)

    def lista(self):
        print("\nLista de caballos en orden: ")
        self._privlista(self.raiz)
        print("")
        
    def buscar(self, tiempo):
        return self.__buscar(self.raiz, tiempo)