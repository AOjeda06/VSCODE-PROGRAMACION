#Crea un diccionario donde las claves sean el conjunto 1 de la siguiente tabla y los valores, el conjunto 2:
#conjunto 1: e i k m p q r s t u v
#conjunto 2: p v i u m t e r k q s
#El programa debe pedir una frase al usuario y debe mostrar la frase encriptada. Para ello, cada vez que encuentre en la 
# frase una letra del conjunto 1 la sustituirá por su correspondiente en el conjunto 2.

#Conjuntos de letras
conjunto1 = ['e', 'i', 'k', 'm', 'p', 'q', 'r', 's', 't', 'u', 'v']
conjunto2 = ['p', 'v', 'i', 'u', 'm', 't', 'e', 'r', 'k', 'q', 's']

#Diccionario para la encriptación
encriptacion = {conjunto1[i]: conjunto2[i] for i in range(len(conjunto1))}

#Pedir una frase al usuario
frase = input("Introduce una frase: ").lower()

frase_encriptada = ""
#Encriptar la frase
for letra in frase:
    if letra in encriptacion:
        frase_encriptada += encriptacion[letra]
    else:
        frase_encriptada += letra

#Mostrar la frase encriptada
print("Frase encriptada:", frase_encriptada)
