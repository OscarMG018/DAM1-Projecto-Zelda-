import Inventario
import Interaccion
import Combate
import Jugabilidad
import random
import Guardado

def makeCheat(args):
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
    succes,message = Interaccion.TryCook(food)
    if succes:
        return f"Cheating: cheat cook {food}"
    else:
        return "Cheating: " + message
    
def ValidName(name):
    if len(name) < 3 or len(name) > 20:
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
    Jugabilidad.OpenSanctuaris = [True,True,True,True,True,True,True]
    Combate.PlayerLife = 9
    Combate.PlayerMaxLife = 9
    return "Cheating: Cheat open sanctuaris"

def GameOver():
    Combate.PlayerCurrentLife = 0
    return "Cheating: Cheat game over"

def WinGame():
    Ganon = Jugabilidad.GetAllEntiiesWithName("Ganon")
    #Posar la entitat de Ganon en una posició aleatòria si no esta.
    if len(Ganon) == 0:
        entity = {"name":"Ganon","x":0,"y":0,"symbol": " "}
        while Jugabilidad.IsBlocked(entity["y"],entity["x"]):
            entity["y"] = random.randint(0,len(Jugabilidad.map)-1)
            entity["x"] = random.randint(0,len(Jugabilidad.map[0])-1)
        Jugabilidad.AddEntity(entity)
    #Quitar todos los GanonHearts si hay
    Hearts = Jugabilidad.GetAllEntiiesWithName("GanonHeart")
    for heart in Hearts:
        Jugabilidad.RemoveEntity(Jugabilidad.GetIndexOfEntity(heart))
    return "Cheating: Cheat win game"

