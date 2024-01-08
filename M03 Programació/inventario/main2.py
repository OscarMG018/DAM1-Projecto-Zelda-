inventario_armas = {"Wood Sword":[0, 0, False], "Sword": [0, 0, False], "Wood Shield":[0, 0, False], "Shield":[0, 0, False]}


#opcion = input(str("Introduce una opcion de inventario: "))

def equip_weapon(opcion, inventario_armas):
    opcion_split = opcion.split()
    if opcion_split[0] == "Equip":
        if len(opcion_split) == 2:
            if opcion_split[1] == "Sword":
                if inventario_armas["Sword"][1] > 0:
                    if inventario_armas["Sword"][2] == False:
                        print("Se ha equipado Sword")
                        inventario_armas["Wood Sword"][2] == False
                        inventario_armas["Sword"][2] == True
                    else:
                        print("Ya tienes Sword equipada")
                else:
                    print("No hay suficientes")

                
            elif opcion_split[1] == "Shield":
                if inventario_armas["Shield"][1] > 0:
                    if inventario_armas["Shield"][2] == False:
                        print("Se ha equipado Shield")
                        inventario_armas["Wood Shield"][2] == False
                        inventario_armas["Shield"][2] == True
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
                            inventario_armas["Sword"][2] == False
                            inventario_armas["Wood Sword"][2] == True
                        else:
                            print("Ya tienes Wood Sword equipada")
                    else:
                        print("No hay suficientes")


                elif opcion_split[2] == "Shield":
                    if inventario_armas["Wood Shield"][1] > 0:
                        if inventario_armas["Wood Shield"][2] == False:
                            print("Se ha equipado Wood Shield")
                            inventario_armas["Shield"][2] == False
                            inventario_armas["Wood Shield"][2] == True
                        else:
                            print("Ya tienes Wood Shield equipada")
                    else:
                        print("No hay suficientes")

def GetEquipedWeapon():
    global inventario_armas
    for key, value in inventario_armas.items():
        if key in ["Wood Sword", "Sword"] and value[2] == True:
            return key

def UseWeapon():
    global inventario_armas
    equiped_weapon = GetEquipedWeapon()
    inventario_armas[equiped_weapon][0] -= 1
    if inventario_armas[equiped_weapon][0] == 0:
        inventario_armas[inventario_armas][1] -= 1
        if equiped_weapon == "Sword":
            inventario_armas[equiped_weapon[0]] = 9
        else:
            inventario_armas[equiped_weapon[0]] = 5
        if inventario_armas[inventario_armas][1] == 0:
            inventario_armas[inventario_armas[2]] = False
        return f"{equiped_weapon} has been broken"

def AddItem(nombre, cantidad):
    global inventario_armas, inventario
    if nombre in ["Vegetable", "Fish", "Meat", "Salad", "Pescatarian", "Roasted"]:
        for x in range(cantidad):
            inventario[nombre] += 1
    if nombre in ["Wood Sword", "Wood Shield" , "Sword", "Shield"]:
        for x in range(cantidad):
            inventario_armas[nombre][1] += 1
                    
