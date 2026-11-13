def evaluar_palabra():
    """
    1. Solicita una palabra y evalúa su longitud usando if-elif-else.
    """
    palabra = input("Ingresa una palabra: ")
    longitud = len(palabra)
    
    # Validamos si está entre 4 y 8 letras )
    if 4 <= longitud <= 8:
        print("Palabra correcta")
    elif longitud < 4:
        print("Hacen falta letras (menos de 4)")
    else:  # longitud > 8
        print("La palabra es demasiado larga (más de 8 letras)")


def evaluar_cuadrante():
    """
    2. Recibe dos números y determina el cuadrante en el plano cartesiano
       basándose en si son mayores o menores a cero.
    """
    try:
        x = float(input("Ingresa el valor de X: "))
        y = float(input("Ingresa el valor de Y: "))
    except ValueError:
        print("Por favor, ingresa números válidos.")
        return

    # Determinación del cuadrante
    if x > 0 and y > 0:
        print("El punto se encuentra en el Cuadrante I (+, +)")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el Cuadrante II (-, +)")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el Cuadrante III (-, -)")
    elif x > 0 and y < 0:
        print("El punto se encuentra en el Cuadrante IV (+, -)")
    else:
        print("El punto se encuentra sobre uno de los ejes coordenados (o en el origen).")


# --- Ejecución principal del script ---
if __name__ == "__main__":
    print("--- PRUEBA 1: Validación de Palabra ---")
    evaluar_palabra()
    
    print("\n--- PRUEBA 2: Ubicación en el Plano Cartesiano ---")
    evaluar_cuadrante()