import Inventario
import Interaccion
import Combate
import MapSystem
import random
import Guardado

def makeCheat(args):
    if len(args) == 0:
        return "Cheating: No cheat specified"
    if args[0] == "rename":
        return renamePlayer(args[1])
    elif args[0] == "add":
        return AddItem(" ".join(args[1:]).title())
    elif args[0] == "cook":
        return cookFood(args[1].title())
    elif args[0] == "open":
        return OpenSanctuaris()
    elif args[0] == "game":
        return GameOver()
    elif args[0] == "win":
        return WinGame()
    else:
        return "Cheating: That is not a cheat"

def AddItem(item):
    if item in ["Sword", "Shield", "Wood Sword", "Wood Shield", "Vegetable", "Meat", "Fish", "Roasted", "Pescatarian", "Salad"]:
        Inventario.AddItem(item,1)
        return f"Cheating: cheat add {item}"
    else:
        return "Cheating: Invalid item"
    

def cookFood(food):
    if food not in ["Salad","Roasted","Pescatarian"]:
        return "Cheating: That is not a food"
    if food not in Interaccion.CookingIngredients:
        return "CheatingThis recipe doesn't exist"
    insuficientIngredients = []
    for ingridient in Interaccion.CookingIngredients[food]:
        if Inventario.GetItem(ingridient[0]) < ingridient[1]:
            insuficientIngredients.append(ingridient[0])
    if len(insuficientIngredients) > 0:
        return "You don't have enough "+" and ".join(insuficientIngredients)
    for ingridient in Interaccion.CookingIngredients[food]:
        Inventario.RemoveItem(ingridient[0],ingridient[1])
    Inventario.AddItem(food,1)
    return f"Cheating: cheat cook {food}"
    
def ValidName(name):
    if len(name) < 3 or len(name) > 10:
        return False
    for c in name:
        if not c.isalnum() and c != " ":
            return False
    return True

def renamePlayer(NewName):
    if not ValidName(NewName):
        return "Cheating: That is not a valid name"
    Guardado.Saves[Guardado.ActiveSave]["PlayerName"] = NewName
    return f"Cheating: cheat rename {NewName}"
    
def OpenSanctuaris():
    MapSystem.OpenSanctuaris = [True,True,True,True,True,True,True]
    Combate.PlayerLife = 9
    Combate.PlayerMaxLife = 9
    return "Cheating: Cheat open sanctuaris"

def GameOver():
    Combate.PlayerLife = 0
    return "Cheating: Cheat game over"

def WinGame():
    Ganon = MapSystem.GetAllEntiiesWithName("Ganon")
    #Posar la entitat de Ganon en una posició aleatòria si no esta.
    if len(Ganon) == 0:
        entity = {"name":"Ganon","x":0,"y":0,"symbol": " "}
        while MapSystem.IsBlocked(entity["y"],entity["x"]):
            entity["y"] = random.randint(0,len(MapSystem.map)-1)
            entity["x"] = random.randint(0,len(MapSystem.map[0])-1)
        MapSystem.AddEntity(entity)
    #Quitar todos los GanonHearts si hay
    Hearts = MapSystem.GetAllEntiiesWithName("GanonHeart")
    for heart in Hearts:
        MapSystem.RemoveEntity(MapSystem.GetIndexOfEntity(heart))
    return "Cheating: Cheat win game"

