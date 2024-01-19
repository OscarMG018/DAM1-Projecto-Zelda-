import Guardado
import Inventario
import MapSystem
import random

PlayerLife = 3
PlayerMaxLife = 3
BloodMoon = 0
BloodMoonAppearances = 0

def tryattack():
    player = MapSystem.GetPlayer()
    enemy = MapSystem.AdjacentEntity(player["y"],player["x"],"Enemy")
    fox = MapSystem.AdjacentEntity(player["y"],player["x"],"Fox")
    if enemy != None:
        return True, MapSystem.GetIndexOfEntity(enemy)
    elif (fox != None and fox["visible"]):
        return True, MapSystem.GetIndexOfEntity(fox)
    return False, -1

def attack():
    global PlayerLife
    success, entityIndex = tryattack()
    if not success:
        return ["No hay entidades cercanas para atacar."]

    weapon_equipped = Inventario.GetEquipedWeapon()
    shield_equipped = Inventario.GetEquipedShield()

    if weapon_equipped is None:
        return ["You don't have a weapon equiped"]

    player = MapSystem.GetPlayer()
    entity = MapSystem.GetEntityByIndex(entityIndex)

    if entity["name"] == "Enemy":
        messages = []
        if shield_equipped == "Shield":
            if random.random() > 0.6:
                PlayerLife -= 1
            else:
                messages.append(f"You blocked the attack")
            message = Inventario.UseShield()
            if message != None:
                messages.append(message)
        elif shield_equipped == "Wood Shield":    
            if random.random() > 0.4:
                PlayerLife -= 1
            else:
                messages.append(f"You blocked the attack")
            message = Inventario.UseShield()
            if message != None:
                messages.append(message)
        else:
            PlayerLife -= 1

        # Attack enemy
        MapSystem.MoveEnemy(MapSystem.GetIndexOfEntity(entity))
        entity["life"] -= 1
        message = Inventario.UseWeapon()
        if message != None:
            messages.append(message)
        if entity["life"] <= 0:
            MapSystem.RemoveEntity(entityIndex)
            messages.append(f"“You defeated an enemy, this is a dangerous zone")
        else:
            messages.append(f"Brave, keep fighting Link")
        messages.append(f"Be careful Link, you only have {PlayerLife} hearts")
        return messages

    elif entity["name"] == "Fox":
        # Attack fox
        MapSystem.RemoveEntity(entityIndex)
        message = [Inventario.UseWeapon()]
        Inventario.AddItem("Meat",1)
        if len(message) > 0:
            return ["You got meat"] + message
        return [f"You got meat"]
    

frases = [
    "Ganon is powerful, are you sure you can defeat him?",
    "Ganon's strength is supernatural, Zelda fought with bravery.",
    "To Ganon, you are like a fly, find a weak spot and attack.",
    "Ganon will not surrender easily.",
    "Ganon has fought great battles, is an expert fighter.",
    "Link, transform your fears into strengths.",
    "Keep it up, Link, Ganon can't hold out much longer.",
    "Link, history repeats itself, Ganon can be defeated.",
    "Think of all the warriors who have tried before.",
    "You fight for the weaker ones, Link, persevere."
]

def TryAttackGanon():
    playerIndex = MapSystem.GetPlayerIndex()
    px = MapSystem.GetEntityByIndex(playerIndex)["x"]
    if px == 19:
        weapon_equipped = Inventario.GetEquipedWeapon()
        if weapon_equipped != None:
            return True,None
        else:
            return False,["No hay armas equipadas para atacar."]
    else:
        return False,["Ganon is out of range"]

def attackGanon():
    global PlayerLife
    if not TryAttackGanon()[0]:
        return TryAttackGanon()[1]
    messages = []

    # Obtener todas las entidades de corazón de Ganon en el castillo
    ganon_hearts = MapSystem.GetAllEntiiesWithName("GanonHeart", location="Castle")

    if ganon_hearts:
        # Obtener la última entidad de corazón de Ganon
        last_ganon_heart = ganon_hearts[-1]

        # Restar una vida al jugador
        PlayerLife -= 1

        #Usar la espada
        message = Inventario.UseWeapon()
        if message != None:
            messages.append(message)

        # Eliminar la última entidad de corazón de Ganon
        MapSystem.RemoveEntity(MapSystem.GetIndexOfEntity(last_ganon_heart))

        # Añadir un mensaje aleatorio como resultado del ataque
        messages.append(random.choice(frases))
        
        # Verificar si quedan más corazones de Ganon
        remaining_ganon_hearts = MapSystem.GetAllEntiiesWithName("GanonHeart", location="Castle")
        if not remaining_ganon_hearts:
            # Ganon está derrotado, realiza las acciones necesarias
            messages.append("It has been an exhausting fight, but with persistence, you have achieved it.")
            # Llamar a la función de pantalla de victoria u otras acciones de victoria

        return messages

def InFrontOfGanon():
    playerIndex = MapSystem.GetPlayerIndex()
    px = MapSystem.GetEntityByIndex(playerIndex)["x"]
    if px == 19:
        return True
    return False


def InitCombate(CombateInfo=None):
    global PlayerLife, PlayerMaxLife, BloodMoon, BloodMoonAppearances
    if CombateInfo != None:
        PlayerLife = CombateInfo[0]
        PlayerMaxLife = CombateInfo[1]
        BloodMoon = CombateInfo[2]
        BloodMoonAppearances = CombateInfo[3]
    else:
        PlayerLife = 3
        PlayerMaxLife = 3
        BloodMoon = 0
        BloodMoonAppearances = 0

def SaveCombate(number):
    global PlayerLife, PlayerMaxLife, BloodMoon, BloodMoonAppearances
    Guardado.Saves[number]["PlayerLife"] = PlayerLife
    Guardado.Saves[number]["PlayerMaxLife"] = PlayerMaxLife
    Guardado.Saves[number]["BloodMoon"] = BloodMoon
    Guardado.Saves[number]["BloodMoonAppearances"] = BloodMoonAppearances