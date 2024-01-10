import random

ascii_draws = [
[
"         &&         ",
"         &&         ",
"      ##OOO         ",
"     ###OOOO        ",
"Zelda, Breath of the Wild                                   ###OOO \       ",
"       |@@@| \      ",
"       |   |  \     ",
"       =   ==       ",
"   %%%%%%%%%%%%     ",
"%%%%%%%%%%%%%%%     "
],
[
"        &&          ",
"        oo &        ",
"$       -- &##      ",
"$$     <<OO####     ",
"Zelda, Breath of the Wild                               $$  //OOO####      ",
"  $$// OO#####      ",
"   **   OOO###      ",
"    &   @@@@\       ",
"        Q  Q        ",
"        Q  Q        "
],
[
"       &&           ",
"      ####          ",
'     " || "         ',
"  @@@@@@@@@@@@      ",
"Zelda, Breath of the Wild                               @     ||@@@        ",
"       |@@@         ",
"      @@@           ",
"    @@@||     @     ",
" @@@@@@@@@@@@@      ",
"       ||           "
]
]

# Seleccionar aleatoriamente un dibujo de la lista "ascii_draws"
draw_chosen = random.choice(ascii_draws)