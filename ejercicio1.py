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


import heapq

def tree(probs):
    q = []
    # Agregamos todos los símbolos a la pila
    for ch,pr in probs.items():
        # La fila de prioridad está ordenada por
        # prioridad y profundidad
        heapq.heappush(q,(pr,0,ch))

    # Empezamos a mezclar símbolos juntos
    # hasta que la fila tenga un elemento
    while len(q) > 1:
        e1 = heapq.heappop(q) # El símbolo menos probable
        e2 = heapq.heappop(q) # El segundo menos probable
        
        # Este nuevo nodo tiene probabilidad e1[0]+e2[0]
        # y profundidad mayor al nuevo nodo
        nw_e = (e1[0]+e2[0],max(e1[1],e2[1])+1,[e1,e2])
        heapq.heappush(q,nw_e)
    return q[0] # Devolvemos el arbol sin la fila

a = tree({'a':0.2,'f':0.17,"1":0.13,"3":0.21,"0":0.05,"M":0.09,"T":0.15})
print(a)



def dict(tree):
    lista = {}
    pila = []
    pila.append(tree+("",))
    
    while len(pila) > 0:
        quitar = lista.pop()
        if type(quitar[2]) == list:
            pila.append(quitar[2][1]+("0",))
            pila.append(quitar[2][0]+("1",))
            
            continue
        else:
            code = quitar[-1]
            lista[pila[2]] = code
        pass
    return lista
b = dict("aaaaaaavbbbbf")
print(b)