import copy
import random
from collections import deque
import Guardado

mapName = "Hyrule"
previusLocation = "Hyrule"

OpenSanctuaris = [False,False,False,False,False,False,False]

# To load a map and see it it requires to have the entity of the player
OriginalMaps = {
    "Hyrule" : {
        #56*10
        "terrain" : [
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","O","O","O"],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","~","~","~","~","~","~","O","O","~","O","O","O","O","~"],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~"," "," "," ","~","~","~","~","~","~"],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~"],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" ","O","O"," "," "," "," ","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            ["O","O","O","O","O","O","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
        ],
        "entities" : [
            {"name" : "Cuina" , "symbol" : "C", "x" : 16, "y" : 2},
            {"name" : "Tree" , "symbol" : "T", "x" : 5, "y" : 3, "hits" : 0},
            {"name" : "Enemy" , "symbol" : "E", "x" : 35, "y" : 4, "life" : 9,"EnemyNumber" : 0},
            {"name" : "Sanctuary" , "symbol" : "S", "x" : 42, "y" : 5, "SanctuaryNumber" : 0},
            {"name" : "Player" , "symbol" : "X", "x" : 10, "y" : 7},
            {"name" : "Tree" , "symbol" : "T", "x" : 46, "y" : 7, "hits" : 0},
            {"name" : "Enemy" , "symbol" : "E", "x" : 20, "y" : 8, "life" : 1,"EnemyNumber" : 1},
            {"name" : "Sanctuary" , "symbol" : "S", "x" : 28, "y" : 8, "SanctuaryNumber" : 1},
            {"name" : "Closed Chest" , "symbol" : "M", "x" : 46, "y" : 8, "item" : "Sword"},
            {"name" : "Tree" , "symbol" : "T", "x" : 44, "y" : 8, "hits" : 0}
        ]
    },
    "Death mountain" : {
        "terrain" : [
            ["O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            ["O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            ["~","~"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            ["~","~","~"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            ["O","~","~","~","~","~","~","~","~"," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," ","O","O"," "," "," "," ","O","O","O","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            ["~","~","~","~","~","~","~","~","~"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," ","~","~","~"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," ","O","O"," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
        ],
        "entities" : [
            {"name" : "Sanctuary" , "symbol" : "S", "x" : 5, "y" : 2, "SanctuaryNumber" : 2},
            {"name" : "Enemy" , "symbol" : "E", "x" : 11, "y" : 3, "life" : 2,"EnemyNumber" : 0},
            {"name" : "Player" , "symbol" : "X", "x" : 1, "y" : 8},
            {"name" : "Cuina" , "symbol" : "C", "x" : 5, "y" : 8},
            {"name" : "Tree" , "symbol" : "T", "x" : 17, "y" : 8, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 17, "y" : 7, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 18, "y" : 6, "hits" : 0},
            {"name" : "Closed Chest" , "symbol" : "M", "x" : 35, "y" : 7, "item" : "Shield"},
            {"name" : "Sanctuary" , "symbol" : "S", "x" : 48, "y" : 8, "SanctuaryNumber" : 3},
            {"name" : "Enemy" , "symbol" : "E", "x" : 50, "y" : 2, "life" : 2,"EnemyNumber" : 1}
        ]
    },
    "Gerudo" : {
        "terrain" : [
            ["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," ","O","O","O","O","O"," "," ","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O"],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O"],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O"],
            [" "," "," "," "," "," "," "," "," "," "," "," "," ","A","A","A","A","A","A"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," ","A","A","A","A","A","A","A","A"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," ","A","A","A","A","A","A","A"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~"],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," ","A","A","A"," "," "," "," "," "," "," "," ","O","O","O","O","O"," "," "," "," ","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~"],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~"]
        ],
        "entities" : [
            {"name" : "Enemy" , "symbol" : "E", "x" : 2, "y" : 3, "life" : 1,"EnemyNumber" : 0},
            {"name" : "Player" , "symbol" : "X", "x" : 1, "y" : 8},
            {"name" : "Tree" , "symbol" : "T", "x" : 4, "y" : 7, "hits" : 0},
            {"name" : "Closed Chest" , "symbol" : "M", "x" : 7, "y" : 8, "item" : "Sword"},
            {"name" : "Cuina" , "symbol" : "C", "x" : 14, "y" : 3},
            {"name" : "Tree" , "symbol" : "T", "x" : 28, "y" : 1, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 29, "y" : 1, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 30, "y" : 1, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 30, "y" : 2, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 31, "y" : 2, "hits" : 0},
            {"name" : "Enemy" , "symbol" : "E", "x" : 37, "y" : 5, "life" : 2,"EnemyNumber" : 1},
            {"name" : "Sanctuary" , "symbol" : "S", "x" : 45, "y" : 2, "SanctuaryNumber" : 4},
            {"name" : "Closed Chest" , "symbol" : "M", "x" : 51, "y" : 0, "item" : "Sword"}
        ]
    },
    "Necluda" : {
        "terrain" : [
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            ["O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~"],
            ["O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","~","~"],
            ["O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~"],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~"],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","~","~","~"],
            ["~","~"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~"],
            ["~","~","~","~","~","~","~","~"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","~","~","~","~","~","~"],
            ["~","~","~","~","~","~","~","~","~","~","~","~"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~"]
        ],
        "entities" : [
            {"name" : "Player" , "symbol" : "X", "x" : 1, "y" : 1},
            {"name" : "Enemy" , "symbol" : "E", "x" : 9, "y" : 1, "life" : 1,"EnemyNumber" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 13, "y" : 6, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 14, "y" : 5, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 14, "y" : 7, "hits" : 0},
            {"name" : "Cuina" , "symbol" : "C", "x" : 18, "y" : 2},
            {"name" : "Closed Chest" , "symbol" : "M", "x" : 21, "y" : 0, "item" : "Shield"},
            {"name" : "Closed Chest" , "symbol" : "M", "x" : 22, "y" : 8, "item" : "Shield"},
            {"name" : "Sanctuary" , "symbol" : "S", "x" : 32, "y" : 8, "SanctuaryNumber" : 6},
            {"name" : "Tree" , "symbol" : "T", "x" : 34, "y" : 2, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 35, "y" : 2, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 36, "y" : 1, "hits" : 0},
            {"name" : "Tree" , "symbol" : "T", "x" : 37, "y" : 1, "hits" : 0},
            {"name" : "Enemy" , "symbol" : "E", "x" : 37, "y" : 5, "life" : 2,"EnemyNumber" : 1},
            {"name" : "Sanctuary" , "symbol" : "S", "x" : 50, "y" : 5, "SanctuaryNumber" : 5},
            {"name" : "Closed Chest" , "symbol" : "M", "x" : 50, "y" : 1, "item" : "Shield"}
        ]
    },
    "Castle" : {
        "terrain" : [
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," ","\\"," ","/"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," ","-","-"," ","O"," ","-","-"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","G","a","n","o","n"," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," ","/"," ","\\"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|",">"," "," ","v","-","v","-","v","-","v"," "," "," ","|",">"," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",","," "," "," ",","," "," ","/","_","\\"," "," ","|"," "," "," "," "," ","|"," "," ","/","_","\\"," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|","\\","_","/","|"," "," ","|"," ","|","'","'","'","'","'","'","'","'","'","'","'","|"," ","|"," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","(","q"," ","p",")",",","-","|"," ","|"," ","|","|"," "," ","_"," "," ","|","|"," ","|"," ","|","'","-",".","_"," ","|","\\"," "," "," "," "," "],
            ["O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","\\","_","/","_","(","/","|"," ","|"," "," "," "," ","|","#","|"," "," "," "," ","|"," ","|"," ",")"," "," ","'","/","/"," "," "," "," "," "],
            ["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"]
        ],
        "entities" : [
            {"name" : "Player" , "symbol" : "X", "x" : 2, "y" : 8},
            {"name" : "Tree" , "symbol" : "T", "x" : 1, "y" : 8, "hits" : 0},
            {"name" : "GanonHeart" , "symbol" : "♥", "x" : 46, "y" :2, "hits" : 0},
            {"name" : "GanonHeart" , "symbol" : "♥", "x" : 47, "y" :2, "hits" : 0},
            {"name" : "GanonHeart" , "symbol" : "♥", "x" : 48, "y" :2, "hits" : 0},
            {"name" : "GanonHeart" , "symbol" : "♥", "x" : 49, "y" :2, "hits" : 0},
            {"name" : "GanonHeart" , "symbol" : "♥", "x" : 50, "y" :2, "hits" : 0},
            {"name" : "GanonHeart" , "symbol" : "♥", "x" : 51, "y" :2, "hits" : 0},
            {"name" : "GanonHeart" , "symbol" : "♥", "x" : 52, "y" :2, "hits" : 0},
            {"name" : "GanonHeart" , "symbol" : "♥", "x" : 53, "y" :2, "hits" : 0},
            {"name" : "Ganon" , "symbol" : " ", "x" : 20, "y" :8},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 0, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 1, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 2, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 3, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 4, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 5, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 6, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 7, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 8, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 9, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 10, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 11, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 12, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 13, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 14, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 15, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 16, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 17, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 18, "y" :7},
            {"name" : "InvisibleWall" , "symbol" : " ", "x" : 19, "y" :7},
        ]
    }
}

maps = {}

map = []

entities = []
    
def ValidPosition(y,x):
    if y < 0 or y >= len(map) or x < 0 or x >= len(map[0]):
        return False
    return True

def TerrainAt(y,x):
    if y < 0 or y >= len(map) or x < 0 or x >= len(map[0]):
        raise IndexError("Attempted to access terrain out of range")
    return map[y][x]
    
def IsBlocked(y,x):
    if TerrainAt(y,x) == "O" or TerrainAt(y,x) == "~" or TerrainAt(y,x) == "A":
        return True
    if GetIndexByPosition(y,x) != -1:
        return True
    return False

def MoveEntityTo(entityIndex,y,x):
    if entityIndex >= len(entities) or entityIndex < 0:
        raise IndexError("Attempted to move an entity out of range")
    if not ValidPosition(y,x):
        raise ValueError("Attempted to move an entity to an invalid position")
    if IsBlocked(y,x):
        return False
    else:
        entities[entityIndex]["x"] = x
        entities[entityIndex]["y"] = y
        return True

def MoveEntityBy(entityIndex,moveY,moveX):
    if entityIndex >= len(entities) or entityIndex < 0:
        raise IndexError("Attempted to move an entity out of range")
    if not ValidPosition(entities[entityIndex]["y"] + moveY,entities[entityIndex]["x"] + moveX):
        raise ValueError("Attempted to move an entity to an invalid position")
    y = entities[entityIndex]["y"] + moveY
    x = entities[entityIndex]["x"] + moveX

    if IsBlocked(y,x):
        return False
    else:
        entities[entityIndex]["y"] = y
        entities[entityIndex]["x"] = x
        return True

def RemoveEntity(entityIndex,location=None):
    if location != None:
        if entityIndex >= len(maps[location]["entities"]) or entityIndex < 0:
            raise IndexError("Attempted to remove an entity out of range in an unloaded map")
        maps[location]["entities"].pop(entityIndex)
        return
    else:
        if entityIndex >= len(entities) or entityIndex < 0:
            raise IndexError("Attempted to remove an entity out of range")
        entities.pop(entityIndex)

def AddEntity(entity):
    if "x" not in entity or "y" not in entity:
        raise KeyError("Attempted to add an entity without x and y coordinates")
    if "name" not in entity:
        raise KeyError("Attempted to add an entity without a name")
    if "symbol" not in entity:
        raise KeyError("Attempted to add an entity without a simbol")
    if IsBlocked(entity["y"],entity["x"]):
        raise ValueError("Attempted to add an entity on a blocked tile")
    entities.append(entity)

def GetIndexOfEntity(entity,location=None):
    if location == None:
        for i in range(len(entities)):
            if entities[i] == entity:
                return i
        return -1
    else:
        for i in range(len(maps[location]["entities"])):
            if maps[location]["entities"][i] == entity:
                return i
        return -1

def GetIndexByPosition(y,x):
    for i in range(len(entities)):
        if entities[i]["x"] == x and entities[i]["y"] == y:
            return i
    return -1

def GetEntityByPosition(y,x):
    for entity in entities:
        if entity["x"] == x and entity["y"] == y:
            return entity
    return None

def GetEntityByIndex(index):
    if index >= len(entities) or index < 0:
        raise IndexError("Attempted to get an entity out of range")
    return entities[index]

def GetAllEntiiesWithName(name,location=None):
    if location == None:
        entitiesWithName = []
        for entity in entities:
            if entity["name"] == name:
                entitiesWithName.append(entity)
        return entitiesWithName
    else:
        entitiesWithName = []
        for entity in maps[location]["entities"]:
            if entity["name"] == name:
                entitiesWithName.append(entity)
        return entitiesWithName

def GetAllEntitiesWithSimbol(simbol):
    entitiesWithSimbol = []
    for entity in entities:
        if entity["symbol"] == simbol:
            entitiesWithSimbol.append(entity)
    return entitiesWithSimbol

def AdjacentTerrain(y,x,terrainToFind,CountCenter=False):
    for y2 in range(y-1,y+2):
        for x2 in range(x-1,x+2):
            if y2 == y and x2 == x and not CountCenter:
                continue
            if ValidPosition(y2,x2) and TerrainAt(y2,x2) == terrainToFind:
                return True
    return False

def AdjacentEntity(y,x,entityToFind,PropertySearching="name"):
    for y2 in range(y-1,y+2):
        for x2 in range(x-1,x+2):
            if ValidPosition(y2,x2) and GetEntityByPosition(y2,x2) != None and GetEntityByPosition(y2,x2)[PropertySearching] == entityToFind:
                return GetEntityByPosition(y2,x2)
    return None

def NearestTerrain(y, x, terrainToFind):
    visited = [[False for _ in range(len(map[0]))] for _ in range(len(map))]
    queue = deque([(y, x, 0)])  # (y, x, distance)
    visited[y][x] = True

    while queue:
        y, x, dist = queue.popleft()
        if TerrainAt(y, x) == terrainToFind:
            return (y, x)

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # up, down, left, right
            ny, nx = y + dy, x + dx
            if ValidPosition(ny, nx) and not visited[ny][nx]:
                queue.append((ny, nx, dist + 1))
                visited[ny][nx] = True

    return (-1, -1)  # return an invalid position if the terrain is not found

def NearestEntity(y, x, entityToFind,PropertySearching="name"):
    visited = [[False for _ in range(len(map[0]))] for _ in range(len(map))]
    queue = deque([(y, x, 0)])  # (y, x, distance)
    visited[y][x] = True

    while queue:
        y, x, dist = queue.popleft()
        if GetEntityByPosition(y, x) != None and GetEntityByPosition(y, x).get(PropertySearching) != None  and GetEntityByPosition(y, x)[PropertySearching] == entityToFind:
            return (y, x)

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # up, down, left, right
            ny, nx = y + dy, x + dx
            if ValidPosition(ny, nx) and not visited[ny][nx]:
                queue.append((ny, nx, dist + 1))
                visited[ny][nx] = True

    return (-1, -1)  # return an invalid position if the terrain is not found

def MapToStr():
    mapstr = ""
    y = 0
    while y < len(map):
        x = 0
        while x < len(map[0]):
            entity = GetEntityByPosition(y,x)
            if entity != None: #TODO all cases for all entities
                if entity["name"] == "Enemy":
                    if ValidPosition(y,x+1) and GetEntityByPosition(y,x+1) == None:
                        x += 1
                        mapstr += entity["symbol"]+str(entity["life"])
                    else:
                        mapstr += entity["symbol"] 
                elif entity["name"] == "Broken Tree":
                    if ValidPosition(y,x+1) and GetEntityByPosition(y,x+1) == None:
                        x += 1
                        mapstr += "T" + str(entity["regen"])
                    else:
                        mapstr += entity["symbol"] 
                elif entity["name"] == "Sanctuary":
                    if OpenSanctuaris[entity["SanctuaryNumber"]]:
                        if ValidPosition(y,x+1) and GetEntityByPosition(y,x+1) == None:
                            x += 1
                            mapstr += entity["symbol"] + str(entity["SanctuaryNumber"])
                        else:
                            mapstr += entity["symbol"]
                    else:
                        if ValidPosition(y,x+1) and GetEntityByPosition(y,x+1) == None:
                            x += 1
                            mapstr += entity["symbol"] + str(entity["SanctuaryNumber"])
                            if ValidPosition(y,x+2) and GetEntityByPosition(y,x+2) == None:
                                x += 1
                                mapstr += "?"
                        else:
                            mapstr += entity["symbol"]
                else:
                    mapstr += entity["symbol"]
            else:
                mapstr += map[y][x]
            x += 1
        if y < len(map)-1:
            mapstr += "\n"
        y += 1
    return mapstr
#print(MapToStr())

def InitMap(MapInfo=None):
    global maps, OpenSanctuaris
    maps = copy.deepcopy(OriginalMaps)
    if MapInfo != None:
        mapName = MapInfo[1]
        OpenSanctuaris = MapInfo[2]
        for mapName,info in MapInfo[0].items():
            enemiesSaved = info["Enemies"]
            for enemy in GetAllEntiiesWithName("Enemy",location=mapName):
                enemySaved = next((e for e in enemiesSaved if e["EnemyNumber"] == enemy["EnemyNumber"]), None)
                if enemySaved == None:
                    raise ValueError("Error: Could not Initialize Map, Enemy in map has no conterpart in SaveFile ")
                if enemySaved["life"] == 0:
                    RemoveEntity(GetIndexOfEntity(enemy,location=mapName),location=mapName)
                else:
                    enemy["life"] = enemySaved["life"]
                    enemy["x"] = enemySaved["x"]
                    enemy["y"] = enemySaved["y"]
            
            chestsSaved = info["Chests"]
            for chest in GetAllEntiiesWithName("Closed Chest",location=mapName):
                chestSaved = next((c for c in chestsSaved if c["x"] == chest["x"] and c["y"] == chest["y"]), None) 
                if chestSaved == None:
                    raise ValueError("Error: Could not Initialize Map, Chest in map has no conterpart in SaveFile ")
                if chestSaved["opened"]:
                    chest["name"] = "Open Chest"
                    chest["symbol"] = "W"
        
                
"""-------------Jugador-----------"""

def GetPlayerIndex():
    for i in range(len(entities)):
        if entities[i]["name"] == "Player":
            return i
    return -1

def GetPlayer():
    return GetEntityByIndex(GetPlayerIndex())

def MovePlayerBy(y,x): #Para Arriba Abajo Derecha Izquierda
    player = GetPlayer()
    playerIndex = GetPlayerIndex()
    for i in range(abs(y)):
        px = player["x"]
        py = player["y"]
        if not ValidPosition(py - y//abs(y), px) or IsBlocked(py - y//abs(y), px):
            return "You can't go there, is not a valid position'"
        else:
            MoveEntityBy(playerIndex,-y//abs(y),0)  
    for i in range(abs(x)):
        px = player["x"]
        py = player["y"]
        if not ValidPosition(py, px + x//abs(x)) or IsBlocked(py, px + x//abs(x)):
            return "You can't go there, is not a valid position'"
        else:
            MoveEntityBy(playerIndex,0,x//abs(x))

def MovePlayerNearEntity(EntityProperty,EntityValue): #
    playerIndex = GetPlayerIndex()
    px = GetEntityByIndex(playerIndex)["x"]
    py = GetEntityByIndex(playerIndex)["y"]
    entityPosition = NearestEntity(py,px,EntityValue,EntityProperty)
    if entityPosition == (-1,-1):
        return f"That is not in this location"
    posiblePositions = []
    radius = 1
    while(len(posiblePositions) == 0):
        for pos in [(radius,0),(-radius,0),(0,radius),(0,-radius)]:
            if ValidPosition(entityPosition[0]+pos[0],entityPosition[1]+pos[1]) and not IsBlocked(entityPosition[0]+pos[0],entityPosition[1]+pos[1]):
                posiblePositions.append([entityPosition[0]+pos[0],entityPosition[1]+pos[1]])
        if len(posiblePositions) > 0:
            break
        for pos in [(radius,radius),(-radius,radius),(-radius,-radius),(radius,-radius)]:
            if ValidPosition(entityPosition[0]+pos[0],entityPosition[1]+pos[1]) and not IsBlocked(entityPosition[0]+pos[0],entityPosition[1]+pos[1]):
                posiblePositions.append([entityPosition[0]+pos[0],entityPosition[1]+pos[1]])
        radius += 1
    pos = random.choice(posiblePositions)
    MoveEntityTo(playerIndex,pos[0],pos[1])
    return f"You can't go to {EntityValue} from here"*(radius-1 != 0)

def MovePlayerNearTerrain(terrain):
    playerIndex = GetPlayerIndex()
    px = GetEntityByIndex(playerIndex)["x"]
    py = GetEntityByIndex(playerIndex)["y"]
    terrainPosition = NearestTerrain(py,px,terrain)
    if terrainPosition == (-1,-1):
        return f"There is no {terrain} near you"

    posiblePositions = []
    radius = 1
    while(len(posiblePositions) == 0):
        for dy in range(-radius,radius+1):
            for dx in range(-radius,radius+1):
                if dy == 0 and dx == 0:
                    continue
                if ValidPosition(terrainPosition[0]+dy,terrainPosition[1]+dx) and not IsBlocked(terrainPosition[0]+dy,terrainPosition[1]+dx):
                    posiblePositions.append([terrainPosition[0]+dy,terrainPosition[1]+dx])
        radius += 1
    pos = random.choice(posiblePositions)
    MoveEntityTo(playerIndex,pos[0],pos[1])
    return f"You can't go to {terrain} from here"*(radius-1 != 0)

"""-------------Enemy-----------"""

def MoveEnemy(entityIndex):
    entity = GetEntityByIndex(entityIndex)
    if entity == None:
        raise IndexError("Attempted to move an entity that doesn't exist")
    if entity["name"] != "Enemy":
        raise ValueError("(MoveEnemy) Attempted to move an entity that is not an Enemy")
    posiblePositions = []
    for dy in [-1,0,1]:
        for dx in [-1,0,1]:
            if dy == 0 and dx == 0:
                continue
            if ValidPosition(entity["y"]+dy,entity["x"]+dx) and not IsBlocked(entity["y"]+dy,entity["x"]+dx):
                posiblePositions.append([entity["y"]+dy,entity["x"]+dx])
    if len(posiblePositions) > 0:
        pos = random.choice(posiblePositions)
        MoveEntityTo(entityIndex,pos[0],pos[1])

def RespawnEnemies():
    global maps, OriginalMaps
    for mapName, mapInfo in OriginalMaps.items():
        originalEnemies = list(filter(lambda x: x["name"] == "Enemy", mapInfo["entities"]))
        currentEnemies = GetAllEntiiesWithName("Enemy", location=mapName)
        for originalEnemy in originalEnemies:
            if not any(currentEnemy["EnemyNumber"] == originalEnemy["EnemyNumber"] for currentEnemy in currentEnemies):
                maps[mapName]["entities"].append(originalEnemy.copy())  # Use copy to avoid modifying the original

def LoadMap(name):
    global map, entities, mapName, OriginalMaps, previusLocation
    if name not in maps:
        raise ValueError(f"Attempted to load an invalid map: {name}")
    previusLocation = mapName
    mapName = name
    map = maps[name]["terrain"]
    entities = maps[name]["entities"]
    #Reset Player Position
    player = GetPlayer()
    for i in range(len(OriginalMaps[name]["entities"])):
        if OriginalMaps[name]["entities"][i]["name"] == "Player":
            OriginalMapplayer = OriginalMaps[name]["entities"][i]
            player["x"] = OriginalMapplayer["x"]
            player["y"] = OriginalMapplayer["y"]
            break
    #Regen Ganon
    if previusLocation == "Castle":
        RegenGanon()

def RegenGanon():
    global maps, OriginalMaps
    # Readds the ganonHearts to the castle map
    castle_map = maps["Castle"]
    original_castle_entities = OriginalMaps["Castle"]["entities"]
    current_castle_entities = castle_map["entities"]

    # Find all GanonHeart entities in the original map
    original_ganon_hearts = [entity for entity in original_castle_entities if entity["name"] == "GanonHeart"]

    # Add GanonHeart entities to the current map if they are not already present
    for heart in original_ganon_hearts:
        # Check if the GanonHeart is already in the current entities
        if not any(entity["name"] == "GanonHeart" and entity["x"] == heart["x"] and entity["y"] == heart["y"] for entity in current_castle_entities):
            # Add the GanonHeart to the current entities
            current_castle_entities.append(heart.copy())  # Use copy to avoid modifying the original

    # Update the maps dictionary with the new entities list
    maps["Castle"]["entities"] = current_castle_entities

def SaveMapInfo(number):
    global maps, mapName, OriginalMaps
    Guardado.Saves[number]["LastLocation"] = mapName
    Guardado.Saves[number]["SanctuariesOpened"] = copy.deepcopy(OpenSanctuaris)
    
    for MapName,location in Guardado.Saves[number]["MapInformation"].items():
        MapEnemies = GetAllEntiiesWithName("Enemy",location=MapName)
        for SavedEnemy in location["Enemies"]:
            MapEnemy = next((e for e in MapEnemies if e["EnemyNumber"] == SavedEnemy["EnemyNumber"]), None)
            if MapEnemy != None:
                SavedEnemy["life"] = MapEnemy["life"]
                SavedEnemy["x"] = MapEnemy["x"]
                SavedEnemy["y"] = MapEnemy["y"]
            else:
                SavedEnemy["life"] = 0
        MapChests = GetAllEntiiesWithName("Closed Chest",location=MapName)
        MapChests += GetAllEntiiesWithName("Open Chest",location=MapName)
        for SavedChest in location["Chests"]:
            MapChest = next((c for c in MapChests if c["x"] == SavedChest["x"] and c["y"] == SavedChest["y"]), None)
            if MapChest != None:
                if MapChest["name"] == "Closed Chest":
                    SavedChest["opened"] = False
                else:
                    SavedChest["opened"] = True
            else:
                raise ValueError(f"There is a chest in the map that is not in the saveFile: {MapChests} {MapChest} {MapName} {SavedChest}")