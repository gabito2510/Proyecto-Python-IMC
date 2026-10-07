
# 1. Captura de datos desde el teclado y 2. Conversión de tipos (Casting)
nombre_completo = input("Introduce tu nombre completo: ")
nombre_formateado = nombre_completo.title()
edad = int(input("Introduce tu edad (años): "))
peso = float(input("Introduce tu peso (kg): "))
estatura = float(input("Introduce tu estatura (metros): "))


# 3. Aplicación de la fórmula del IMC
imc = peso / (estatura ** 2)

# Mostrar los resultados en pantalla
#print(f"\nHola {nombre_completo}, tienes {edad} años.")
#print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")
# Mostrar resumen con formato del nombre 
resumen = f"\nNombre Completo: {nombre_formateado} | Edad: {edad} años | Peso: {peso} | Estatura: {estatura}"
#mostrar resumen 
print(resumen)