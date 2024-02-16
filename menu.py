import json
import Datas.Modulos.modulo_usuarios as FCRUD

def main():
    print("Bienvenido usuario, ¿Que deseas hacer el día de hoy? ")
    print("1. acceder al modulo de usuarios ")
    print("2. acceder al modulo de gestion de servivios ")
    print("3. acceder al modulo de reportes ")
    print("4. acceder al modulo de bonificaciones ")
    print("5. salir ")

def menu_usuarios():
    print("Menú de usuarios ")
    print("1. registrar cliente nuevo ")
    print("2. ver informacion de un cliente ")
    print("3. actualizar informacion de un cliente ")
    print("4. eliminar cliente ya existente ")
    print("5. Registro de servicios utilizados por un cliente  ")
    print("6. seguimiento de las interacciones de los clientes ")
    print("7. mostrar los clientes más leales ")
    print("8. atrás ")

with open("Datas/Clientes.json", "r") as outfile:
        data = json.load(outfile)
while True:
    main()
    opcion = input("selecciona una opcion: ")
    if opcion == '1':    
        while True:
            menu_usuarios()
            opcion = input("selecciona una opcion: ")
            if opcion == '1':
                print("zi")
                FCRUD.registrar_usuario()
            elif opcion == '2':
                FCRUD.mostrar_info_cliente()   
            elif opcion == '3':
                FCRUD.actualizar_cliente() 
            elif opcion == '4':
                FCRUD.eliminar_cliente()  
            elif opcion == '5':
                FCRUD.Registrar_servicio()    
            elif opcion == '8':
                break    
    elif opcion == '5':
        print("Hasta luego")
        break
               