import datetime

import os
os.system("cls")

ubicaciones = ["Platinum"] * 20 + ["Gold"] * 30 + ["Silver"] * 50
precios = {"Platinum": 120000, "Gold": 80000, "Silver": 50000}
asistentes = []



def menuprincipal():
    print("""
        
        ##### MENU #####
    
    1. Comprar entradas
    2. Mostrar ubicaciones disponibles
    3. Ver listado de asistentes
    4. Mostrar ganancias totales
    5. Salir
    
    """)


def comprar_entradas():
    cantidad = int(input("Ingrese la cantidad de entradas a comprar (1-3): "))
    if cantidad < 1 or cantidad > 3:
        
        print("La cantidad de entradas debe ser entre 1 y 3.")
        return
    disponibles = [i+1 for i, ubicacion in enumerate(ubicaciones) if ubicacion != "Vendida"]
    if not disponibles:
        print("No quedan entradas disponibles.")
        return

    print("Ubicaciones disponibles:")
    for ubicacion in disponibles:
        print(f"{ubicacion}. {ubicaciones[ubicacion-1]}")

    for i in range(cantidad):
        ubicacion = 0
        while ubicacion not in disponibles:
            ubicacion = int(input("Seleccione una ubicación disponible: "))
            if ubicacion not in disponibles:
                print("La ubicación seleccionada no está disponible.")

        run = input("Ingrese el RUN del asistente (sin guiones ni puntos): ")
        asistentes.append((run, ubicacion))
        ubicaciones[ubicacion-1] = "Vendida X"

    print("Operación realizada correctamente.")


def mostrar_ubicaciones_disponibles():
    for i, ubicacion in enumerate(ubicaciones):
        print(f"{i+1}. {ubicacion}")


def mostrar_listado_asistentes():
    if not asistentes:
        print("No hay asistentes registrados.")
        return

    asistentes_ordenados = sorted(asistentes, key=lambda x: x[0])
    print("Listado de asistentes:")
    for asistente in asistentes_ordenados:
        print("+------------------------------+")
        print(f"|RUN: {asistente[0]} | Ubicación: {asistente[1]}|")
        


def mostrar_ganancias_totales():
    total = sum(precios[ubicacion] for _, ubicacion in asistentes)
    print("Tipo Entrada\tCantidad\tTotal")
    for ubicacion, cantidad in precios.items():
        cantidad_entradas = sum(1 for _, u in asistentes if u == ubicacion)
        if cantidad_entradas > 0:
            print(f"{ubicacion}\t\t{cantidad_entradas}\t\t${cantidad_entradas * cantidad:,}")
    print(f"TOTAL\t\t{len(asistentes)}\t\t${total:,}")


def salir_sistema():
    fechahora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"¡Hasta luego, nos vemos! {fechahora}")


def principal():
    while True:
        menuprincipal()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            comprar_entradas()
        elif opcion == "2":
            mostrar_ubicaciones_disponibles()
        elif opcion == "3":
            mostrar_listado_asistentes()
        elif opcion == "4":
            mostrar_ganancias_totales()
        elif opcion == "5":
            salir_sistema()
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    principal()

#prueba d funcion main non borrarlo despue