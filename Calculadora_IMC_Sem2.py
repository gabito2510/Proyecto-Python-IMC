


# 1. Captura de datos desde el teclado y 2. Conversión de tipos (Casting)
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad (años): "))
peso = float(input("Introduce tu peso (kg): "))
estatura = float(input("Introduce tu estatura (metros): "))

# 3. Aplicación de la fórmula del IMC
imc = peso / (estatura ** 2)

# Mostrar los resultados en pantalla
print(f"\nHola {nombre}, tienes {edad} años.")
print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")

