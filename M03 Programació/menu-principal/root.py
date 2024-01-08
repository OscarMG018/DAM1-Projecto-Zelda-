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
                        elif not (new_prompt.replace(" ", "")).isalnum():
                            prompts_list.append("> " + '"' + new_prompt + '"' + " is not a valid name")
                        else:
                            user_name = new_prompt
                            prompts_list.append("> Welcome to the game, " + new_prompt)
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

root()