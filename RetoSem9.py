import random

def simular_canica(niveles: int = 12) -> int:
    """
    Simula el recorrido de una canica a través de niveles de obstáculos 
    donde en cada nivel puede ir hacia la izquierda o hacia la derecha.

    Parámetros:
    ----------
    niveles : int, opcional
        El número de niveles u obstáculos por los que pasará la canica 
        (por defecto es 12).

    Retorna:
    -------
    int
        Un valor entero que representa el contenedor final donde cae la canica, 
        calculado como la suma total de movimientos a la derecha.
    """
    contenedor = 0
    
    # Se repite el proceso tantas veces como niveles se indiquen
    for _ in range(niveles):
        # Generamos un valor aleatorio: 0 para izquierda, 1 para derecha
        movimiento = random.randint(0, 1)
        contenedor += movimiento
        
    return contenedor

# Ejemplo de uso de la funcion :
resultado_final = simular_canica()
print(f"La canica cayó en el contenedor final: {resultado_final}")