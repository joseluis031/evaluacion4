class nodoArbol(object):
    
    def __init__(self,info):
        self.izq = None
        self.der = None
        self.info = info
        
def insertar_nodo(raiz,dato):
        if raiz is None:
            raiz = nodoArbol(dato)
        elif dato < raiz.info:
            raiz.izq = insertar_nodo(raiz.izq,dato)
        else:
            raiz.der = insertar_nodo(raiz.der,dato)
        return raiz

def buscar(raiz,clave):
    pos = None
    if raiz is not None:
        if raiz.info == clave:
            pos = raiz
        elif clave < raiz.info:
            pos = buscar(raiz.izq, clave)
        else:
            pos = buscar(raiz.der, clave)
    return pos