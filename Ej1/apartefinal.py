separador = " "

def codificar(texto):
    binario = " ".join(format(ord(i), "b")for i in texto) #b implica formato binario
    print("La codificacion del texto es la siguiente:")
    return binario

def decimal(binario):
    valor = int(binario, 2)
    return chr(valor) # recibe un número y devuelve su representación como carácter


def decodificar(texto2):
    texto_vacio = ""
    for i in texto2.split(separador):
        texto_vacio += decimal(i)
    return texto_vacio

a = input("¿que deseas codificar?")
b = codificar(a)
print(b)

c = input("¿que deseas decodificar(en binario por favor)?")
d = decodificar(c)
print(d)

