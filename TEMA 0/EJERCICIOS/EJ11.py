#Crear una función que devuelva un tipo booleano que indique si el carácter que se pasa como parámetro de entrada corresponde con una vocal.

def es_vocal(caracter):
    vocales = "aeiouAEIOU"
    return caracter in vocales