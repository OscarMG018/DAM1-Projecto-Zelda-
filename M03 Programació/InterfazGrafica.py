import Guardado
import Inventario
import Combate
import Jugabilidad
import platform
import os
import Interaccion
from menuprincipal.ascii_draws_chosen import draw_chosen
from datetime import datetime
import copy

PlayerName = ""

#Funciones de utilidad
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

prompts_list = []

def AddToPropmts(message):
    if len(prompts_list) >= 8:
        prompts_list.pop(0)
        prompts_list.append("> " + message)
    else:
        prompts_list.append("> " + message)

#Concatena str1 y str2 en forma horizontal, linea por linea
def concathorizontal(str1,str2):
    lines1 = str1.split('\n')
    lines2 = str2.split('\n')

    while len(lines1) < len(lines2):
        lines1.append('')
    while len(lines2) < len(lines1):
        lines2.append('')

    # Concatenate corresponding lines from both lists
    result = [line1 + line2 for line1, line2 in zip(lines1, lines2)]

    return '\n'.join(result)

#rjust mdificado para soportar "* ", str.rjust solo soporta fillcharapter de len 1
def rjust(input_string, width, fillchar):
    fill_len = len(fillchar)
    if width <= len(input_string):
        return input_string
    else:
        fill_num = (width - len(input_string)) // fill_len
        remainder = (width - len(input_string)) % fill_len
        return input_string + fillchar * fill_num + fillchar[:remainder]

# La función 'printWithFrame' toma un contenido de texto y lo enmarca con asteriscos.
# También permite la inclusión de menús en las esquinas del marco. 1 TopLeft, 2 BottomLeft,
# Los parámetros 'skipLeft' y 'skipRight' permiten omitir la adición del borde a la izquierda y a la derecha, respectivamente.
# El parámetro 'Menus' es una lista de tuplas, donde cada tupla contiene el nombre del menú y su posición
def WithFrame(content,Menus=[],skipLeft=False,skipRight=False):
    lines = content.split('\n')
    width = -1
    for line in lines:
        width = max(width, len(line))
    
    if (skipLeft):
        top = " "
    else:
        top = "* "
    MenusTL = list(filter(lambda x: x[1] == 1,Menus))
    MenuWidth = 0
    for i in range(len(MenusTL)):
        top += MenusTL[i][0]
        if i < len(MenusTL)-1:
            MenuWidth += len(MenusTL[i][0]) + 2
            top += ", "
        else:
            MenuWidth += len(MenusTL[i][0]) + 1
            top += " "
            if (MenuWidth % 2 != 0 and width % 2 != 0) or (MenuWidth % 2 == 0 and width % 2 == 0):
                top += " "
    top = rjust(top,width,"* ") 
    if not skipRight:
        top += " *"
    
    middle = ""
    for i in range(len(lines)):
        line = ""
        if (skipLeft):
            line += lines[i]
        else:
            line += "*" + lines[i]
        if not skipRight:
            line = line.ljust(width) + "*"
        if i < len(lines)-1:
            line += "\n"
        middle += line


    if (skipLeft):
        bottom = " "
    else:
        bottom = "* "
    MenusBL = list(filter(lambda x: x[1] == 2,Menus))
    MenuWidth = 0
    for i in range(len(MenusBL)):
        bottom += MenusBL[i][0]
        if i < len(MenusBL)-1:
            MenuWidth += len(MenusBL[i][0]) + 2
            bottom += ", "
        else:
            MenuWidth += len(MenusBL[i][0]) + 1
            bottom += " "
            if (MenuWidth % 2 != 0 and width % 2 != 0) or (MenuWidth % 2 == 0 and width % 2 == 0):
                bottom += " "
    bottom = rjust(bottom,width,"* ") 
    
    if not skipRight:
        bottom += " *"

    return top + "\n" + middle + "\n" + bottom

def parse_input(input):
    parts = input.split()
    if len(parts) == 0:
        return None, None
    command = parts[0]
    args = parts[1:]
    return command, args


def InitializeNewGame(playerName):
    global PlayerName
    #Consigue un Guardado base
    save = Guardado.NewSave(playerName)
    #Consigue una GameId para el Guardado
    GameId = Guardado.GetNewGameId()
    #Guarda el Guardado en el diccionario local y en la base de datos
    Guardado.Saves[GameId] = save
    Guardado.NewDBSave(playerName, GameId)
    #Inicializa los sistemas de juego
    Inventario.InvenroryInit()
    Jugabilidad.InitMap()
    Combate.InitCombate()
    PlayerName = playerName
    Guardado.ActiveSave = GameId
    return GameId

def LoadSavedGame(GameId):
    global PlayerName
    Inventario.InvenroryInit(invetoryInfo=Guardado.GetInventoryInfo(GameId))
    Jugabilidad.InitMap(MapInfo=Guardado.GetMapInfo(GameId))
    Combate.InitCombate(CombateInfo=Guardado.GetCombateInfo(GameId))
    Guardado.ActiveSave = GameId
    PlayerName = Guardado.Saves[GameId]["PlayerName"]
    return Guardado.Saves[GameId]["LastLocation"]


def main_menu():
    # Imprimir el marco superior
    print("* " * 40)

    # Imprimir el contenido del dibujo con los marcos laterales
    for line in draw_chosen:
        print("*" + line.rjust(77) + "*")

    # Comprobar si hay una partida guardada e imprimir opciones del menú según
    if len(Guardado.Saves) == 0:
        print("* New Game, BDdata, Help, About, Exit " + ("* " * 25))
    else:
        print("* Continue, New Game, BDdata, Help, About, Exit " + ("* " * 20))

def new_game_menu_help():
    print(
"""* Help, new game  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                             *
*                                                                             *
*          When asked, type your name and press enter                         *
*          if 'Link' is fine for you, just press enter                        *
*                                                                             *
*          Name must be between 3 and 10 characters long and only             *
*          letters, numbers and spaces are allowed                            *
*                                                                             *
*          Type 'back' now to go back to 'Set your name'                      *
*                                                                             *
* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")
    return ["back"]

def new_game_menu():
    print(
"""* New game  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                             *
*                                                                             *
*                                                                             *
*                                                                             *
*          Set your name ?                                                    *
*                                                                             *
*                                                                             *
*                                                                             *
*          Type 'back' now to go back to the 'Main menu'                      *
*                                                                             *
* Back, Help  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")
    return ["back", "help"]

def help_menu():
    print(
"""* Help, main menu * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                             *
*                                                                             *
* Type 'continue' to continue a saved game                                    *
* Type 'new game' to start a new game                                         *
* Type 'about' to see information about the game                              *
* Type 'exit' to exit the game                                                *
*                                                                             *
*                                                                             *
* Type 'back' now to go back to the 'Main menu'                               *
*                                                                             *
* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")

def about_menu():
    print(
"""* About * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                             *
*         Game developed by ‘Team 2, The hometown bugs’ :                     *
*                                                                             *
*                                                                             *
*              Allan Turing                                                   *
*              Steve Jobs                                                     *
*              Linus Torvalds                                                 *
*                                                                             *
*         Type 'back' now to go back to the 'Main menu'                       *
*                                                                             *
* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
""")
    return "back"

def Plot():
    return """* Plot * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                            *
*                                                                            *
*   Now history is repeating itself, and Princess Zelda has been captured by *
*   Ganon. He has taken over the Guardians and filled Hyrule with monsters.  *
*                                                                            *
*                                                                            *
*   But a young man named 'Link' has just awakened and                       *
*   must reclaim the Guardians to defeat Ganon and save Hyrule.              *
*                                                                            *
*                                                                            *
* Continue * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"""

def Legend():
    return """* Legend * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*   10,000 years ago, Hyrule was a land of prosperity thanks to the Sheikah  *
*   tribe. The Sheikah were a tribe of warriors who protected the Triforce,  *
*   a sacred relic that granted wishes.                                      *
*                                                                            *
*   But one day, Ganondorf, an evil sorcerer, stole the Triforce and began   *
*   to rule Hyrule with an iron fist.                                        *
*                                                                            *
*   The princess, with the help of a heroic young man, managed to defeat     *
*   Ganondorf and recover the Triforce.                                      *
*                                                                            *
* Continue * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"""

def saved_games_menu():
    result = "* Saved games * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n"
    result += "*                                                                             *\n"
    copia = copy.deepcopy(list(Guardado.Saves.values()))
    copia.sort(key=lambda x: x["SaveDate"], reverse=True)
    for i, save in enumerate(copia):
        result += f'*  {i}: {save["SaveDate"]} - {save["PlayerName"]}, {save["LastLocation"]}'.ljust(72)+f'♥ {save["PlayerLife"]}/{save["PlayerMaxLife"]} *\n'
    for i in range(len(Guardado.Saves),9):
        result += "*                                                                             *\n"
    result += "* Play X, Erase X, Help, Back * * * * * * * * * * * * * * * * * * * * * * * * *"
    print(result)

def saved_games_menu_help():
    print("""* Help, saved games * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                             *
*                                                                             *
*       Type 'play X' to continue playing the game 'X'                        *
*       Type 'erase X' to erase the game 'X'                                  *
*       Type 'back' now to go back to the main menu                           *
*                                                                             *
*                                                                             *
*                                                                             *
*       Type 'back' now to go back to 'Saved games'                           *
*                                                                             *
* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *""")

def InventoryHelp():
    return """* Help, inventory * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*       Type 'show inventory main' to show the main inventory                 *
*       (main, weapons, Food)                                                 *
*       Type 'eat X' to eat X, where X is a Food item                         *
*       Type 'Cook X' to Cook X, where X is a Food item                       *
*       Type 'equip X' to equip X, where X is a weapon                        *
*       Type 'unequip X' to unequip X, where X is a weapon                    *
*       Type 'back' now to go back to the 'Game'                              *
* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"""

def InventoryMain():
    result = " * * * * Inventory *" + "\n"
    result += "                   *" + "\n"
    result += f" {PlayerName}" + f"♥ {Combate.PlayerLife}/{Combate.PlayerMaxLife} *".rjust(19-len(PlayerName)," ") + "\n"
    result += " Blood Moon in " + f"{25-Combate.BloodMoon} *".rjust(5," ") + "\n"
    result += "                   *" + "\n"
    result += " Equipment         *" + "\n"
    result += f"{Inventario.GetEquipedWeapon()} *".rjust(20," ") + "\n"
    result += f"{Inventario.GetEquipedShield()} *".rjust(20," ") + "\n"
    result += "                   *" + "\n"
    food = Inventario.GetItem("Vegetable")+Inventario.GetItem("Salad")+Inventario.GetItem("Pescatarian")+Inventario.GetItem("Roasted")
    result += " Food" + f"{food} *".rjust(15," ") + "\n"
    weapons = Inventario.GetItem("Sword")[1]+Inventario.GetItem("Wood Sword")[1]+Inventario.GetItem("Shield")[1]+Inventario.GetItem("Wood Shield")[1]
    result += " Weapons" + f"{weapons} *".rjust(12," ") + "\n"
    result += " * * * * * * * * * *" + "\n"
    return result

def InventoryWeapons():
    result = " * * * * * Weapons *" + "\n"
    result += "                   *" + "\n"
    result += "                   *" + "\n"
    result += "Wood Sword" +f"{Inventario.GetItem('Wood Sword')[0]}/{Inventario.GetItem('Wood Sword')[1]} *".rjust(10," ") + "\n"
    if Inventario.GetEquipedWeapon() == "Wood Sword":
        result += "  (equiped)        *" + "\n"
    else:
        result += "                   *" + "\n"
    result += "Sword" +f"{Inventario.GetItem('Sword')[0]}/{Inventario.GetItem('Sword')[1]} *".rjust(15," ") + "\n"
    if Inventario.GetEquipedWeapon() == "Sword":
        result += "  (equiped)        *" + "\n"
    else:
        result += "                   *" + "\n"
    result += "Wood Shield" +f"{Inventario.GetItem('Wood Shield')[0]}/{Inventario.GetItem('Wood Shield')[1]} *".rjust(9," ") + "\n"
    if Inventario.GetEquipedWeapon() == "Wood Shield":
        result += "  (equiped)        *" + "\n"
    else:
        result += "                   *" + "\n"
    result += "Shield" +f"{Inventario.GetItem('Shield')[0]}/{Inventario.GetItem('Shield')[1]} *".rjust(14," ") + "\n"
    if Inventario.GetEquipedWeapon() == "Shield":
        result += "  (equiped)        *" + "\n"
    else:
        result += "                   *" + "\n"
    result += " * * * * * * * * * *" + "\n"
    return result

def InventoryFood():
    result = " * * * * * *  Food *" + "\n"
    result += "                   *" + "\n"
    result += "                   *" + "\n"
    result += " Vegetable" +f"{Inventario.GetItem('Vegetable')} *".rjust(10," ") + "\n"
    result += " Fish" +f"{Inventario.GetItem('Fish')} *".rjust(15," ") + "\n"
    result += " Meat" +f"{Inventario.GetItem('Meat')} *".rjust(15," ") + "\n"
    result += "                   *" + "\n"
    result += " Salad" +f"{Inventario.GetItem('Salad')} *".rjust(14," ") + "\n"
    result += " Pescatarian" +f"{Inventario.GetItem('Pescatarian')} *".rjust(8," ") + "\n"
    result += " Roasted" +f"{Inventario.GetItem('Roasted')} *".rjust(12," ") + "\n"
    result += "                   *" + "\n"
    result += " * * * * * * * * * *" + "\n"
    return result

def GameOver():
 return """* Link death * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                                             *
*                                                                             *
*                                                                             *
*                                                                             *
*       Game Over.                                                            *
*                                                                             *
*                                                                             *
*                                                                             *
*                                                                             *
*                                                                             *
* Continue  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"""

def ZeldaSaved():
    return """* Zelda saved * * * * * * * * * * * * * * * * * * * * * * * * * * * * *a * * * *
*                                                                             *
*                                                                             *
*                                                                             *
*                                                                             *
*       Congratulations, Link has saved Princess Zelda.                       *
*       Thanks for playing!                                                   *
*                                                                             *
*                                                                             *
*                                                                             *
*                                                                             *
* Continue  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"""


def dbdata_help():
    result = "* DBdara, Help * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *" + "\n"
    result += "* Help, Players, Player Activity, Weapons, Food, Blood Moons  * * * * * * * * *"
    print(result)

def dbdata_players():
    result = "* DBdara, Players * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *" + "\n"
    result += "*                                                                             *\n"
    for saveId, save in Guardado.Saves.items():
        result += f"* {save['PlayerName']}" + f"{save['SaveDate']}".rjust(75-len(save["PlayerName"])," ") +" *" + "\n"
    for i in range(len(Guardado.Saves),9):
        result += "*                                                                             *\n"
    result += "*                                                                             *\n"
    result += "* Help, Players, Player Activity, Weapons, Food, Blood Moons  * * * * * * * * *"
    print(result)
    
def dbdata_player_activity():
    result = "* DBdara, Player Activity * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"

def dbdata_weapons():
    result = "* DBdara, Weapons * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"

def dbdata_food():
    result = "* DBdara, Food * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"

def dbdata_blood_moons():
    result = "* DBdara, Blood Moons * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"

def MainMenuAction(action):
    if action == "new game":
        AddToPropmts(action)
        NewGameMenu()
    elif action == "dbdata":
        AddToPropmts(action)
        DBdataMenu()
    elif action == "help":
        AddToPropmts(action)
        HelpMenu()
    elif action == "about":
        AddToPropmts(action)
        AboutMenu()
    elif action == "exit":
        AddToPropmts(action)
        return "Exit"
    elif action == "continue":
        if len(Guardado.Saves) == 0:
            AddToPropmts("Invalid Action")
        elif len(Guardado.Saves) == 1:
            AddToPropmts(action)
            LastLocation = LoadSavedGame(list(Guardado.Saves.keys())[0])
            MapMenu(LastLocation)
        else:
            AddToPropmts(action)
            SavedGamesMenu()
    else:
        AddToPropmts("Invalid Action")

def MainMenu():
    while(True):
        clear_screen()
        main_menu()
        print("\n## Last Prompts ##")
        for p in prompts_list:
            print(p)
        print("- - - - -\nWhat to do now?")
        action = input("> ").lower()
        if MainMenuAction(action) == "Exit":
            break

def DBdataMenu():
    datashowing = "help"
    while(True):
        clear_screen()
        if datashowing == "help":
            dbdata_help()
        elif datashowing == "players":
            dbdata_players()
        elif datashowing == "player activity":
            dbdata_player_activity()
        elif datashowing == "weapons":
            dbdata_weapons()
        elif datashowing == "food":
            dbdata_food()
        elif datashowing == "blood moons":
            dbdata_blood_moons()
        print("\n## Last Prompts ##")
        for p in prompts_list:
            print(p)
        print("- - - - -\nWhat to do now?")
        action = input("> ").lower()
        if action == "back":
            AddToPropmts(action)
            break
        elif action in ["help","players","player activity","weapons","food","blood moons"]:
            AddToPropmts(action)
            datashowing = action

def HelpMenu():
    while(True):
        clear_screen()
        help_menu()
        print("\n## Last Prompts ##")
        for p in prompts_list:
            print(p)
        print("- - - - -\nWhat to do now?")
        action = input("> ").lower()
        if action == "back":
            AddToPropmts(action)
            break
        else:
            AddToPropmts("Invalid Action")

def AboutMenu():
    while(True):
        clear_screen()
        about_menu()
        print("\n## Last Prompts ##")
        for p in prompts_list:
            print(p)
        print("- - - - -\nWhat to do now?")
        action = input("> ").lower()
        if action == "back":
            AddToPropmts(action)
            break
        else:
            AddToPropmts("Invalid Action")

def ValidName(name):
    if len(name) < 3 or len(name) > 20:
        return False
    for c in name:
        if not c.isalnum() and c != " ":
            return False
    return True

def NewGameMenu():
    while(True):
        clear_screen()
        new_game_menu()
        print("\n## Last Prompts ##")
        for p in prompts_list:
            print(p)
        print("- - - - -\nWhat's your name (Link)?")
        action = input("> ").lower()
        if action == "back":
            AddToPropmts(action)
            break
        elif action == "help":
            AddToPropmts(action)
            NewGameMenuHelp()
        else:
            if ValidName(action):
                AddToPropmts(f"Welcome to the game,{action}")
                LegendPlotMenu(action)
                break
            else:
                AddToPropmts(f"{action} is not a valid name")

def NewGameMenuHelp():
    while(True):
        clear_screen()
        new_game_menu_help()
        print("\n## Last Prompts ##")
        for p in prompts_list:
            print(p)
        print("- - - - -\nWhat to do now?")
        action = input("> ").lower()
        if action == "back":
            AddToPropmts(action)
            LegendPlotMenu(action)
            break
        else:
            AddToPropmts("Invalid Action")

def SavedGamesMenuAction(command,args):
    if command == "play":
        if len(args) == 0 or len(args) > 1:
            AddToPropmts("Invalid action")
        elif not args[0].isdigit():
            AddToPropmts("Invalid action")
        else:
            index = Guardado.GetSavedGameId(int(args[0]))
            AddToPropmts(str(index))
            if Guardado.Saves.get(index) == None:
                AddToPropmts("Invalid action")
            else:
                LastLocation = LoadSavedGame(index)
                MapMenu(LastLocation)
                return "back"
    elif command == "erase":
        if len(args) == 0 or len(args) > 1:
            AddToPropmts("Invalid action")
        elif not args[0].isdigit():
            AddToPropmts("Invalid action")
        else:
            index = Guardado.GetSavedGameId(int(args[0]))
            if Guardado.Saves.get(index) == None:
                AddToPropmts("Invalid action")
            else:
                AddToPropmts(str(index))
                Guardado.DeleteSaveFromDB(index)
                del Guardado.Saves[index]
    elif command == "help":
        SavedGamesMenuHelp()
    elif command == "back":
        return "back"
    else:
        AddToPropmts("Invalid action")

def SavedGamesMenu():
    while(len(Guardado.Saves) > 0):
        clear_screen()
        saved_games_menu()
        print("\n## Last Prompts ##")
        for p in prompts_list:
            print(p)
        print("- - - - -\nWhat to do now?")
        action = input("> ").lower()
        command,args = parse_input(action)
        if SavedGamesMenuAction(command,args) == "back":
            break

def SavedGamesMenuHelp():
    while(True):
        clear_screen()
        saved_games_menu_help()
        for p in prompts_list:
            print(p)
        print("- - - - -\nWhat to do now?")
        new_prompt = input("> ").lower()
        if new_prompt == "back":
            break
        else:
            prompts_list.append("> Invalid Action")
    clear_screen()

def LegendPlotMenu(PlayerName):
    while(True):
        clear_screen()
        print(Legend())
        if len(prompts_list) > 8:
            del prompts_list[0]
        print("\n## Last Prompts ##")
        for prompt in prompts_list:
            print(prompt)
        print("- - - - -\nWhat do you want to do next?")
        new_prompt = input("> ").lower()
        if new_prompt == "continue":
            break
        else:
            prompts_list.append("> Invalid Action")
    while(True):
        clear_screen()
        print(Plot())
        if len(prompts_list) > 8:
            del prompts_list[0]
        print("\n## Last Prompts ##")
        for prompt in prompts_list:
            print(prompt)
        print("- - - - -\nWhat do you want to do next?")
        new_prompt = input("> ").lower()
        if new_prompt == "continue":
            break
        else:
            prompts_list.append("> Invalid Action")
    InitializeNewGame(PlayerName)
    MapMenu("Hyrule")

mapConnections = {
    "Hyrule" : ["Gerudo","Death mountain","Castle"],
    "Gerudo" : ["Hyrule","Necluda","Castle"],
    "Death mountain" : ["Hyrule","Necluda","Castle"],
    "Necluda" : ["Gerudo","Death mountain","Castle"],
    "Castle" : []
}

def WorldMap():
    result = "* Map * * * * * * * * * * * * * * * * * * * * * * * * * * *" + "\n"
    result += "*                                                         *" + "\n"
    result += "*  Hyrule       " + "S0" + "?"*(not Jugabilidad.OpenSanctuaris[0]) + " "* Jugabilidad.OpenSanctuaris[0] +" "*23+"Death Mountain  *" + "\n"
    result += "*"+" "*30 + "S2" + "?"*(not Jugabilidad.OpenSanctuaris[2]) + " "* Jugabilidad.OpenSanctuaris[2] + " "*24+"*" + "\n"
    result += "*"+" "*8 + "S1" + "?"*(not Jugabilidad.OpenSanctuaris[1]) + " "* Jugabilidad.OpenSanctuaris[1] +" "*39 + "S3" + "?"*(not Jugabilidad.OpenSanctuaris[3]) + " "* Jugabilidad.OpenSanctuaris[3] + " "*4+ "*" +"\n"
    result += "*                                                         *" + "\n"
    result += "*"+"Castle".center(57," ") +"*"+"\n"
    result += "*                                                         *" + "\n"
    result += "*" +" "*17 + "S4" + "?"*(not Jugabilidad.OpenSanctuaris[4]) + " "* Jugabilidad.OpenSanctuaris[4]+" "*32 + "S5" + "?"*(not Jugabilidad.OpenSanctuaris[5]) + " "* Jugabilidad.OpenSanctuaris[5] +"  *" + "\n"
    result += "*  Gerudo" + " "*31 + "S6" + "?"*(not Jugabilidad.OpenSanctuaris[6]) + " "* Jugabilidad.OpenSanctuaris[6] + " "*6 + "Necluda  *" + "\n"
    result += "*                                                         *" + "\n"
    result += "* Back  * * * * * * * * * * * * * * * * * * * * * * * * * *" + "\n"
    return result

def WorldMapMenu():
    while(True):
        clear_screen()
        print(WorldMap())
        print("\n## Last Prompts ##")
        for p in prompts_list:
            print(p)
        print("- - - - -\nWhat to do now?")
        action = input("> ").lower()
        if action == "back":
            break
        else:
            AddToPropmts("Invalid Action")

def InventoryHelpMenu():
    while(True):
        clear_screen()
        print(InventoryHelp())
        action = input("type Back to go back:  ")
        if action == "Back":
            break

def GetInventory():
    global invetoryToShow
    if invetoryToShow == "main":
        return InventoryMain()
    elif invetoryToShow == "weapons":
        return InventoryWeapons()
    elif invetoryToShow == "food":
        return InventoryFood()
    else:
        return "Error"

def ActionsAvailables():
    actions = [["Exit",2],["Go",2],["Equip",2],["Unequip",2]]
    if Jugabilidad.mapName == "Castle":
        if Interaccion.TryCutGrass()[0] or Interaccion.TryCutTree()[0] or Combate.TryAttackGanon():
            actions.insert(1,["Attack",2])
    else:
        if Combate.tryattack()[0] or Interaccion.TryCutGrass()[0] or Interaccion.TryShakeTree()[0]:
            actions.insert(1,["Attack",2])
        if Inventario.GetItem("Vegetable")+Inventario.GetItem("Salad")+Inventario.GetItem("Pescatarian")+Inventario.GetItem("Roasted") > 0:
            actions.append(["Eat",2])
        for cookable,ingredients in Interaccion.CookingIngredients.items():
            if Interaccion.TryCook(cookable)[0]:
                actions.append(["Cook",2])
                break
        if Interaccion.TryFishing()[0]:
            actions.append(["Fish",2])
        if Interaccion.TryOpenChest()[0] or Interaccion.TryOpenSanctuary()[0]:
            actions.append(["Open",2])
    actions.append(["Show",2])
    return actions


def ExecuteMapAction(command,args):
    if command == None:
        AddToPropmts("Invalid action")
        return
    command = command.lower()
    if command == "go":
        if args[0].isdigit():
            if len(args) != 2:
                AddToPropmts("Invalid action")
            number = int(args[0])
            direction = args[1].lower()
            if direction == "up":
                message = Jugabilidad.MovePlayerBy(1*number, 0)
                if message != None:
                    AddToPropmts(message)
                ActionTime()
            elif direction == "down":
                message = Jugabilidad.MovePlayerBy(-1*number, 0)
                if message != None:
                    AddToPropmts(message)
                ActionTime()
            elif direction == "left":
                message = Jugabilidad.MovePlayerBy(0, -1*number)
                if message != None:
                    AddToPropmts(message)
                ActionTime()
            elif direction == "right":
                message = Jugabilidad.MovePlayerBy(0, 1*number)
                if message != None:
                    AddToPropmts(message)
                ActionTime()
            else:
                AddToPropmts("That is not a direction")
            if Jugabilidad.mapName == "Castle" and Combate.InFrontOfGanon():
                AddToPropmts("Ganon's presence hurts you")
                Combate.PlayerLife -= 1
        elif args[0].lower() == "by" and args[1].lower() == "the":
            if args[2].lower() == "water":
                message = Jugabilidad.MovePlayerNearTerrain("~")
                if message == "You can't go to ~ from here":
                    AddToPropmts(message)
                    ActionTime()
                elif message != "":
                    AddToPropmts(message)
                else:
                    ActionTime()
            else:
                if len(args[2]) == 1:
                    message = Jugabilidad.MovePlayerNearEntity("symbol",args[2])
                    if message == f"You can't go to {args[2]} from here":
                        AddToPropmts(message)
                        ActionTime()
                    elif message != "":
                        AddToPropmts(message)
                    else:
                        ActionTime()
                elif args[2][0] == "S":
                    message = Jugabilidad.MovePlayerNearEntity("SanctuaryNumber",int(args[2][1:]))
                    if message == f"You can't go to {args[2][1:]} from here":
                        AddToPropmts(f"You can't go to {args[2]} from here")
                        ActionTime()
                    elif message != "":
                        AddToPropmts(message)
                    else:
                        ActionTime()
                else:
                    AddToPropmts("That is not in this location")
        elif args[0] == "to":
            mapname = (" ".join(args[1:])).capitalize()
            " ".capitalize()
            if Jugabilidad.mapName == mapname:
                AddToPropmts("You are already in that location")

            elif Jugabilidad.maps.get(mapname) == None:
                AddToPropmts("That is not a location")

            elif Jugabilidad.mapName == "Castle":
                AddToPropmts("To exit the castle type \"Back\"")

            elif mapname not in mapConnections[Jugabilidad.mapName]:
                AddToPropmts("You can't go to that location from here")

            else:
                Jugabilidad.LoadMap(mapname)
                message = Interaccion.DecideFoxVisibility()
                AddToPropmts(f"You are now in {mapname}")
                Interaccion.fished = False
                if message != None:
                    AddToPropmts(message)
                ActionTime()
                SaveData()
        else:
            AddToPropmts("Invalid action")
    elif command == "fish":
        if len(args) != 0:
            AddToPropmts("Invalid action")
        message = Interaccion.Fishing()
        AddToPropmts(message)   
        if message == "You Get A Fish" or message == "You don't Get A Fish":
            SaveData()
            ActionTime()
    elif command == "open":
        if len(args) != 1:
            AddToPropmts("Invalid action")
        if args[0].lower() == "chest":
            message = Interaccion.OpenChest()
            AddToPropmts(message)
            if message[0] == "Y":
                SaveData()
                ActionTime()
        elif args[0].lower() == "sanctuary":
            message = Interaccion.OpenSanctuary()
            if message[4] != "o":
                AddToPropmts(message)
            else:
                SaveData()
                ActionTime()
    elif command == "show":
        if len(args) > 2:
            AddToPropmts("Invalid action")
        if args[0].lower() == "inventory":
            if args[1].lower() in ["main","weapons","food"]:
                global invetoryToShow
                invetoryToShow = args[1]
            elif args[1].lower() == "help":
                InventoryHelpMenu()
            else:
                AddToPropmts("Invalid action")
        elif args[0].lower() == "map":
            WorldMapMenu()
        else:
            AddToPropmts("Invalid action")
    elif command == "cook":
        if len(args) != 1:
            AddToPropmts("Invalid action")
            return
        message = Interaccion.Cook(args[0].capitalize())
        if message != f"You cooked a {args[0].capitalize()}":
            AddToPropmts(message)
            ActionTime()
            SaveData()            
    elif command == "attack":
        player = Jugabilidad.GetPlayer()
        px = player["x"]
        py = player["y"]
        if Jugabilidad.AdjacentEntity(py,px,"Tree") != None or Jugabilidad.AdjacentEntity(py,px,"Broken Tree") != None:
            messages = Interaccion.ShakeTree()
            for message in messages:
                AddToPropmts(message)
            if messages[0][0] == "Y":
                ActionTime()
                SaveData()
            elif messages[0] == "The Tree didn't give you anythng":
                ActionTime()
        elif Jugabilidad.AdjacentEntity(py,px,"Fox") != None or Jugabilidad.AdjacentEntity(py,px,"Enemy") != None:
            if len(args) != 0:
                AddToPropmts("Invalid action")
                return
            messages = Combate.attack()
            for message in messages:
                AddToPropmts(message)
            if not(len(messages) == 1 and messages[0] == "No hay entidades cercanas para atacar."):
                ActionTime()
                SaveData()
        elif Jugabilidad.AdjacentEntity(py,px,"Ganon") != None:
            messages = Combate.attackGanon()
            for message in messages:
                AddToPropmts(message)
            if len(messages) > 1:
                ActionTime()
                SaveData()
            elif messages[0] != "No hay armas equipadas para atacar." or messages[0] != "Ganon is out of range":
                ActionTime()
                SaveData()
        elif Jugabilidad.TerrainAt(py,px) == " ":
            message = Interaccion.CutGrass()
            if message != None:
                AddToPropmts(message)
            if message != "No Weapon Equiped":
                ActionTime()
                SaveData()
    elif command == "equip":
        if len(args) != 1:
            AddToPropmts("Invalid action")
        if "sword" in args[0].lower():
            message = Inventario.equip_weapon(args[0].title())
        elif "shield" in args[0].lower():
            message = Inventario.equip_shield(args[0].title())
        else:
            AddToPropmts("Invalid action")
            return
        AddToPropmts(message)
        if message == f"You have equipped '{args[0].title()}'":
            ActionTime()
            SaveData()
    elif command == "unequip":
        if len(args) != 1:
            AddToPropmts("Invalid action")
        if "sword" in args[0].lower() or "shield" in args[0].lower():
            message = Inventario.unequip_item(args[0].title())
            AddToPropmts(message)
            if message == f"You have unequipped '{args[0].title()}'":
                ActionTime()
                SaveData()
        else:
            AddToPropmts("Invalid action")
    elif command == "eat":
        if len(args) != 1:
            AddToPropmts("Invalid action")
        message = Interaccion.Eat(args[0].capitalize())
        AddToPropmts(message)
        if message == f"You ate a {args[0].capitalize()}":
            ActionTime()
            SaveData()
    elif command == "cheat":
        return
    elif command == "back":
        if Jugabilidad.mapName == "Castle":
            if len(args) != 0:
                AddToPropmts("Invalid action")
            else:
                Jugabilidad.LoadMap(Jugabilidad.previusLocation)
                message = Interaccion.DecideFoxVisibility()
                AddToPropmts(message)
                ActionTime()
                SaveData()
        else:
            AddToPropmts("Invalid action")
    elif command == "exit":
        if len(args) != 0:
            AddToPropmts("Invalid action")
        return "back"
    else:
        AddToPropmts("Invalid action")

invetoryToShow = "main"

def MapMenu(LastLocation):
    global invetoryToShow
    invetoryToShow = "main"
    Jugabilidad.LoadMap(LastLocation)
    message = Interaccion.DecideFoxVisibility()
    AddToPropmts(message)
    while(True):
        clear_screen()
        mapstr = Jugabilidad.MapToStr()
        menus = [[Jugabilidad.mapName,1]] + ActionsAvailables()
        mapstr = WithFrame(mapstr,Menus=menus)
        inventorystr = GetInventory()
        UI = concathorizontal(mapstr,inventorystr)
        print(UI)
        print("\n## Last Prompts ##")
        for prompt in prompts_list:
            print(prompt)
        print("- - - - -\nWhat do you want to do next?")
        action = input("> ")
        command,args = parse_input(action)
        if ExecuteMapAction(command,args) == "back":
            break 
        if Combate.PlayerLife <= 0:
            GameOverMenu()
            break

def GameOverMenu():
    while(True):
        clear_screen()
        GameOver()
        print("\n## Last Prompts ##")
        for p in prompts_list:
            print(p)
        print("- - - - -\nWhat to do now?")
        action = input("> ").lower()
        if action == "back":
            AddToPropmts(action)
            Combate.PlayerLife = Combate.PlayerMaxLife
            SaveData()
            break
        else:
            AddToPropmts("Invalid Action")


def ActionTime():
    #Broken trees regen -=1
    btrees = Jugabilidad.GetAllEntiiesWithName("Broken Tree")
    for tree in btrees:
        tree["regen"] -= 1
        if tree["regen"] <= 0:
            tree["name"] = "Tree"
            del tree["regen"]
    #Reclose ches if condition
    if len(Jugabilidad.GetAllEntiiesWithName("Closed Chest")) == 0 and Inventario.GetItem("Wood Sword")[1] == 0 and Inventario.GetItem("Sword")[1] == 0:
        Interaccion.RecloseChest()
    #Blood Moon
    Combate.BloodMoon += 1
    if Combate.BloodMoon >= 25:
        Combate.BloodMoon = 0
        Combate.BloodMoonAppearances += 1
        Jugabilidad.RespawnEnemies()

def SaveData():
    ActiveSave = Guardado.ActiveSave
    Inventario.SaveInventory(ActiveSave)
    Jugabilidad.SaveMapInfo(ActiveSave)
    Combate.SaveCombate(ActiveSave)
    Guardado.Saves[ActiveSave]["SaveDate"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    Guardado.SaveToDB(ActiveSave)

Guardado.LoadFromDB()
MainMenu()
