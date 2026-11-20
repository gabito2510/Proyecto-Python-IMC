import random
import matplotlib.pyplot as plt


def simular_pasos(num_bolas=1000, num_niveles=10):
    """
    Simula la caída de varias bolas a través de niveles con decisiones
    aleatorias ('izquierda' o 'derecha') y devuelve la posición final
    (cantidad de pasos a la derecha) de cada bola.
    """
    resultados = []

    for _ in range(num_bolas):
        posicion_derecha = 0
        for _ in range(num_niveles):
            decision = random.choice(["izquierda", "derecha"])
            if decision == "derecha":
                posicion_derecha += 1
        resultados.append(posicion_derecha)

    return resultados


def graficar_resultados(datos):
    """
    Recibe una lista de datos numéricos y genera un histograma.
    """
    plt.figure(figsize=(8, 5))
    plt.hist(datos, bins=range(min(datos), max(datos) + 2), align="left", rwidth=0.8)
    plt.title("Histograma de resultados de la simulación")
    plt.xlabel("Cantidad de pasos a la derecha")
    plt.ylabel("Frecuencia (número de bolas)")
    plt.xticks(range(min(datos), max(datos) + 1))
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    datos_simulacion = simular_pasos(num_bolas=1000, num_niveles=10)
    graficar_resultados(datos_simulacion)