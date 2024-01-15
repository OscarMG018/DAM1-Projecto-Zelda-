import Guardado
import copy

inventario = {"Vegetable": 0, "Fish": 0, "Meat": 0, "Salad": 0, "Pescatarian": 0, "Roasted": 0}
inventario_armas = {"Wood Sword":[0, 1, False], "Sword": [0, 1, True], "Wood Shield":[0, 1, False], "Shield":[0, 1, True]}


#opcion = input(str("Introduce una opcion de inventario: "))
def equip_weapon(type):
    global inventario_armas
    if inventario_armas[type][1] != 0:
        if inventario_armas["Wood Sword"][2] == False and inventario_armas["Sword"][2] == False:
            inventario_armas[type][2] = True
            return f"You have equipped '{type}'"
        elif inventario_armas["Wood Sword"][2] == True:
            return "You already have 'Wood Sword' equipped'"
        elif inventario_armas["Sword"][2] == True:
            return "You already have 'Sword' equipped'"
    else:
        return f"You don't have '{type}'"

def equip_shield(type):
    global inventario_armas
    if inventario_armas[type][1] != 0:
        if inventario_armas["Wood Shield"][2] == False and inventario_armas["Shield"][2] == False:
            inventario_armas[type][2] = True
            return f"You have equipped '{type}'"
        elif inventario_armas["Wood Shield"][2] == True:
            return "You already have 'Wood Shield' equipped'"
        elif inventario_armas["Shield"][2] == True:
            return "You already have 'Shield' equipped'"
    else:
        return f"You don't have '{type}'"

def unequip_item(type):
    global inventario_armas
    if inventario_armas[type][1] != 0:
        if inventario_armas[type][2] == True:
            inventario_armas[type][2] = False
            return f"You have unequipped '{type}'"
        else:
            return f"You don't have '{type}' equipped"
    else:
        return f"You don't have '{type}'"
    
def GetEquipedWeapon():
    global inventario_armas
    for key, value in inventario_armas.items():
        if key in ["Wood Sword", "Sword"] and value[2] == True:
            return key
        
def GetEquipedShield():
    global inventario_armas
    for key, value in inventario_armas.items():
        if key in ["Wood Shield", "Shield"] and value[2] == True:
            return key

def UseWeapon():
    global inventario_armas
    equiped_weapon = GetEquipedWeapon()
    inventario_armas[equiped_weapon][0] -= 1
    if inventario_armas[equiped_weapon][0] == 0:
        inventario_armas[equiped_weapon][1] -= 1
        if equiped_weapon == "Sword":
            inventario_armas[equiped_weapon[0]] = 9
        else:
            inventario_armas[equiped_weapon[0]] = 5
        if inventario_armas[equiped_weapon][1] == 0:
            inventario_armas[equiped_weapon[2]] = False
        return f"{equiped_weapon} has been broken, you have {inventario_armas[equiped_weapon][1]} left"
    
def UseShield():
    global inventario_armas
    equiped_shield = GetEquipedShield()
    inventario_armas[equiped_shield][0] -= 1
    if inventario_armas[equiped_shield][0] == 0:
        inventario_armas[equiped_shield][1] -= 1
        if equiped_shield == "Shield":
            inventario_armas[equiped_shield[0]] = 9
        else:
            inventario_armas[equiped_shield[0]] = 5
        if inventario_armas[equiped_shield][1] == 0:
            inventario_armas[equiped_shield[2]] = False
        return f"{equiped_shield} has been broken, you have {inventario_armas[equiped_shield][1]} left"

def AddItem(nombre, cantidad):
    global inventario_armas, inventario
    if nombre in ["Vegetable", "Fish", "Meat", "Salad", "Pescatarian", "Roasted"]:
        inventario[nombre] += cantidad
    if nombre in ["Wood Sword", "Wood Shield"]:
        inventario_armas[nombre][1] += cantidad
        inventario_armas[nombre][0] = 5       
    if nombre in ["Sword", "Shield"]:
        inventario_armas[nombre][1] += cantidad
        inventario_armas[nombre][0] = 9

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