import Guardado
import copy

inventario = {"Vegetable": 0, "Fish": 0, "Meat": 0, "Salad": 0, "Pescatarian": 0, "Roasted": 0}
inventario_armas = {"Wood Sword":[0, 0, False], "Sword": [0, 0, False], "Wood Shield":[0, 0, False], "Shield":[0, 0, False]}


#opcion = input(str("Introduce una opcion de inventario: "))

def equip_weapon(opcion):
    global inventario_armas
    opcion_split = opcion.split()
    if opcion_split[0] == "equip":
        if len(opcion_split) == 2:
            if opcion_split[1] == "Sword":
                if inventario_armas["Sword"][1] > 0:
                    if inventario_armas["Sword"][2] == False:
                        inventario_armas["Wood Sword"][2] == False
                        inventario_armas["Sword"][2] == True
                        return "Se ha equipado Sword",True
                    else:
                        return "Ya tienes Sword equipada",False
                else:
                    return f"No hay suficientes{opcion_split[1]}",False

                
            elif opcion_split[1] == "Shield":
                if inventario_armas["Shield"][1] > 0:
                    if inventario_armas["Shield"][2] == False:
                        inventario_armas["Wood Shield"][2] == False
                        inventario_armas["Shield"][2] == True
                        return "Se ha equipado Shield",True
                    else:
                        return "Ya tienes Shield equipado",False
                else:
                    return "No hay suficientes",False
            
        if len(opcion_split) == 3:
            if opcion_split[1] == "Wood":
                if opcion_split[2] == "Sword":
                    if inventario_armas["Wood Sword"][1] > 0:
                        if inventario_armas["Wood Sword"][2] == False:
                            inventario_armas["Sword"][2] == False
                            inventario_armas["Wood Sword"][2] == True
                            return "Se ha equipado Wood Sword",True
                        else:
                            return "Ya tienes Wood Sword equipada",False
                    else:
                        return "No hay suficientes",False


                elif opcion_split[2] == "Shield":
                    if inventario_armas["Wood Shield"][1] > 0:
                        if inventario_armas["Wood Shield"][2] == False:
                            inventario_armas["Shield"][2] == False
                            inventario_armas["Wood Shield"][2] == True
                            return "Se ha equipado Wood Shield",True
                        else:
                            return "Ya tienes Wood Shield equipada",False
                    else:
                        return "No hay suficientes",False

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

def GetItem(nombre):
    global inventario_armas, inventario
    if nombre in ["Vegetable", "Fish", "Meat", "Salad", "Pescatarian", "Roasted"]:
        return inventario[nombre]
    if nombre in ["Wood Sword", "Wood Shield" , "Sword", "Shield"]:
        return inventario_armas[nombre]

def RemoveItem(nombre, cantidad):
    global inventario_armas, inventario
    if nombre in ["Vegetable", "Fish", "Meat", "Salad", "Pescatarian", "Roasted"]:
        inventario[nombre] -= cantidad
    if nombre in ["Wood Sword", "Wood Shield" , "Sword", "Shield"]:
        inventario_armas[nombre][1] -= cantidad

def InvenroryInit(invetoryInfo=None):
    global inventario, inventario_armas
    if invetoryInfo != None:
        inventario = copy.deepcopy(invetoryInfo[0])
        inventario_armas = copy.deepcopy(invetoryInfo[1])
    else :
        inventario = {"Vegetable": 0, "Fish": 0, "Meat": 0, "Salad": 0, "Pescatarian": 0, "Roasted": 0}
        inventario_armas = {"Wood Sword":[0, 0, False], "Sword": [0, 0, False], "Wood Shield":[0, 0, False], "Shield":[0, 0, False]}

def SaveInventory(number):
    global inventario_armas, inventario
    Guardado.Saves[number]["Inventario"] = copy.deepcopy(inventario)
    Guardado.Saves[number]["Inventario Armas"] = copy.deepcopy(inventario_armas)