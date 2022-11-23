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

def compress(dic,content):
    res = ""
    # Iteramos sobre cada elemento del archivo de entrada
    for ch in content:
        code = dic[ch]
        res = res + code
    # Agregamos el 1 a la izquierda, y el marcador de final
    # a la derecha
    res = '1' + res + dic['end']
    # Agregamos ceros para que la longitud del resultado
    # sea un múltiplo de 8
    res = res + (len(res) % 8 * "0")
    return int(res,2) # Convertimos a entero! (2 porque es base 2
            