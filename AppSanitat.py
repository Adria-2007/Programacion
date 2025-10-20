nombre = ""
edad = 0
peso = 0.0
altura = 0.0
datos_introducidos = False


while True:
    print("\n=== CONTROL SALUD ===")
    print("a) Introducir datos")
    print("b) Modificar datos")
    print("c) Visualizar datos")
    print("d) Salir")
    
    opcion = input("Selecciona una opción: ").lower()
    
    
    if opcion == "a":
        print("\n--- INTRODUCIR DATOS ---")
        
        
        while True:
            nombre = input("Nombre completo: ").strip()
            if nombre == "":
                print("Error: Debes poner un nombre")
            else:
                break
        
        
        while True:
            try:
                edad= input("Edad: ")
                if edad <= 0 or edad > 120:
                    print("Error: Esa no es tu edad")
                else:
                    break
            except:
                print("Error: Formato numérico inválido")
        
        
        while True:
            try:
                peso = float("Peso (kg): ").replace(",", ".")
                if peso <= 0 or peso > 400:
                    print("Error: El peso debe ser razonable")
                else:
                    break
            except:
                print("Error: Formato numérico inválido")
        
        
        while True:
            try:
                altura= float("Altura (m): ").replace(",", ".")
                if altura <= 0.5 or altura >= 2.5:
                    print("Error: La altura debe de humano, ni gremblin ni rascacielos")
                else:
                    break
            except:
                print("Error: Formato numérico inválido")
        
        datos_introducidos = True
        print("Datos guardados correctamente!")
    
    
    elif opcion == "b":
        if not datos_introducidos:
            print("Error: Primero debes introducir datos (opción a)")
            continue
            
        print("\n--- MODIFICAR DATOS ---")
        print("1) Nombre")
        print("2) Edad")
        print("3) Peso")
        print("4) Altura")
        
        try:
            opcion_mod = int(input("¿Qué dato quieres modificar? "))
        except:
            print("Error: Opción inválida")
            continue
        
        if opcion_mod == 1:
            while True:
                nuevo_nombre = input("Nuevo nombre: ").strip()
                if nuevo_nombre == "":
                    print("Error: Debes poner un nombre")
                else:
                    nombre = nuevo_nombre
                    print("Nombre actualizado correctamente!")
                    break
                    
        elif opcion_mod == 2:
            while True:
                try:
                    nueva_edad = int(input("Nueva edad: "))
                    if nueva_edad <= 0 or nueva_edad > 120:
                        print("Error: Esa no es tu edad")
                    else:
                        edad = nueva_edad
                        print("Edad actualizada correctamente!")
                        break
                except:
                    print("Error: Formato numérico inválido")
                    
        elif opcion_mod == 3:
            while True:
                try:
                    nuevo_peso = float(input("Nuevo peso (kg): ").replace(",", "."))
                    if nuevo_peso <= 0 or nuevo_peso > 400:
                        print("Error: El peso debe ser razonable")
                    else:
                        peso = nuevo_peso
                        print("Peso actualizado correctamente!")
                        break
                except:
                    print("Error: Formato numérico inválido")
                    
        elif opcion_mod == 4:
            while True:
                try:
                    nueva_altura = float(input("Nueva altura (m): ").replace(",", "."))
                    if nueva_altura <= 0.5 or nueva_altura >= 2.5:
                        print("Error: La altura debe de humano, ni gremblin ni rascacielos")
                    else:
                        altura = nueva_altura
                        print("Altura actualizada correctamente!")
                        break
                except:
                    print("Error: Formato numérico inválido")
        else:
            print("Error: Opción inválida")
    
    
    elif opcion == "c":
        if not datos_introducidos:
            print("Error: Primero debes introducir datos (opción a)")
            continue
            
        print("\n--- VISUALIZAR DATOS ---")
        
        
        nombre_normalizado = ""
        partes_nombre = nombre.split()
        for parte in partes_nombre:
            if parte != "":
                if nombre_normalizado != "":
                    nombre_normalizado += " "
                nombre_normalizado += parte.capitalize()
        
        
        imc = peso / (altura * altura)
        
        
        if imc < 18.5:
            categoria_imc = "peso bajo"
        elif imc < 25:
            categoria_imc = "peso normal"
        elif imc < 30:
            categoria_imc = "sobrepeso"
        else:
            categoria_imc = "obesidad"
        

        fc_max = 220 - edad
        fc_50 = int(fc_max * 0.5)
        fc_85 = int(fc_max * 0.85)
        

        agua_ml = 35 * peso
        agua_litros = agua_ml / 1000
        

        from datetime import datetime
        año_actual = datetime.now().year
        año_nacimiento = año_actual - edad
        

        print(f"Hola, {nombre_normalizado}!")
        print(f"Edad: {edad} años | Pes: {peso:.2f} kg | Altura: {altura:.2f} m")
        print(f"IMC: {imc:.2f} ({categoria_imc})")
        print(f"FC máxima estimada: {fc_max} bpm")
        print(f"Zona FC objetivo: {fc_50}—{fc_85} bpm")
        print(f"Agua recomendada: {agua_litros:.2f} L/dia")
        print(f"Año de nacimiento aproximado: {año_nacimiento}")
    
    
    elif opcion == "d":
        print("¡Hasta pronto!")
        break
    

    else:
        print("Error: Opción no válida. Selecciona a, b, c o d")