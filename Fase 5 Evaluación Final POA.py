# Problema 1: Clasificación de compromiso de sesiones
# Autor:JOHAN PRADA
# Programa: fundamentso de programacion
# Descripción: Evalúa el nivel de compromiso de clientes según duración y clics

# -------------------------------
# Función para clasificar compromiso
# Recibe: duración (segundos) y número de clics
# Devuelve: "Alto", "Medio" o "Bajo" según las reglas
def clasificar_sesion(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"   # Sesión larga y con muchos clics
    elif duracion < 60 or clics < 3:
        return "Bajo"   # Sesión muy corta o con pocos clics
    else:
        return "Medio"  # Caso intermedio

# -------------------------------
# Datos iniciales: matriz con 5 sesiones
# Cada fila tiene: [ID Cliente, Duración, Clics]
sesiones = [
    [101, 200, 10],   # Cliente con sesión larga y muchos clics
    [102, 45, 2],     # Cliente con sesión corta y pocos clics
    [103, 120, 5],    # Cliente con sesión intermedia
    [104, 300, 12],   # Cliente con sesión muy larga y muchos clics
    [105, 80, 1]      # Cliente con pocos clics
]

# -------------------------------
# Generar informe en consola
print("Informe de Clasificación de Compromiso")
print("--------------------------------------")

# Recorremos cada fila de la matriz con un ciclo for
for sesion in sesiones:
    id_cliente = sesion[0]   # Primer elemento: ID
    duracion = sesion[1]     # Segundo elemento: duración
    clics = sesion[2]        # Tercer elemento: clics
    clasificacion = clasificar_sesion(duracion, clics)  # Llamamos la función
    print(f"Cliente {id_cliente}: {clasificacion}")     # Mostramos resultado
