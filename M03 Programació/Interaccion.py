import Jugabilidad
import random
import Inventario
import Combate

#Pesca

fished = False

def TryFishing():
    playerIndex = Jugabilidad.GetPlayerIndex()
    px = Jugabilidad.GetEntityByIndex(playerIndex)["x"]
    py = Jugabilidad.GetEntityByIndex(playerIndex)["y"]
    if fished:
        return False,"You have already fished in this loacation"
    if not Jugabilidad.AdjacentTerrain(py,px,"~"):
        return False, "There isn't water near you"
    return True,None

def Fishing():
    global fished
    if not TryFishing()[0]:
        return TryFishing()[1]
    p = random.random()
    if p < 0.2:
        Inventario.AddItem("Fish", 1)
        fished = True
        return "You Get A Fish"
    return"You don't Get A Fish"

#Fox

def DecideFoxVisibility():
    foxlist = Jugabilidad.GetAllEntiiesWithName("Fox")
    if len(foxlist) == 0:
        return
    fox = foxlist[0]
    if random.random() < 0.5:
        fox["visible"] = True
        return "You see a Fox"
        return
    fox["visible"] = False
    return "You don't see a Fox"

#Cocinar

CookingIngredients =  {
    "Salad" : [["Vegetable",2]],
    "Pescatarian" : [["Fish",1],["Vegetable",1]],
    "Roasted" : [["Meat",1],["Vegetable",1]]
}

def TryCook(name):
    player = Jugabilidad.GetPlayer()
    px = player["x"]
    py = player["y"]
    if Jugabilidad.AdjacentEntity(py,px,"Cuina") == None:
        return False, "There isn't a cooking pot here"
    if name not in CookingIngredients:
        return False, "This recipe doesn't exist"
    insuficientIngredients = []
    for ingridient in CookingIngredients[name]:
        if Inventario.GetItem(ingridient[0]) < ingridient[1]:
            insuficientIngredients.append(ingridient[0])
    if len(insuficientIngredients) > 0:
        return False, "You don't have enough "+" and ".join(insuficientIngredients)
    return True,None
                   
def Cook(name):
    if not TryCook(name)[0]:
        return TryCook(name)[1]
    for ingridient in CookingIngredients[name]:
        Inventario.RemoveItem(ingridient[0],ingridient[1])
    Inventario.AddItem(name,1)
    return f"You cooked a {name}"

#Cofres

def TryOpenChest():
    playerIndex = Jugabilidad.GetPlayerIndex()
    px = Jugabilidad.GetEntityByIndex(playerIndex)["x"]
    py = Jugabilidad.GetEntityByIndex(playerIndex)["y"]
    if Jugabilidad.AdjacentEntity(py,px,"Closed Chest") == None:
        if Jugabilidad.AdjacentEntity(py,px,"Open Chest") != None:
            return False, "This chest is already open"
        else:
            return False, "There isn't a closed chest here"
    return True,None

def OpenChest():
    if not TryOpenChest()[0]:
        return TryOpenChest()[1]
    playerIndex = Jugabilidad.GetPlayerIndex()
    px = Jugabilidad.GetEntityByIndex(playerIndex)["x"]
    py = Jugabilidad.GetEntityByIndex(playerIndex)["y"]
    chest = Jugabilidad.AdjacentEntity(py,px,"Closed Chest")
    Inventario.AddItem(chest["item"],1)
    chest["name"] = "Open Chest"
    chest["symbol"] = "W"
    return f"You got a {chest['item']}"

def RecloseChest():
    chests = Jugabilidad.GetAllEntiiesWithName("Open Chest")
    for chest in chests:
        chest["name"] = "Closed Chest"
        chest["symbol"] = "M"

#Sanctuary

def TryOpenSanctuary():
    player = Jugabilidad.GetPlayer()
    px = player["x"]
    py = player["y"]
    sanc = Jugabilidad.AdjacentEntity(py,px,"Sanctuary")
    if sanc == None:
        return False, "There isn't a sanctuary here"
    elif Jugabilidad.OpenSanctuaris[sanc["SanctuaryNumber"]] == True:
        return False, "You already opened this sanctuary"
    return True,None

def OpenSanctuary():
    if not TryOpenSanctuary()[0]:
        return TryOpenSanctuary()[1]
    player = Jugabilidad.GetPlayer()
    px = player["x"]
    py = player["y"]
    sanc = Jugabilidad.AdjacentEntity(py,px,"Sanctuary")
    Jugabilidad.OpenSanctuaris[sanc["SanctuaryNumber"]] = True
    Combate.PlayerMaxLife += 1
    return "You opened the sanctuary"

#Tree

def TryShakeTree():
    player = Jugabilidad.GetPlayer()
    px = player["x"]
    py = player["y"]
    if Jugabilidad.AdjacentEntity(py,px,"Tree") == None:
        if Jugabilidad.AdjacentEntity(py,px,"Broken Tree") != None:
            return False, ["The tree is not ready yet"]
        return False, ["There isn't a tree here"]
    return True,None

def ShakeTree():
    if not TryShakeTree()[0]:
        return TryShakeTree()[1]
    messages = []
    r = random.random()
    if Inventario.GetEquipedWeapon() == None:
        if r < 0.1:
            r = random.random()
            if r < 0.5:
                Inventario.AddItem("Wood Sword",1)
                return ["You got a Wood sword"]
            else:
                Inventario.AddItem("Wood Shield",1)
                return ["You got a Wood shield"]
        elif r < 0.5:
            Inventario.AddItem("Vegetable",1)
            return ["You got an apple"]
        else:
            return ["The Tree didn't give you anythng"]
    else:
        player = Jugabilidad.GetPlayer()
        px = player["x"]
        py = player["y"]
        tree = Jugabilidad.AdjacentEntity(py,px,"Tree")
        tree["hits"] += 1
        if tree["hits"] >= 5:
            tree["hits"] = 0
            tree["name"] = "Broken Tree"
            tree["regen"] = 10
        if r < 0.2:
            Inventario.AddItem("Wood Sword",1)
            messages.append("You got a Wood sword")
        elif r < 0.4:
            Inventario.AddItem("Wood Shield",1)
            messages.append("You got a Wood shield")
        elif r < 0.8:
            Inventario.AddItem("Vegetable",1)
            messages.append("You got an apple")
        else:
            messages.append("The Tree didn't give you anythng")
        message = Inventario.UseWeapon()
        if message != None:
            messages.append(message)
        return messages

#Gespa

def TryCutGrass():
    if Inventario.GetEquipedWeapon() == None:
        return False,"No Weapon Equiped"
    player = Jugabilidad.GetPlayer()
    px = player["x"]
    py = player["y"]
    if Jugabilidad.TerrainAt(py,px) != " ":
        return False,None
    return True,None

def CutGrass():
    if not TryCutGrass()[0]:
        return TryCutGrass()[1] 
    r = random.random()
    if r < 1:
        Inventario.AddItem("Meat",1)
        return "You got a lizard"

