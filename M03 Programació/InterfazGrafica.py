import Guardado
import Inventario
import Combate
import Jugabilidad
import os
import Interaccion
from menuprincipal.ascii_draws_chosen import draw_chosen

#Funciones de utilidad

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



def InitializeNewGame(PlayerName):
    #Consigue un Guardado base
    save = Guardado.NewSave(PlayerName)
    #Consigue una GameId para el Guardado
    GameId = Guardado.GetNewGameId()
    #Guarda el Guardado en el diccionario local y en la base de datos
    Guardado.Saves[GameId] = save
    #Guardado.NewDBSave(PlayerName, GameId)
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
    return Guardado.Saves[GameId]["LastLocation"]

# Sabremos si hay saved_game comprobando en la BD
saved_game = False

prompts_list = []

exit_game = False

# Funcion para borrar la pantalla
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    # Imprimir el marco superior
    print("* " * 40)

    # Imprimir el contenido del dibujo con los marcos laterales
    for line in draw_chosen:
        print("*" + line.rjust(77) + "*")

    # Comprobar si hay una partida guardada e imprimir opciones del menú según
    if not saved_game: 
        print("* New Game, Help, About, Exit " + ("* " * 25))
        return ["new game", "help", "about", "exit"]
    else:
        print("* Continue, New Game, Help, About, Exit " + ("* " * 20))
        return ["continue", "new game", "help", "about", "exit"]

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
    return "back"

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

def root():
    global exit_game
    while not exit_game:
        clear_screen()
        if len(prompts_list) > 8:
            del prompts_list[0]
        available_prompts = main_menu()
        print("\n## Last Prompts ##")
        for prompt in prompts_list:
            print(prompt)
        print("- - - - -\nWhat to do now?")
        new_prompt = input("> ").lower()
        if new_prompt not in available_prompts:
            prompts_list.append("> " + "Invalid Action")
        else:
            prompts_list.append("> " + new_prompt)

            if new_prompt == "new game":
                new_prompt = NewGameMenu()

            if new_prompt == "help":
                while True:
                    clear_screen()
                    if len(prompts_list) > 8:
                        del prompts_list[0]
                    available_prompts = help_menu()
                    print("\n## Last Prompts ##")
                    for prompt in prompts_list:
                        print(prompt)
                    print("- - - - -\nWhat to do now?")
                    new_prompt = input("> ").lower()
                    if new_prompt not in available_prompts:
                        prompts_list.append("> " + "Invalid Action")
                    else:
                        prompts_list.append("> " + new_prompt)
                        break
                
            elif new_prompt == "about":
                while True:
                    clear_screen()
                    if len(prompts_list) > 8:
                        del prompts_list[0]
                    available_prompts = about_menu()
                    print("\n## Last Prompts ##")
                    for prompt in prompts_list:
                        print(prompt)
                    print("- - - - -\nWhat to do now?")
                    new_prompt = input("> ").lower()
                    if new_prompt not in available_prompts:
                        prompts_list.append("> " + "Invalid Action")
                    else:
                        prompts_list.append("> " + new_prompt)
                        break

def NewGameMenu():
    while True:
        clear_screen()
        if len(prompts_list) > 8:
            del prompts_list[0]
        available_prompts = new_game_menu()
        print("\n## Last Prompts ##")
        for prompt in prompts_list:
            print(prompt)
        print("- - - - -\nWhat's your name (Link)?")
        new_prompt = input("> ")
        if new_prompt not in available_prompts:
            if not new_prompt:
                prompts_list.append("> Welcome to the game, Link")   
                LegendPlotMenu("Link")                       
            elif not (new_prompt.replace(" ", "")).isalnum():
                prompts_list.append("> " + '"' + new_prompt + '"' + " is not a valid name")
            else:
                if len(new_prompt) < 3 or len(new_prompt) > 10:
                    prompts_list.append("> " + '"' + new_prompt + '"' + " is not a valid name")
                else:
                    user_name = new_prompt
                    prompts_list.append("> Welcome to the game, " + new_prompt)
                    LegendPlotMenu(new_prompt)
        else:
            prompts_list.append("> " + new_prompt)
            if new_prompt == "help":
                while True:
                    clear_screen()
                    if len(prompts_list) > 8:
                        del prompts_list[0]
                    available_prompts = new_game_menu_help()
                    print("\n## Last Prompts ##")
                    for prompt in prompts_list:
                        print(prompt)
                    print("- - - - -\nWhat to do now?")
                    new_prompt = input("> ").lower()
                    if new_prompt not in available_prompts:
                        prompts_list.append("> " + "Invalid Action")
                    else:
                        prompts_list.append("> " + new_prompt)
                        break
            else:
                break
    return new_prompt

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

def ExecuteMapAction(action):
    action = action.split(" ")
    if action[0] == "fishing":
        print(Interaccion.Fishing())
    if action[0] == "go":
        Jugabilidad.MovePlayerBy(int(action[1]),int(action[2]))
    if action[0] == "goto":
        Jugabilidad.MovePlayerNearEntity("symbol",action[1])
    if action[0] == "open":
        if action[1] == "chest":
            print(Interaccion.OpenChest())
        elif action[1] == "sanctuary":
            print(Interaccion.OpenSanctuary())

def MapMenu(LastLocation):
    Jugabilidad.LoadMap(LastLocation)
    Interaccion.DecideFoxVisibility()
    while(True):
        clear_screen()
        print(WithFrame(Jugabilidad.MapToStr(),[[Jugabilidad.mapName,1],["Back",2]]))
        print("\n## Last Prompts ##")
        for prompt in prompts_list:
            print(prompt)
        print("- - - - -\nWhat do you want to do next?")
        new_prompt = input("> ").lower()
        ExecuteMapAction(new_prompt)

#Guardado.LoadFromDB()
root()