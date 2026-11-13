def validar_acceso():
    # Colección de datos (Lista de diccionarios que simulan usuarios registrados con credenciales y datos de ubicación)
    # Usamos string, int y float para demostrar el casting y manejo de tipos
    usuarios_registrados = [
        {"usuario": "admin", "pin": 1234, "lat": 20.9674, "lon": -89.5926, "rol": "Administrador"},
        {"usuario": "maria", "pin": 5678, "lat": 19.4326, "lon": -99.1332, "rol": "Operador"},
        {"usuario": "carlos", "pin": 9876, "lat": 40.7128, "lon": -74.0060, "rol": "Invitado"}
    ]
    
    intentos = 3
    
    print("=== SISTEMA DE VALIDACIÓN DE ACCESO ===")
    
    while intentos > 0:
        # Entrada de datos (Casting implícito a string, pero manejado explícitamente según se requiera)
        input_usuario = input("Ingrese su nombre de usuario: ").strip().lower()
        
        # Validación y casting de PIN a entero (int) para evitar errores de tipo
        try:
            input_pin = int(input("Ingrese su PIN de acceso (4 dígitos): "))
        except ValueError:
            print("Error: El PIN debe contener únicamente números.")
            intentos -= 1
            print(f"Te quedan {intentos} intentos.\n")
            continue
            
        # Estructuras de control para buscar al usuario en la colección (lista)
        usuario_encontrado = None
        for u in usuarios_registrados:
            if u["usuario"] == input_usuario and u["pin"] == input_pin:
                usuario_encontrado = u
                break
                
        # Condicionales para otorgar o negar el acceso
        if usuario_encontrado:
            print(f"\n¡Acceso concedido! Bienvenido, {usuario_encontrado['usuario'].capitalize()} ({usuario_encontrado['rol']}).")
            
            # Demostración del uso de coordenadas flotantes (float) y enteros (int)
            lat_str = str(usuario_encontrado["lat"])
            lon_str = str(usuario_encontrado["lon"])
            
            print(f"Coordenadas registradas (como string): Lat {lat_str}, Lon {lon_str}")
            print(f"Coordenadas transformadas a float exacto -> Lat: {float(lat_str):.4f}, Lon: {float(lon_str):.4f}")
            
            # Ejemplo de longitud del nombre de usuario usando casting y función de longitud
            longitud_nombre = len(str(usuario_encontrado["usuario"]))
            print(f"La longitud de su nombre de usuario es de {longitud_nombre} caracteres.")
            return True
        else:
            intentos -= 1
            print(f"Credenciales incorrectas. Te quedan {intentos} intentos.\n")
            
    print("Acceso bloqueado por demasiados intentos fallidos.")
    return False

# Ejecución del programa
if __name__ == "__main__":
    validar_acceso()