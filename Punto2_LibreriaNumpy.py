import numpy as np

Estudiantes = 6500


Codigos = np.arange(220000, 220000 + Estudiantes)  # arange(inicio, fin, paso) permite sumarle 1 en cada posicion
Nombres = np.array([f"Estudiante_{i}" for i in range(Estudiantes)])  # np.array() crear arrays a partir de listas
Promedios = np.random.uniform(2.0, 5.0, Estudiantes).round(2)  # Promedios entre 2.0 y 5.0 el .round(2) me permite redondear a 2 decimales
                                                                #Me genera números aleatorios con decimales
CodigosCarreras = np.random.randint(1, 11, Estudiantes)  # Me genera números aletorios enteros y se los asigna a cada posicion (estudiante)
AñoIngreso = np.random.randint(1980, 2024, Estudiantes)  # Me genera números aletorios enteros y se los asigna a cada posicion (estudiante)

# Entrada del usuario
IngresoCodigoCarrera = int(input("""Ingrese el código de la carrera a listar:
1. ING. SISTEMAS
2. ING. CIVIL
3. ING. ELECTRICA
4. ING. ELECTRONICA
5. ING. MECANICA
6. ING. INDUSTRIAL
7. ING. PETROLEOS
8. ING. QUIMICA
9. ING. METALURGICA
10. ING. BIOMEDICA
11. ING. CIENCIAS DE DATOS
Ingrese el número correspondiente: """))

# Filtrar estudiantes de la carrera seleccionada con promedio mayor o igual a 4.0
EstudiCarrera = CodigosCarreras == IngresoCodigoCarrera
EstudiExcelente = Promedios >= 4.0
filtro1 = EstudiCarrera & EstudiExcelente  # Estudiantes que cumplen ambas condiciones

Anterior1990 = AñoIngreso == 1990
Condicionales = (Promedios > 2.7) & (Promedios < 3.2)
filtro2 = Anterior1990 & Condicionales

# filtro1
CodigosBusqueda1 = Codigos[filtro1]
NombresBusqueda1 = Nombres[filtro1]

# filtro2
CodigosBusqueda2 = Codigos[filtro2]
NombresBusqueda2 = Nombres[filtro2]

# Imprimir resultados
print(f"\nEstudiantes con promedio acumulado mayor o igual 4.0 en la carrera {IngresoCodigoCarrera}:")
for codigo, nombre in zip(CodigosBusqueda1, NombresBusqueda1):
    print(f"Código: {codigo} --- Nombre: {nombre}")

# Total de estudiantes encontrados
print(f"\nTotal de estudiantes encontrados: {len(CodigosBusqueda1)}")

print(f"\nEstudiantes que ingresaron antes de 1990 y están condicionales")
for codigo, nombre in zip(CodigosBusqueda2, NombresBusqueda2):
    print(f"Código: {codigo} --- Nombre: {nombre}")

#JOHAN FRANCISCO LÓPEZ JAIMES