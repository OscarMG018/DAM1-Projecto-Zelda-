import os
from ascii_draws_chosen import draw_chosen

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
