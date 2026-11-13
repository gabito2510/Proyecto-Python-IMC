
# 1. LISTA para almacenar las palabras ingresadas por el usuario

palabras_intentadas = []

# 2. TUPLA para definir los nombres de los cuadrantes
# Utilizamos una tupla (()), ya que los nombres de los cuadrantes son datos fijos 
# o constantes que no deben cambiar durante la ejecución del programa. 
# Esto nos aporta seguridad y nos permite acceder a ellos de manera eficiente 
# mediante sus índices (por ejemplo, cuadrantes[0] para "Cuadrante I").
cuadrantes = ("Cuadrante I", "Cuadrante II", "Cuadrante III", "Cuadrante IV")

# 3. USO INTERACTIVO BÁSICO

print("--- BIENVENIDO AL JUEGO / RETO ---")

# Simulamos la interacción de ingreso de palabras por el usuario
while True:
    palabra_usuario = input("Ingresa una palabra (o escribe 'salir' para terminar): ").strip()
    
    if palabra_usuario.lower() == 'salir':
        break
        
    # Guardamos cada intento en nuestra lista
    palabras_intentadas.append(palabra_usuario)
    
    # Ejemplo de uso de la tupla mediante índices (por ejemplo, asignando el primer cuadrante)
    print(f"Has ingresado la palabra '{palabra_usuario}' asignada al: {cuadrantes[0]}")

# Mostramos el registro final almacenado en la lista
print("\n--- RESUMEN DE SESIÓN ---")
print(f"Total de palabras intentadas: {len(palabras_intentadas)}")
print(f"Lista completa de palabras: {palabras_intentadas}")