
import random
import time


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
    autorizado = random.choice([True, False])
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
    estado_casa["nivel_co2"] = random.randint(100, 1000)
    print(f"Nivel de CO₂ actual: {estado_casa['nivel_co2']} ppm")

    if estado_casa["nivel_co2"] > 700:
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
    estado_casa["aspersor"] = "encendido"
    print("Aspersor activado.")

def desactivar_aspersor():
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

def main_menu():
    while True:
        print("""
======== MENÚ PRINCIPAL ========
1. Abrir puerta con Face ID
2. Detectar nivel de CO₂
3. Activar aspersor
4. Desactivar aspersor
5. Ver estado de la casa
6. Salir
================================
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

if __name__ == "__main__":
    main_menu()
