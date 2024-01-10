import Guardado
import Inventario
import Combate
import Jugabilidad

def InitializeNewGame(PlayerName):
    #Consigue un Guardado base
    save = Guardado.NewSave(PlayerName)
    #Consigue una GameId para el Guardado
    GameId = Guardado.GetNewGameId()
    #Guarda el Guardado en el diccionario local y en la base de datos
    Guardado[GameId] = save
    Guardado.NewDBSave(PlayerName, GameId)
    #Inicializa los sistemas de juego
    Inventario.InvenroryInit()
    Jugabilidad.InitMap()
    Combate.InitCombate()
    Guardado.ActiveSave = GameId
    return GameId

def LoadSavedGame(GameId):
    Inventario.InvenroryInit(invetoryInfo=Guardado.GetInventoryInfo(GameId))
    Jugabilidad.InitMap(MapInfo=Guardado.GetMapInfo(GameId))
    Combate.InitCombate(CombateInfo=Guardado.GetCombateInfo(GameId))
    Guardado.ActiveSave = GameId