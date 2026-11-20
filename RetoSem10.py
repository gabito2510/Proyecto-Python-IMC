import random

def simular_canica(num_niveles=10):
    """
    Simula el recorrido de una canica a través de un tablero.
    utilizando lógica de pasos aleatorios.
    
    Cada nivel representa una bifurcación donde la canica puede ir a la izquierda (0) 
    o a la derecha (1). El contenedor final corresponde a la suma total de movimientos a la derecha.
    """
    posicion = 0  # Iniciamos en el centro/borde izquierdo según se numere
    for _ in range(num_niveles):
        # Cada paso aleatorio es una decisión binaria: 0 (izquierda) o 1 (derecha)
        paso = random.choice([0, 1])
        posicion += paso
    return posicion

def ejecutar_simulacion_total(num_repeticiones=3000, num_niveles=10):
    """
    1. Función principal que llama a simular_canica dentro de un bucle de 3,000 repeticiones.
    2. Almacena el contenedor final de cada canica en una lista.
    
    """
    contenedores_finales = []
    
    for _ in range(num_repeticiones):
        contenedor = simular_canica(num_niveles)
        contenedores_finales.append(contenedor)
        
    return contenedores_finales

# Bloque principal de ejecución
if __name__ == "__main__":
    # Configuración de la simulación para 3,000 canicas y 10 niveles de caída
    TOTAL_REPETICIONES = 3000
    NIVELES = 10
    
    resultados = ejecutar_simulacion_total(TOTAL_REPETICIONES, NIVELES)
    
    print(f"Se simularon exitosamente {len(resultados)} canicas.")
    print(f"Primeros 10 contenedores finales de ejemplo: {resultados[:10]}")