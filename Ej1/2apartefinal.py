def codificar(texto):
    binario = " ".join(format(ord(i), "b")for i in texto) #b implica formato binario
    print("La codificacion del texto es la siguiente:")
    return binario

a = input("¿que deseas codificar?")
b = codificar(a)
print(b)
