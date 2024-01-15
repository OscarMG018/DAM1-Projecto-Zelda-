import Guardado
import Inventario
import Jugabilidad
import random

PlayerLife = 3
PlayerMaxLife = 3
BloodMoon = 0
BloodMoonAppearances = 0



def tryattack():
    player = Jugabilidad.GetPlayer()

    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dy == 0 and dx == 0:
                continue

            y, x = player["y"] + dy, player["x"] + dx
            if Jugabilidad.ValidPosition(y, x):
                entity = Jugabilidad.GetEntityByPosition(y, x)
                if entity and entity["name"] in ["Enemy", "Fox"]:
                    return True, Jugabilidad.GetIndexOfEntity(entity)

    return False, -1

def attack():
    success, entityIndex = tryattack()

    if not success:
        return "No hay entidades cercanas para atacar."

    weapon_equipped = GetEquipedWeapon()
    shield_equipped = GetEquipedShield()


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
    playerIndex = Jugabilidad.GetPlayerIndex()
    px = Jugabilidad.GetEntityByIndex(playerIndex)["x"]
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
    ganon_hearts = Jugabilidad.GetAllEntiiesWithName("GanonHeart", location="Castle")

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
        Jugabilidad.RemoveEntity(Jugabilidad.GetIndexOfEntity(last_ganon_heart))

        # Añadir un mensaje aleatorio como resultado del ataque
        messages.append(random.choice(frases))
        
        # Verificar si quedan más corazones de Ganon
        remaining_ganon_hearts = Jugabilidad.GetAllEntiiesWithName("GanonHeart", location="Castle")
        if not remaining_ganon_hearts:
            # Ganon está derrotado, realiza las acciones necesarias
            messages.append("It has been an exhausting fight, but with persistence, you have achieved it.")
            # Llamar a la función de pantalla de victoria u otras acciones de victoria

        return messages

def InFrontOfGanon():
    playerIndex = Jugabilidad.GetPlayerIndex()
    px = Jugabilidad.GetEntityByIndex(playerIndex)["x"]
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