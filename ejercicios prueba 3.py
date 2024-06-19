
trabajadores = []


def registrar_trabajador():
    nombre = input("Ingrese el nombre del trabajador: ")
    apellido = input("Ingrese el apellido del trabajador: ")
    cargo = input("Ingrese el cargo del trabajador (CEO, Desarrollador, Analista de datos): ")
    try:
        sueldo_bruto = float(input("Ingrese el sueldo bruto del trabajador: "))
    except ValueError:
        print("El sueldo bruto debe ser un número.")
        return

        print("Todos los campos son obligatorios.")
        return
    

    desc_salud = sueldo_bruto * 0.07
    desc_afp = sueldo_bruto * 0.12
    sueldo_liquido = sueldo_bruto - desc_salud - desc_afp

    trabajador = {
        "nombre": nombre,
        "apellido": apellido,
        "cargo": cargo,
        "sueldo_bruto": sueldo_bruto,
        "desc_salud": desc_salud,
        "desc_afp": desc_afp,
        "sueldo_liquido": sueldo_liquido
    }
    
   
    trabajadores.append(trabajador)
    print("Trabajador registrado con éxito.")

def listar_trabajadores():
    if not trabajadores:
        print("No hay trabajadores registrados.")
        return
    for trabajador in trabajadores:
        print(f"{trabajador['nombre']} {trabajador['apellido']}, {trabajador['cargo']}, Sueldo Bruto: {trabajador['sueldo_bruto']}, Desc. Salud: {trabajador['desc_salud']}, Desc. AFP: {trabajador['desc_afp']}, Sueldo Líquido: {trabajador['sueldo_liquido']}")

def imprimir_planilla():
    opcion = input("¿Desea imprimir la planilla de todos los trabajadores o por cargo? (todos/cargo): ")
    if opcion == "todos":
        Nombre_Archivo = "planilla_todos.txt"
        with open(Nombre_Archivo, 'w') as archivo:
            for trabajador in trabajadores:
                archivo.write(f"{trabajador['nombre']} {trabajador['apellido']}, {trabajador['cargo']}, Sueldo Bruto: {trabajador['sueldo_bruto']}, Desc. Salud: {trabajador['desc_salud']}, Desc. AFP: {trabajador['desc_afp']}, Sueldo Líquido: {trabajador['sueldo_liquido']}\n")
        print(f"Planilla de todos los trabajadores guardada en {Nombre_Archivo}.")
    elif opcion == "cargo":
        cargo = input("Ingrese el cargo a filtrar (CEO, Desarrollador, Analista de datos): ")
        Nombre_Archivo= f"planilla_{cargo}.txt"
        with open(Nombre_Archivo, 'w') as archivo:
            for trabajador in trabajadores:
                if trabajador['cargo'].lower() == cargo.lower():
                    archivo.write(f"{trabajador['nombre']} {trabajador['apellido']}, {trabajador['cargo']}, Sueldo Bruto: {trabajador['sueldo_bruto']}, Desc. Salud: {trabajador['desc_salud']}, Desc. AFP: {trabajador['desc_afp']}, Sueldo Líquido: {trabajador['sueldo_liquido']}\n")
        print(f"Planilla de trabajadores con cargo {cargo} guardada en {Nombre_Archivo}.")
    else:
        print("Opción no válida.")

def salir():
    print("Saliendo del programa...espere un momento")
    exit()


def menu():
    while True:
        print("*********************************")
        print("---------------------------------")
        print("     Seleccione una Opcion       ")
        print("---------------------------------")
        print("*********************************")
        print("1. Registrar trabajador          ")
        print("2. Listar todos los trabajadores ")
        print("3. Imprimir planilla de sueldos  ")
        print("4. Salir del Programa            ")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_trabajador()
        elif opcion == "2":
            listar_trabajadores()
        elif opcion == "3":
            imprimir_planilla()
        elif opcion == "4":
            salir()
        else:
            print("Opción no válida. Intente nuevamente.")

menu()