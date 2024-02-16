import json

def ingresar_numero(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            return valor
        else:
            print("Ingresa un valor valido ")


def registrar_usuario():
    with open("Datas/Clientes.json", "r") as outfile:
        data = json.load(outfile)

    clientes = data["Clientes"] 

    nuevo_cliente = {}
    while True:    
        try:
            nuevo_id = max([cliente["ID"]for cliente in clientes], default = 0) + 1
            nuevo_cliente["ID"] = nuevo_id
            nuevo_cliente["N_documento"] = ingresar_numero("Ingrese el numero de documento del nuevo cliente: ")
            nuevo_cliente["Nombre"] = input("Ingrese el nombre del nuevo cliente: ")
            nuevo_cliente["Apellido"] = input("Ingrese el apellido del nuevo cliente: ")
            nuevo_cliente["N_celular"] = ingresar_numero("Ingrese el numero de celular: ")
            nuevo_cliente["Direccion"] = input("Ingrese la direccion del nuevo cliente: ")
            nuevo_cliente["categoria"] = input("Ingrese la categoria del nuevo cliente: ")
            nuevo_cliente["Contacto_Soporte"] = ""
            nuevo_cliente["Servicios"] = input[ 
                                        "Sercicio": "Fibra Optica",
                                        "Sercicio": "Plan pospago",
                                        "Sercicio": "Internet Hogar",
                                        "Sercicio": "Plan prepago"
                                               ]
            clientes.append(nuevo_cliente)
            break

        except ValueError:
            print("Ingresa un valor numerico")    
    
    

    with open("Datas/Clientes.json", "w") as outfile:
        json.dump(data, outfile, indent = 4)

def mostrar_info_cliente():
    with open("Datas/Clientes.json", "r") as outfile:
        data = json.load(outfile)
    clientes = data["Clientes"]    
    while True:
        try:
            id_cliente = int(input("Ingresa el ID del cliente que deseas buscar: "))
            cliente_encontrado = next((cliente for cliente in clientes if cliente["ID"] == id_cliente), None)
            if cliente_encontrado:
                for key, value in cliente_encontrado.items():
                    print(f"{key}: {value}")
                break       
        except ValueError:
            print("Ingresa un valor numerico")

def actualizar_cliente():
    with open("Datas/Clientes.json", "r") as outfile:
        data = json.load(outfile)
    clientes = data["Clientes"]
    id_cliente = int(input("Ingresa el ID del cliente que deseas actualizar: "))
    for cliente in clientes:
        if cliente["ID"] == id_cliente:
            N_documento = ingresar_numero("Ingresa el nuevo numero de documento: ")
            Nombre = input("Ingresa el nombre: ")
            Apellido = input("Ingresa el apellido: ")
            N_celular = ingresar_numero("Ingresa el nuevo numero de celular: ")
            Direccion = input("Ingrese la nueva direccion del cliente: ")
            categoria = input("Ingrese la nueva categoría: ")
            Contacto_Soporte = input("numero de veces que el cliente contactó con soporte" )

        cliente["N_documento"] = N_documento    
        cliente["Nombre"] = Nombre    
        cliente["Apellido"] = Apellido   
        cliente["N_celular"] = N_celular  
        cliente["Direccion"] = Direccion
        cliente["categoria"] = categoria
        cliente["Contacto_Soporte"] = Contacto_Soporte

    with open("Datas/Clientes.json", "w") as outfile:
        json.dump(data, outfile, indent = 4)      

def eliminar_cliente():
    with open("Datas/Clientes.json", "r") as outfile:
        data = json.load(outfile)
    clientes = data["Clientes"]
    id_cliente = int(input("Ingresa el ID del cliente que deseas eliminar: "))
    for cliente in clientes:
        if cliente["ID"] == id_cliente:
            clientes.remove(clientes)

def Registrar_servicio():

    with open("Datas/Clientes.json", "r") as outfile:
        data = json.load(outfile)
    clientes = data["Clientes"]
    servicio_registrado = set()
    for cliente in clientes.get("Servicios", []):
            s = input(f"Ingresa el servicio N. {cliente}")
            servicio_registrado.add(s)
    
    with open("Datas/Clientes.json", "w") as outfile:
        json.dump(data, outfile, indent = 4)



                        