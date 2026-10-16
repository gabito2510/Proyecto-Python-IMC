# Solicitar una palabra al usuario
palabra = input("Por favor, ingresa una palabra: ")

# Calcular la longitud de la palabra
longitud = len(palabra)

# Evaluar mediante if - elif - else
if 4 <= longitud <= 8:
    print(f"La palabra '{palabra}' tiene {longitud} letras. Cumple con la condición (entre 4 y 8 letras).")
elif longitud < 4:
    print(f"La palabra '{palabra}' tiene {longitud} letras. Es demasiado corta (menos de 4 letras).")
else:
    print(f"La palabra '{palabra}' tiene {longitud} letras. Es demasiado larga (más de 8 letras).")
    
# Definición de las variables (puedes cambiar estos valores para probar)

x = 5
y = -3


# Estructura condicional para determinar el cuadrante
if x > 0 and y > 0:
    print("El punto está en el Cuadrante I")
elif x < 0 and y > 0:
    print("El punto está en el Cuadrante II")
elif x < 0 and y < 0:
    print("El punto está en el Cuadrante III")
elif x > 0 and y < 0:
    print("El punto está en el Cuadrante IV")
else:
    print("El punto se encuentra sobre uno de los ejes (o en el origen)")


def verificar_palabra(intento, palabra_secreta):
    # Convertimos ambas a minúsculas para evitar problemas con mayúsculas
    intento = intento.lower()
    palabra_secreta = palabra_secreta.lower()
    
    if intento == palabra_secreta:
        print("Palabra correcta")
    elif len(intento) < len(palabra_secreta):
        print("Hacen falta letras")
    elif len(intento) > len(palabra_secreta):
        print("Sobran letras")
    else:
        print("Palabra incorrecta (misma longitud pero letras diferentes)")

# --- Ejemplo de uso ---
PALABRA_CORRECTA = "python"

# Prueba 1: Correcta
verificar_palabra("python", PALABRA_CORRECTA)  # Imprime: Palabra correcta

# Prueba 2: Faltan letras
verificar_palabra("pyt", PALABRA_CORRECTA)     # Imprime: Hacen falta letras

# Prueba 3: Sobran letras
verificar_palabra("pythons", PALABRA_CORRECTA) # Imprime: Sobran letras

# Prueba 4: Incorrecta (misma longitud)
verificar_palabra("cython", PALABRA_CORRECTA) # Imprime: Palabra incorrecta (...)
