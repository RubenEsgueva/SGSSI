frecuencias="eaolsndruitcpmyqbhgfvjñzxkw"
frecuencias=frecuencias.upper()
texto_cifrado="" #Aqui se pone el texto que se quiera descodificar.
#texto_cifrado = texto_cifrado.upper() # Como todas las letras en principio se cambiaran a la misma independientemente de si estan en mayusculas o minusculas usaremos esta linea si es necesario.

print(texto_cifrado + "\n")

letras = {}

for letra in frecuencias:
    letras[letra] = 0

for letra in texto_cifrado: #recogemos cuantas veces aparece cada caracter en el texto cifrado
    if letra in letras:
        letras[letra] += 1

def get_value(elem): #Devolver valor de una clave
    return elem[1]

def get_keys(elem): #Devolver un array de las claves, por ser un array de tuplas
    array = []
    for item in elem:
        array.append(item[0])
    return array

letras_ordenadas = get_keys(sorted(letras.items(), key=get_value, reverse=True)) #ordenamos las letras en funcion de cuantas veces aparecen en el texto

texto_descifrado = texto_cifrado
cont = 0
for letra in texto_cifrado: #sustituimos las letras en el texto cifrado por su correspondiente estimada en funcion de la cantidad de veces que aparece
    if letra in frecuencias:
        texto_descifrado = texto_descifrado[:cont] + frecuencias[letras_ordenadas.index(letra)] + texto_descifrado[cont+1:]
    cont += 1

#print(texto_descifrado)

lista_cambios = { #En el examen rehacer esta lista después de la primera aproximación del descifrado deduciendo que letras pueden ser cuales
    # Formato a seguir --> "LETRA A CAMBIAR": "letra correspondiente"
}

for letra in lista_cambios:
    texto_descifrado = texto_descifrado.replace(letra, lista_cambios[letra]) #substituimos las letras del texto cifrado por su correspondiente

relaciones = {}
cont=0
for letra in texto_descifrado:
    relaciones[letra]=texto_cifrado[cont]
    cont+=1
print(texto_descifrado + "\n")
relaciones = sorted(relaciones.items())
print("Relaciones: Cifrado --> Descifrado")
print("----------------------------------")
for relacion in relaciones:
    print("            " + relacion[1] + " --> " + relacion[0])
