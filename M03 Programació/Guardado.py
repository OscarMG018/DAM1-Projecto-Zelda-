from datetime import datetime
import json
import os
import copy

ActiveSave = 0

Saves = [
    
]

def SaveToFile():
    with open("saves.json", "w") as f:
        json.dump(Saves, f)

def LoadFromFile():
    if os.path.isfile("saves.json"):
        with open("saves.json", "r") as f:
            global Saves
            Saves = json.load(f)

def SaveToDB():
    return

def LoadFromDB():
    return

def DeleteSaveFromDB():
    return

def NewSave(PlayerName):
    return {
        "DateStarted" : datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "SaveDate" : datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "PlayerName" : PlayerName,
        "LastLocation" : "Hyrule",
        "PlayerLife" : 3,
        "PlayerMaxLife" : 3,
        "BloodMoon" : 0,
        "BloodMoonAppearences" : 0,
        "SanctuariesOpened" : [False,False,False,False,False,False,False],
        "Inventario" : {"Vegetable": 0, "Fish": 0, "Meat": 0, "Salad": 0, "Pescatarian": 0, "Roasted": 0},
        "Inventario Armas" : {"Wood Sword":[0, 0, False], "Sword": [0, 0, False], "Wood Shield":[0, 0, False], "Shield":[0, 0, False]},
        "MapInformation" : {
            "Hyrule" : {
                "Enemies" : [
                    {"x" : 35, "y" : 4, "life" : 9, "EnemyNumber" : 0},
                    {"x" : 20, "y" : 8, "life" : 1, "EnemyNumber" : 1}
                ],
                "Chests" : [
                    {"x" : 46, "y" : 8,"opened" : False},
                ]
            },
            "Death mountain" : {
                "Enemies" : [
                    {"x" : 11, "y" : 3, "life" : 2, "EnemyNumber" : 0},
                    {"x" : 50, "y" : 2, "life" : 2, "EnemyNumber" : 1}
                ],
                "Chests" : [
                    {"x" : 35, "y" : 7,"opened" : False}
                ]
            },
            "Gerudo" : {
                "Enemies" : [
                    {"x" : 2, "y" : 3, "life" : 1, "EnemyNumber" : 0},
                    {"x" : 37, "y" : 5, "life" : 2, "EnemyNumber" : 1}
                ],
                "Chests" : [
                    {"x" : 7, "y" : 8, "opened" : False},
                    {"x" : 51, "y" : 0, "opened" : False}
                ]
            },
            "Necluda" : {
                "Enemies" : [
                    {"x" : 9, "y" : 1, "life" : 1, "EnemyNumber" : 0},
                    {"x" : 37, "y" : 5, "life" : 2, "EnemyNumber" : 1}
                ],
                "Chests" : [
                    {"x" : 21, "y" : 0, "opened" : False},
                    {"x" : 22, "y" : 8, "opened" : False},
                    {"x" : 50, "y" : 1, "opened" : False}           
                ]
            }
        }
    }

def GetMapInfo(number):
    return [copy.deepcopy(Saves[number]["MapInformation"]),Saves[number]["LastLocation"],copy.deepcopy(Saves[number]["SanctuariesOpened"])]

def GetInventoryInfo(number):
    return [copy.deepcopy(Saves[number]["Inventario"]),copy.deepcopy(Saves[number]["Inventario Armas"])]

def GetCombateInfo(number):
    return [Saves[number]["PlayerLife"],Saves[number]["PlayerMaxLife"],Saves[number]["BloodMoon"],Saves[number]["BloodMoonAppearences"]]