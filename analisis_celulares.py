import pandas as pd

# Dataset simulado
data = {
    "Estudiante": ["Ana", "Luis", "Marta", "Carlos", "Lucía"],
    "Horas_Diarias": [5, 8, 3, 6, 4],
    "Red_Social_Favorita": ["Instagram", "TikTok", "Twitter", "Facebook", "Instagram"],
    "Rendimiento_Académico": ["Alto", "Bajo", "Medio", "Alto", "Medio"]
}

df = pd.DataFrame(data)

# 1. Agregación: Promedio y desviación estándar de horas
promedio = df['Horas_Diarias'].mean()
desviacion = df['Horas_Diarias'].std()
print("Promedio de horas diarias:", promedio)
print("Desviación estándar:", desviacion)

# 2. Filtrado: Estudiantes con rendimiento "Alto" y menos de 5 horas
filtro = df[(df['Rendimiento_Académico'] == 'Alto') & (df['Horas_Diarias'] < 5)]
print("\nEstudiantes con rendimiento 'Alto' y <5 horas:")
print(filtro)

# 3. Conteo: Preferencias de redes sociales
conteo_redes = df['Red_Social_Favorita'].value_counts()
print("\nPreferencias de redes sociales:")
print(conteo_redes)

# 4. Nueva columna: Clasificación del uso
def clasificar_uso(horas):
    if horas > 5:
        return "Excesivo"
    elif 3 <= horas <= 5:
        return "Moderado"
    else:
        return "Bajo"

df['Uso_Celular'] = df['Horas_Diarias'].apply(clasificar_uso)
print("\nDataFrame final con clasificación de uso:")
print(df)
