class NodoArbol:
       
   def __init__(self,info,texto):
        self.izq = None
        self.der = None
        self.info = info
        self.altura = 0
        self.texto = texto
    
def altura(raiz):
    if raiz is None:
        return -1
    else:
        return raiz.altura
    
def actualizar_altura(raiz):
    if raiz is not None:
        alt_izq = altura(raiz.izquierda)
        alt_der = altura(raiz.derecha)
        raiz.altura = (alt_izq if alt_izq > alt_der else alt_der) +1
        
def rotar_simple(raiz, control):
    if control:
        aux = raiz.izquierda
        raiz.izquierda = aux.derecha
        aux.derecha = raiz
    else:
        aux = raiz.derecha
        raiz.izquierda = aux.izquierda
        aux.izquierda = raiz
        
def rotar_doble(raiz, control):
    if control:
        raiz.izquierda = rotar_simple(raiz.izquierda, False)
        raiz = rotar_simple(raiz, True)
    else:
        raiz.derecha = rotar_simple(raiz.derecha, True)
        raiz = rotar_simple(raiz, False)
    return raiz

def balancear(raiz):
    if raiz is not None:
        if (altura(raiz.izquierda)-altura(raiz.derecha)) ==2:
            if (raiz.izquierda.izquierda) >= altura(raiz.izquierda.derecha):
                raiz = rotar_simple(raiz, True)
            else:
                raiz = rotar_doble(raiz, True)
        elif (altura(raiz.derecha)-altura(raiz.izquierda)) == 2:
            if altura(raiz.derecha.derecha) >= altura(raiz.derecha.derecha):
                raiz = rotar_simple(raiz, False)
            else:
                raiz = rotar_doble(raiz, False)
    return raiz

def insertar_nodo(raiz,dato,pos):
    if raiz == None:
        print("Nodo raiz")
        raiz = NodoArbol(dato,pos)
    else:
        while True:
            if dato < raiz.info:
                if raiz.izquierda is None:
                    raiz.izquierda = NodoArbol(dato, pos)
                    raiz.izquierda.padre = raiz
                    break
                else:
                    raiz = raiz.izquierda
            else:
                if raiz.derecha is None:
                    raiz.derecha = NodoArbol(dato, pos)
                    raiz.derecha.padre = raiz
                    break
                else:
                    raiz = raiz.derecha
                    
    raiz = balancear(raiz)
    actualizar_altura(raiz)
    return raiz

def reemplazar(raiz):
    aux = None
    if raiz.derecha is None:
        aux = raiz
        raiz = raiz.izquierda
        
    else:
        raiz.derecha, aux = reemplazar(raiz.derecha)
    return raiz, aux

def eliminar_nodo(raiz, clave):
    x = None
    if raiz is not None:
        raiz.izquierda, x = eliminar_nodo(raiz.izquierda, clave)
    elif clave > raiz.info:
        raiz.derecha, x = eliminar_nodo(raiz.derecha, clave)
    else:
        x = raiz.info
        if raiz.izquierda is None:
            raiz = raiz.derecha
        elif raiz.derecha is None:
            raiz = raiz.izquierda
        else:
            raiz.izquierda, aux = reemplazar(raiz.izquierda)
    raiz = balancear(raiz)
    actualizar_altura(raiz)
    return raiz, x

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
