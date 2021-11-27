#Productos
catalogo_comidas={"100": "Hamburguesa", "101": "Perro caliente", "102": "Pizza","Nombre":"Comidas"}
catalogo_bebidas={"200": "Gaseosa", "201": "Agua", "202": "Té","Nombre":"Bebidas"}
catalogo_postres={"300": "Chocolatina", "301": "Helado", "302": "Dona","Nombre":"Postres"}


def imprimir_menu(catalogos):
    print("Menu:")
    print("\t\tCodigo\tProducto")
    for ci in catalogos:
        print(f'\t{ci["Nombre"]}')
        
        for k in ci:
            if k != "Nombre":
                print(f"\t\t{k}\t{ci[k]}")

def pedidos_costo():

    catalogos = [catalogo_comidas,catalogo_bebidas,catalogo_postres]
    catalogo_completo = {}
    for ci in catalogos:
        catalogo_completo.update(ci)

    cedula = input("Ingrese cedula: ")
    while cedula != "": #El programa acaba cuando no se ingresa nada en cedula
        if cedula.isnumeric():
            rol = input("Ingrese rol (1 para estudiante, 2 para profesor): ")
            while rol != "1" and rol != "2":
                print("Rol invalido")
                rol = input("Ingrese rol (1 para estudiante, 2 para profesor): ")
            
            print()

            imprimir_menu(catalogos)

            codigos = []
            valor = 0

            print("Registrar productos:")
            codigo_producto = input("Ingrese el codigo del producto: ")
            while codigo_producto != "": #Si no se ingresa el codigo del producto se asume que se debe parar de registrar
                if codigo_producto in catalogo_completo:
                    cantidad = input("Ingrese la cantidad: ")
                    while not cantidad.isnumeric():
                        print("Las cantidades deben ser numericas")
                        cantidad = input("Ingrese la cantidad: ")
                    cantidad = int(cantidad)
                    
                    precio = input("Ingrese el precio: ")
                    while not precio.isnumeric():
                        print("El precio debe ser numerico")
                        precio = input("Ingrese el precio: ")
                    precio = int(precio)
                    
                    codigos.append(codigo_producto)
                    if rol == "1":
                        valor += (precio*cantidad)*0.5
                    elif rol == "2":
                        valor += (precio*cantidad)*0.8
                else:
                    print("El codigo no es valido")
                codigo_producto = input("Ingrese el codigo del producto: ")

            print()
            if rol == "1":
                rol = "Estudiante"
            elif rol == "2":
                rol = "Profesor"


            if len(codigos)==1:
                print(f"El {rol} con cedula {cedula}, debe pagar {valor} por el producto {catalogo_completo[codigos[0]]}")
            elif len(codigos)>0:
                productos = ""
                for c in codigos[:-1]:
                    productos += catalogo_completo[c] + ", "
                productos += catalogo_completo[codigos[-1]]
                print(f"El {rol} con cedula {cedula}, debe pagar {valor} por los productos {productos}")
            else:
                print(f"El {rol} con cedula {cedula}, debe pagar {valor}")
                    
        else:
            print("La cedula solo debe contener números")
        
    
        cedula = input("Ingrese cedula: ")


if __name__ == '__main__':
    pedidos_costo()