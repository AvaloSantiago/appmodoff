import os
import random

# 1. Desafíos aleatorios
actividades = ["Leer", "Caminar", "Meditar"]
actividad_aleatoria = random.choice(actividades)
print(f"Actividad aleatoria para desconectar: {actividad_aleatoria}")

# 2. Puntos por actividad
puntos = {"Leer": 10, "Caminar": 15, "Meditar": 20}
actividad_usuario = input("Ingresa la actividad que realizaste (Leer, Caminar, Meditar): ")

if actividad_usuario in puntos:
    print(f"¡Ganaste {puntos[actividad_usuario]} puntos por {actividad_usuario}!")
else:
    print("Actividad no reconocida. Intenta con Leer, Caminar o Meditar.")

# 3. Meta diaria
def verificar_meta(minutos):
    if minutos >= 30:
        print("🎉 Logro desbloqueado: ¡30+ minutos sin conexión!")
    else:
        print("Sigue intentando, ¡ya casi logras la meta!")

# Prueba la función con input del usuario
try:
    minutos_off = int(input("¿Cuántos minutos estuviste desconectado hoy?: "))
    verificar_meta(minutos_off)
except ValueError:
    print("Por favor, ingresa un número válido de minutos.")
