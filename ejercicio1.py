class NodoArbol:
   
   def __init__(self,simb,frec):
        self.izq = None
        self.der = None
        self.padre = None
        self.simb = simb
        self.frec = frec
    
def buscar(raiz,clave):
    pos = None
    if raiz is not None:
        if raiz.simb == clave:
            pos = raiz
        elif clave < raiz.info:
            pos = buscar(raiz.izq, clave)
        else:
            pos = buscar(raiz.der, clave)
    return pos