dict_binario = {"a":00,"3":"01","1":100,"0":1010,"M":1011,"T":110,"f":111}
dict_binario
def comprimir(texto):
    separador = ""
    contador = 0
    
    for letra in texto:
        separador += dict_binario       
        if contador +1 < len(texto):
            separador += contador
        contador +=1
    
    return separador
c="skodf"
comprimir("f")

def codificar(texto):
        codificado = []
        if texto[0] in dict_binario:
            texto.pop(0)
            for i in texto:
                codificado += dict_binario[i]
        else:
            pass
        return codificado
    
a=list("afTMT")
codificar(a)