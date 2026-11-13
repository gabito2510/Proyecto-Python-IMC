print("--- Programa de Cuadrantes ---")

# Validación para la coordenada X
x = 0
while x == 0:
    x = float(input("Ingresa la coordenada X (diferente de 0): "))
    if x == 0:
        print("¡Error! La coordenada X no puede ser 0. Inténtalo de nuevo.")

# Validación para la coordenada Y
y = 0
while y == 0:
    y = float(input("Ingresa la coordenada Y (diferente de 0): "))
    if y == 0:
        print("¡Error! La coordenada Y no puede ser 0. Inténtalo de nuevo.")

print(f"\nCoordenadas aceptadas: X = {x}, Y = {y}")

# Opcional: Determinar el cuadrante
if x > 0 and y > 0:
    print("El punto se encuentra en el Primer Cuadrante.")
elif x < 0 and y > 0:
    print("El punto se encuentra en el Segundo Cuadrante.")
elif x < 0 and y < 0:
    print("El punto se encuentra en el Tercer Cuadrante.")
else:
    print("El punto se encuentra en el Cuarto Cuadrante.")

print("--- Programa de Longitud / Validación de Palabra ---")

palabra_secreta = "programacion"
palabra_usuario = ""

# El ciclo se repite mientras la palabra ingresada sea diferente a la correcta
while palabra_usuario != palabra_secreta:
    palabra_usuario = input("Ingresa la palabra correcta: ").lower()
    
    if palabra_usuario != palabra_secreta:
        print("¡Incorrecto! Intenta ingresar una palabra nueva.")

print(f"\n¡Felicitaciones! Adivinaste la palabra correcta: '{palabra_secreta}'")    