import MapSystem
import random
import Inventario
import Combate
import Guardado

#Pesca

fished = False

def TryFishing():
    playerIndex = MapSystem.GetPlayerIndex()
    px = MapSystem.GetEntityByIndex(playerIndex)["x"]
    py = MapSystem.GetEntityByIndex(playerIndex)["y"]
    if fished:
        return False,"You have already fished in this loacation"
    if not (MapSystem.AdjacentTerrain(py,px,"~") or  MapSystem.AdjacentTerrain(py,px,"-")):
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
    foxlist = MapSystem.GetAllEntiiesWithName("Fox",location=None)
    if len(foxlist) > 0:
        MapSystem.RemoveEntity(MapSystem.GetIndexOfEntity(foxlist[0]))
    if random.random() <= 0.5:
        if MapSystem.mapName == "Hyrule":
            MapSystem.AddEntity({"name" : "Fox" , "symbol" : "F", "x" : 50, "y" : 8})
        if MapSystem.mapName == "Death mountain":
            MapSystem.AddEntity({"name" : "Fox" , "symbol" : "F", "x" : 29, "y" : 1})
        if MapSystem.mapName == "Gerudo":
            MapSystem.AddEntity({"name" : "Fox" , "symbol" : "F", "x" : 47, "y" : 7})
        if MapSystem.mapName == "Necluda":
            MapSystem.AddEntity({"name" : "Fox" , "symbol" : "F", "x" : 5, "y" : 6})
        return "You see a Fox"
    else:
        return "You don't see a Fox"

#Cocinar

CookingIngredients =  {
    "Salad" : [["Vegetable",2]],
    "Pescatarian" : [["Fish",1],["Vegetable",1]],
    "Roasted" : [["Meat",1],["Vegetable",1]]
}

def TryCook(name):
    player = MapSystem.GetPlayer()
    px = player["x"]
    py = player["y"]
    if MapSystem.AdjacentEntity(py,px,"Cuina") == None:
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
    playerIndex = MapSystem.GetPlayerIndex()
    px = MapSystem.GetEntityByIndex(playerIndex)["x"]
    py = MapSystem.GetEntityByIndex(playerIndex)["y"]
    if MapSystem.AdjacentEntity(py,px,"Closed Chest") == None:
        if MapSystem.AdjacentEntity(py,px,"Open Chest") != None:
            return False, "This chest is already open"
        else:
            return False, "There isn't a closed chest here"
    return True,None

def OpenChest():
    if not TryOpenChest()[0]:
        return TryOpenChest()[1]
    playerIndex = MapSystem.GetPlayerIndex()
    px = MapSystem.GetEntityByIndex(playerIndex)["x"]
    py = MapSystem.GetEntityByIndex(playerIndex)["y"]
    chest = MapSystem.AdjacentEntity(py,px,"Closed Chest")
    Inventario.AddItem(chest["item"],1)
    chest["name"] = "Open Chest"
    chest["symbol"] = "W"
    return f"You got a {chest['item']}"

def RecloseChest():
    chests = MapSystem.GetAllEntiiesWithName("Open Chest")
    for chest in chests:
        chest["name"] = "Closed Chest"
        chest["symbol"] = "M"

#Sanctuary

def TryOpenSanctuary():
    player = MapSystem.GetPlayer()
    px = player["x"]
    py = player["y"]
    sanc = MapSystem.AdjacentEntity(py,px,"Sanctuary")
    if sanc == None:
        return False, "There isn't a sanctuary here"
    elif MapSystem.OpenSanctuaris[sanc["SanctuaryNumber"]] == True:
        return False, "You already opened this sanctuary"
    return True,None

def OpenSanctuary():
    if not TryOpenSanctuary()[0]:
        return TryOpenSanctuary()[1]
    player = MapSystem.GetPlayer()
    px = player["x"]
    py = player["y"]
    sanc = MapSystem.AdjacentEntity(py,px,"Sanctuary")
    MapSystem.OpenSanctuaris[sanc["SanctuaryNumber"]] = True
    Combate.PlayerMaxLife += 1
    Combate.PlayerLife += 1
    return "You opened the sanctuary"

#Tree

def TryShakeTree():
    player = MapSystem.GetPlayer()
    px = player["x"]
    py = player["y"]
    if MapSystem.AdjacentEntity(py,px,"Tree") == None:
        if MapSystem.AdjacentEntity(py,px,"Broken Tree") != None:
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
        player = MapSystem.GetPlayer()
        px = player["x"]
        py = player["y"]
        tree = MapSystem.AdjacentEntity(py,px,"Tree")
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
    player = MapSystem.GetPlayer()
    px = player["x"]
    py = player["y"]
    if MapSystem.TerrainAt(py,px) != " ":
        return False,None
    return True,None

def CutGrass():
    if not TryCutGrass()[0]:
        return TryCutGrass()[1] 
    r = random.random()
    if r < 0.1:
        Inventario.AddItem("Meat",1)
        return "You got a lizard"
    return "You cut the grass, but didn't get anything"

def TryEat(food_type):
    if food_type not in ["Vegetable","Salad","Pescatarian","Roasted"]:
        return False, f"{food_type} isn't comestible"
    if Inventario.inventario[food_type] != 0:
        if Combate.PlayerLife != Combate.PlayerMaxLife:
            return True, None
        else:
            return False, "You're not hungry now"
    else:
        return False, f"You don't have '{food_type}' to eat"

def Eat(food_type):
    if not TryEat(food_type)[0]:
        return TryEat(food_type)[1]
    Guardado.Saves[Guardado.ActiveSave]["FoodConsumed"][food_type] += 1
    if food_type == "Vegetable":
        Combate.PlayerLife += 1
    if food_type == "Salad":
        Combate.PlayerLife += 2
    if food_type == "Pescatarian":
        Combate.PlayerLife += 3
    if food_type == "Roasted":
        Combate.PlayerLife += 4
    Inventario.inventario[food_type] -= 1
    if Combate.PlayerLife > Combate.PlayerMaxLife:
        Combate.PlayerLife = Combate.PlayerMaxLife
    return f"You ate a {food_type.capitalize()}"
