inventario_armas = {"Wood Sword":[0, 0, False], "Sword": [0, 0, False], "Wood Shield":[0, 0, False], "Shield":[0, 0, False]}


opcion = input(str("Introduce una opcion de inventario: "))

def equip_weapon(opcion, inventario_armas):
    opcion_split = opcion.split()
    if opcion_split[0] == "Equip":
        if len(opcion_split) == 2:
            if opcion_split[1] == "Sword":
                if inventario_armas["Sword"][1] > 0:
                    if inventario_armas["Sword"][2] == False:
                        print("Se ha equipado Sword")
                        inventario_armas["Wood Sword"][2] = False
                        inventario_armas["Sword"][2] = True
                    else:
                        print("Ya tienes Sword equipada")
                else:
                    print("No hay suficientes")

                
            elif opcion_split[1] == "Shield":
                if inventario_armas["Shield"][1] > 0:
                    if inventario_armas["Shield"][2] == False:
                        print("Se ha equipado Shield")
                        inventario_armas["Wood Shield"][2] = False
                        inventario_armas["Shield"][2] = True
                    else:
                        print("Ya tienes Shield equipado")
                else:
                    print("No hay suficientes")
            
        if len(opcion_split) == 3:
            if opcion_split[1] == "Wood":
                if opcion_split[2] == "Sword":
                    if inventario_armas["Wood Sword"][1] > 0:
                        if inventario_armas["Wood Sword"][2] == False:
                            print("Se ha equipado Wood Sword")
                            inventario_armas["Sword"][2] = False
                            inventario_armas["Wood Sword"][2] = True
                        else:
                            print("Ya tienes Wood Sword equipada")
                    else:
                        print("No hay suficientes")


                elif opcion_split[2] == "Shield":
                    if inventario_armas["Wood Shield"][1] > 0:
                        if inventario_armas["Wood Shield"][2] == False:
                            print("Se ha equipado Wood Sword")
                            inventario_armas["Shield"][2] = False
                            inventario_armas["Wood Shield"][2] = True
                        else:
                            print("Ya tienes Wood Shield equipado")
                    else:
                        print("No hay suficientes")