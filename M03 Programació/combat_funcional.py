inventario = {"Vegetable": 0, "Fish": 0, "Meat": 0, "Salad": 0, "Pescatarian": 0, "Roasted": 0}
inventario_armas = {"Wood Sword":[0, 0, False], "Sword": [0, 0, False], "Wood Shield":[0, 0, False], "Shield":[0, 1, False]}


#opcion = input(str("Introduce una opcion de inventario: "))

def equip_weapon(type, inventario_armas):
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

def equip_shield(type, inventario_armas):
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

def unequip_item(type, inventario_armas):
    if inventario_armas[type][1] != 0:
        if inventario_armas[type][2] == True:
            inventario_armas[type][2] = False
            return f"You have unequipped '{type}'"
        else:
            return f"You don't have '{type}' equipped"
    else:
        return f"You don't have '{type}'"


def tryattack():
    playerIndex = GetPlayerIndex()
    player = GetPlayer()

    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dy == 0 and dx == 0:
                continue

            y, x = player["y"] + dy, player["x"] + dx
            if ValidPosition(y, x):
                entity = GetEntityByPosition(y, x)
                if entity and entity["name"] in ["Enemy", "Fox"]:
                    return True, GetIndexOfEntity(entity)

    return False, -1

def attack():
    success, entityIndex = tryattack()

    if not success:
        return "No hay entidades cercanas para atacar."

    weapon_equipped = None
    shield_equipped = None
    for weapon, stats in inventario_armas.items():
        if stats[2] == True and weapon in ["Sword","Wood Sword"]:  # Check if the weapon is equipped
            weapon_equipped = weapon
            break
    
    for shield, stats in inventario_armas.items():
        if stats[2] == True and shield in ["Shield","Wood Shield"]:  # Check if the shield is equipped
            shield_equipped = shield
            break

    if weapon_equipped is None:
        return "No hay armas equipadas para atacar."

    player = GetPlayer()
    entity = GetEntityByIndex(entityIndex)

    weapon_stats = inventario_armas[weapon_equipped]

    if entity["name"] == "Enemy":
        # Attack enemy
        entity["life"] -= 1
        if ahield_equipped in ["Shield", "Wood Shield"]:
            player["vida"] -= 0  # No damage to player if shield is equipped
        else:
            player["vida"] -= 1

        if entity["life"] <= 0:
            RemoveEntity(entityIndex)
            return f"Atacaste al enemigo con {weapon_equipped}. ¡Enemigo eliminado!"
        else:
            return f"Atacaste al enemigo con {weapon_equipped}. Vida restante del enemigo: {entity['life']}."

    elif entity["name"] == "Fox":
        # Attack fox
        RemoveEntity(entityIndex)
        return f"Atacaste al zorro con {weapon_equipped}. ¡Zorro eliminado!"

def UseWeapon(weapon):
    inventario_armas[weapon][0] -= 1
    if inventario_armas[weapon][0] == 0:
        if inventario_armas[weapon][1] == 1:
            inventario_armas[weapon][1] = 0
            inventario_armas[weapon][0] = 0
        else:
            if weapon in ["Wood Sword", "Wood Shield"]:
                inventario_armas[weapon][1] -= 1
                inventario_armas[weapon][0] = 5
            if weapon in ["Sword","Shield"]:
                inventario_armas[weapon][1] -= 1
                inventario_armas[weapon][0] = 9


def TryAttackGanon():
    playerIndex = GetPlayerIndex()
    px = GetEntityByIndex(playerIndex)["x"]
    if px == 21:
        weapon_equipped = None
        for weapon, stats in inventario_armas.items():
            if stats[2] == True and weapon in ["Sword","Wood Sword"]:  # Check if the weapon is equipped
                weapon_equipped = weapon
                break
        if weapon_equipped != None:
            AttackGanon()
        else:
            return "No hay armas equipadas para atacar."
    else:
        return "Ganon is out of range"

def AttackGanon():
    ganonhealth = 8

def InFrontOfGanon():
    playerIndex = GetPlayerIndex()
    px = GetEntityByIndex(playerIndex)["x"]
    if px == 21:
    # treure un cor al jugador
    player_life -= 1
    return "Ganon's presence hurts you"

#---------------------------------------------------------------------------------------------------------------#

        frases = [      "Ganon is powerful, are you sure you can defeat him?"
                        "Ganon's strength is supernatural, Zelda fought with bravery."
                        "To Ganon, you are like a fly, find a weak spot and attack."
                        "Ganon will not surrender easily."
                        "Ganon has fought great battles, is an expert fighter."
                        "Link, transform your fears into strengths."
                        "Keep it up, Link, Ganon can't hold out much longer."
                        "Link, history repeats itself, Ganon can be defeated."
                        "Think of all the warriors who have tried before."
                        "You fight for the weaker ones, Link, persevere."               ]

#---------------------------------------------------------------------------------------------------------------#

def attackGanon():
    global maps

    # Obtener todas las entidades de corazón de Ganon en el castillo
    ganon_hearts = GetAllEntiiesWithName("GanonHeart", location="Castle")

    if ganon_hearts:
        # Obtener la última entidad de corazón de Ganon
        last_ganon_heart = ganon_hearts[-1]

        # Eliminar la última entidad de corazón de Ganon
        RemoveEntity(GetIndexOfEntity(last_ganon_heart))

        # Verificar si quedan más corazones de Ganon
        remaining_ganon_hearts = GetAllEntiiesWithName("GanonHeart", location="Castle")
        if not remaining_ganon_hearts:
            # Ganon está derrotado, realiza las acciones necesarias
            print("¡Has derrotado a Ganon!")
            # Llamar a la función de pantalla de victoria u otras acciones de victoria

        # Retorna un mensaje aleatorio como resultado del ataque
        return random.choice(frases)

    