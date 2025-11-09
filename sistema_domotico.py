import random
import time
from datetime import datetime, timedelta


estado_casa = {
    "puerta": "cerrada",
    "face_id_autorizado": False,
    "nivel_co2": 0,
    "alarma": "desactivada",
    "aspersor": "apagado",
    "extintor": "apagado"
}

def face_id():
    print("\n--- SISTEMA FACE ID ---")

respuesta = input("¿El rostro está autorizado? (si/no): ").strip().lower()

autorizado = respuesta == "si"

if autorizado:
    estado_casa["face_id_autorizado"] = True
    estado_casa["puerta"] = "abierta"
    print("Rostro reconocido. Puerta abierta.")
else:
    estado_casa["face_id_autorizado"] = False
    estado_casa["puerta"] = "cerrada"
    print("Rostro no reconocido. Puerta cerrada.")

def detectar_co2():
    print("\n--- DETECCIÓN DE CO₂ ---")

    try:
        co2 = int(input("¿A partir de qué nivel de CO₂ (ppm) deseas que se active la alarma?: "))
    except ValueError:
        print("Entrada no válida. Se usará el valor por defecto de 700 ppm.")
        co2 = 700

    estado_casa["nivel_co2"] = random.randint(100, 1000)
    print(f"Nivel de CO₂ actual: {estado_casa["nivel_co2"]} ppm")

    if estado_casa["nivel_co2"] > co2:
        activar_alarma()
    else:
        if estado_casa["alarma"] == "activada":
            desactivar_alarma()
        print("Nivel de CO₂ dentro del rango normal.")


def activar_alarma():
    if estado_casa["alarma"] == "desactivada":
        estado_casa["alarma"] = "activada"
        print("Alarma activada por alto nivel de CO₂.")
        activar_extintor()

def desactivar_alarma():
    estado_casa["alarma"] = "desactivada"
    estado_casa["extintor"] = "apagado"
    print("Alarma desactivada. Extintor apagado.")

def activar_aspersor():
    if estado_casa["aspersor"] == "apagado":
        estado_casa["aspersor"] = "encendido"
        print("Aspersor activado.")

def desactivar_aspersor():
    if estado_casa["aspersor"] == "encendido":
        estado_casa["aspersor"] = "apagado"
        print("Aspersor desactivado.")

def activar_extintor():
    estado_casa["extintor"] = "activado"
    print("Extintor activado automáticamente por alarma.")

def estado_general():
    print("\n--- ESTADO DE LA CASA ---")
    for k, v in estado_casa.items():
        print(f"{k.capitalize()}: {v}")
    print("----------------------------")


def modo_manual():
    """Modo de operación manual (código original)."""
    while True:
        print("""
======== MENÚ PRINCIPAL (MANUAL) ========
1. Abrir puerta con Face ID
2. Detectar nivel de CO₂
3. Activar aspersor
4. Desactivar aspersor
5. Ver estado de la casa
6. Salir
========================================
""")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            face_id()
        elif opcion == "2":
            detectar_co2()
        elif opcion == "3":
            activar_aspersor()
        elif opcion == "4":
            desactivar_aspersor()
        elif opcion == "5":
            estado_general()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
        time.sleep(1.5)

def modo_simulacion_automatica():
    """Modo de simulación automática con reloj y aspersor programado."""
    print("\n--- MODO SIMULACIÓN AUTOMÁTICA ---")
    
    
intervalo_horas = None

while intervalo_horas is None:
    try:
        valor = float(input("Introduce el intervalo de activación del aspersor en horas (ej: 6 para cada 6 horas): "))
        if valor <= 0:
            print("El intervalo debe ser un número positivo.")
        else:
            intervalo_horas = valor
    except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")

    intervalo_segundos = intervalo_horas * 3600
    
    
    tiempo_simulacion = datetime.now().replace(microsecond=0)
    proxima_activacion = tiempo_simulacion + timedelta(seconds=intervalo_segundos)
    
    print(f"Simulación iniciada a las: {tiempo_simulacion.strftime('%H:%M:%S')}")
    print(f"El aspersor se activará cada {intervalo_horas} horas.")
    print(f"Próxima activación programada para: {proxima_activacion.strftime('%H:%M:%S')}")
    
    
    while True:
        
        print("\n" + "="*40)
        print(f"RELOJ DE SIMULACIÓN: {tiempo_simulacion.strftime('%Y-%m-%d %H:%M:%S')}")
        estado_general()
        
        
        if tiempo_simulacion >= proxima_activacion:
            print("\n*** EVENTO PROGRAMADO: HORA DE RIEGO ***")
            activar_aspersor()
            
            time.sleep(5)
            desactivar_aspersor()
            
            
            proxima_activacion += timedelta(seconds=intervalo_segundos)
            print(f"Próxima activación reprogramada para: {proxima_activacion.strftime('%H:%M:%S')}")
        
       
        if random.random() < 0.2:
            detectar_co2()
            
        avance_simulacion_segundos = 3600
        tiempo_simulacion += timedelta(seconds=avance_simulacion_segundos)
        
        print(f"\n[Avanzando {avance_simulacion_segundos} segundos en la simulación...]")
        time.sleep(1) 


def menu_inicial():
    """Menú inicial para seleccionar el modo de operación."""
    while True:
        print("""
========================================
    SISTEMA DOMÓTICO - MENÚ INICIAL
========================================
1. Modo Manual (Interactivo)
2. Modo Simulación Automática (Reloj)
3. Salir
========================================
""")
        opcion = input("Selecciona el modo de operación: ")

        if opcion == "1":
            modo_manual()
        elif opcion == "2":
            modo_simulacion_automatica()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
        

        if opcion in ["1", "2"]:
            print("\nVolviendo al menú inicial...")
            time.sleep(2)

if __name__ == "__main__":
    menu_inicial()
