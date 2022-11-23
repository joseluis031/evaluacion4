class NodoArista():
    def __init__(self, info, destino):
        self.info = info
        self.destino = destino
        self.sig = None
        
class NodoVertice():
    def __init__(self,info,nombre,pais):
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista()
        self.nombre = nombre
        self.pais = pais
        
class Arista():
    def __init__(self):
        self.inicio = None
        self.tamanio = 0
        
class Grafo():
    def __init__(self, dirigido=False):
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0