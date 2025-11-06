import datetime

print("PROGRAMA DE VENTA DE COMBUSTIBLE")

gasolina_premium = 290.10
gasolina_regular = 272.50
gasoil_optimo = 242.10
gasoil_regular = 224.80
aceite = 350.00

fecha = datetime.datetime.now()
formato = fecha.strftime("%d/%m/%Y %H:%M:%S")
cliente = "Consulting SRL"

while True:
    rnc = input("\nIngrese RNC del cliente: ")
    if not rnc.isdigit():
        print("Dato inválido. Ingrese solo números.")
        continue
    if not (len(rnc) == 9 or len(rnc) == 11):
        print("El número debe tener exactamente 9 dígitos (RNC) o 11 dígitos (Cédula).")
        continue
    
    while True:
        print("\n---PRODUCTOS---\n"
            "1. Gasolina Premium\n"
            "2. Gasolina Regular\n"
            "3. Gasoil Optimo\n"
            "4. Gasoil Regular\n"
            "5. Aceite de motor\n"
            "6. Salir\n")
        
        opcion = input("Ingrese producto: ")
        
        if opcion == "6":
            print("Cerrando sistema...")
            print("Sistema cerrado")
            break
    
        #Acciones del programa segùn el producto seleccinado
        elif opcion == "1":
            monto = int(input("ingrese monto: "))
            producto = "Gasolina Premium"
            Precio = gasolina_premium
            cantidad = monto / gasolina_premium
        elif opcion == "2":
            monto = int(input("ingrese monto: "))
            producto = "Gasolina Regular"
            Precio = gasolina_regular
            cantidad = monto / gasolina_regular
        elif opcion == "3":
            monto = int(input("ingrese monto: "))
            producto = "Gasoil Optimo"
            Precio = gasoil_optimo
            cantidad = monto / gasoil_optimo
        elif opcion == "4":
            monto = int(input("ingrese monto: "))
            producto = "Gasoil Regular"
            Precio = gasoil_regular
            cantidad = monto / gasoil_regular
        
        elif opcion == "5":
            cantidad = int(input("Ingrese cantidad: "))
            producto = "Aceite"
            impuestos = aceite * cantidad * 0.18
            subtotal = (aceite * cantidad) - impuestos
            print("\n----------------------------------------\n"
            "            ESTACION CORAL SRL\n")
            print ("**********FACTURA**********\n"
                    f"Fecha: {formato}\n"
                    f"RNC: {rnc}\n"
                    f"Cliente: {cliente}\n"
                f"\nProducto              monto\n"
                    "-----------------------------\n"
                f"{producto}...............${aceite:.2f}\n"
                f"Cantidad.............{cantidad} Ctr.\n"
                "\n"
                f"Subtotal.............${subtotal:.2f}\n"
                f"Impuestos............${impuestos:.2f}\n"
                f"Total................${aceite * cantidad + impuestos:.2f}\n"
                f"****GRACIAS POR PREFERIRNOS****\n")
            print("----------------------------------------\n")
            break        
        else:
            print("Producto incorretcto. Ingrese un producto válido.\n")
            continue
        
        print("\n----------------------------------------\n"
        "           ESTACION CORAL SRL\n")
        print("**************FACTURA**************\n"
            f"Fecha: {formato}\n"
            f"RNC: {rnc}\n"
            f"Cliente: {cliente}\n"
            f"\nProducto                     monto\n"
            "------------------------------------\n"
                f"{producto}............${Precio:.2f}\n"
                "\n"
                f"Cantidad....................{cantidad:.2f} Gls.\n"
                f"Total.......................${monto:.2f}\n"
                f"*******GRACIAS POR PREFERIRNOS*******\n")
        print("----------------------------------------\n")
        break
        

