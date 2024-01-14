from datetime import datetime
import json
import os
import copy
import mysql.connector

DBhost = 'localhost'
DBuser = 'root'
DBpassword = '123456'
DBdatabase = 'ProjectoDB'

ActiveSave = 0

Saves = {
}

def SaveToFile():
    with open("saves.json", "w") as f:
        json.dump(Saves, f)

def LoadFromFile():
    if os.path.isfile("saves.json"):
        with open("saves.json", "r") as f:
            global Saves
            Saves = json.load(f)

def ExecuteQuerry(querry):
    mydb = None
    try:
        mydb = mysql.connector.connect(
            host=DBhost,
            user=DBuser,
            password=DBpassword,
            database=DBdatabase
        )
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute(querry)
        mydb.commit()
        if querry.lower().startswith("select"):
            if mycursor.rowcount > 0:
                return mycursor.fetchall()
            else:
                return []
        else:
            return mycursor.rowcount
    except Exception as e:
        print(e)
        return None
    finally:
        if mydb != None:
            mydb.close()

def NewDBSave(PlayerName,number):
    ExecuteQuerry(f"INSERT INTO game VALUES ({number},'{PlayerName}', '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}', '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}', 3, 3, 0, 0, 'Hyrule')")
    ExecuteQuerry(f"INSERT INTO food VALUES ({number},'Vegetable',0,0,0)")
    ExecuteQuerry(f"INSERT INTO food VALUES ({number},'Fish',0,0,0)")
    ExecuteQuerry(f"INSERT INTO food VALUES ({number},'Meat',0,0,0)")
    ExecuteQuerry(f"INSERT INTO food VALUES ({number},'Salad',0,0,0)")
    ExecuteQuerry(f"INSERT INTO food VALUES ({number},'Pescatarian',0,0,0)")
    ExecuteQuerry(f"INSERT INTO food VALUES ({number},'Roasted',0,0,0)")
    ExecuteQuerry(f"INSERT INTO weapons VALUES ({number},'Sword',0,0,False,0,0)")
    ExecuteQuerry(f"INSERT INTO weapons VALUES ({number},'Shield',0,0,False,0,0)")
    ExecuteQuerry(f"INSERT INTO weapons VALUES ({number},'Wood Sword',0,0,False,0,0)")
    ExecuteQuerry(f"INSERT INTO weapons VALUES ({number},'Wood Shield',0,0,False,0,0)")
    for i in range(len(Saves[number]["SanctuariesOpened"])):
        ExecuteQuerry(f"INSERT INTO Sanctuaries VALUES ({number},{i},False)")
    for locationName,locationvalue in Saves[number]["MapInformation"].items():
        for enemy in locationvalue["Enemies"]:
            ExecuteQuerry(f"INSERT INTO enemies VALUES ({number},'{locationName}',{enemy['EnemyNumber']},{enemy['life']},{enemy['x']},{enemy['y']})")
        for id,chest in enumerate(locationvalue["Chests"]):
            ExecuteQuerry(f"INSERT INTO chests VALUES ({number},'{locationName}',{id},{chest['opened']})")

def SaveToDB(number):
    ExecuteQuerry(f"UPDATE game SET LastSaved = '{Saves[number]['SaveDate']}', UserName = '{Saves[number]['PlayerName']}', LastRegion = '{Saves[number]['LastLocation']}', PlayerCurrentLife = {Saves[number]['PlayerLife']}, PlayerMaxLife = {Saves[number]['PlayerMaxLife']}, BloodMoon = {Saves[number]['BloodMoon']}, BloodMoonAppearances = {Saves[number]['BloodMoonAppearances']} WHERE GameId = {number}")

    ExecuteQuerry(f"UPDATE food SET FoodQuantity = {Saves[number]['Inventario']['Vegetable']},TimesObtained = {Saves[number]['FoodObtained']['Vegetable']},TimesConsumed = {Saves[number]['FoodConsumed']['Vegetable']}  WHERE GameId = {number} and FoodName = 'Vegetables'")
    ExecuteQuerry(f"UPDATE food SET FoodQuantity = {Saves[number]['Inventario']['Fish']},TimesObtained = {Saves[number]['FoodObtained']['Fish']},TimesConsumed = {Saves[number]['FoodConsumed']['Fish']}  WHERE GameId = {number} and FoodName = 'Fish'")
    ExecuteQuerry(f"UPDATE food SET FoodQuantity = {Saves[number]['Inventario']['Meat']},TimesObtained = {Saves[number]['FoodObtained']['Meat']},TimesConsumed = {Saves[number]['FoodConsumed']['Meat']}  WHERE GameId = {number} and FoodName = 'Meat'")
    ExecuteQuerry(f"UPDATE food SET FoodQuantity = {Saves[number]['Inventario']['Salad']},TimesObtained = {Saves[number]['FoodObtained']['Salad']},TimesConsumed = {Saves[number]['FoodConsumed']['Salad']}  WHERE GameId = {number} and FoodName = 'Salad'")
    ExecuteQuerry(f"UPDATE food SET FoodQuantity = {Saves[number]['Inventario']['Pescatarian']},TimesObtained = {Saves[number]['FoodObtained']['Pescatarian']},TimesConsumed = {Saves[number]['FoodConsumed']['Pescatarian']}  WHERE GameId = {number} and FoodName = 'Pescatarian'")
    ExecuteQuerry(f"UPDATE food SET FoodQuantity = {Saves[number]['Inventario']['Roasted']},TimesObtained = {Saves[number]['FoodObtained']['Roasted']},TimesConsumed = {Saves[number]['FoodConsumed']['Roasted']}  WHERE GameId = {number} and FoodName = 'Roasted'")

    ExecuteQuerry(f"UPDATE weapons SET Equiped = {Saves[number]['Inventario Armas']['Sword'][2]}, WeaponDurability = {Saves[number]['Inventario Armas']['Sword'][0]}, WeaponQuantity = {Saves[number]['Inventario Armas']['Sword'][1]},TimesObtained = {Saves[number]['ArmasObteined']['Sword']},TimesUsed = {Saves[number]['ArmasUsed']['Sword']}  WHERE GameId = {number} and WeaponName = 'Sword'")
    ExecuteQuerry(f"UPDATE weapons SET Equiped = {Saves[number]['Inventario Armas']['Shield'][2]}, WeaponDurability = {Saves[number]['Inventario Armas']['Shield'][0]}, WeaponQuantity = {Saves[number]['Inventario Armas']['Shield'][1]},TimesObtained = {Saves[number]['ArmasObteined']['Shield']},TimesUsed = {Saves[number]['ArmasUsed']['Shield']}  WHERE GameId = {number} and WeaponName = 'Shield'")
    ExecuteQuerry(f"UPDATE weapons SET Equiped = {Saves[number]['Inventario Armas']['Wood Sword'][2]}, WeaponDurability = {Saves[number]['Inventario Armas']['Wood Sword'][0]}, WeaponQuantity = {Saves[number]['Inventario Armas']['Wood Sword'][1]},TimesObtained = {Saves[number]['ArmasObteined']['Wood Sword']},TimesUsed = {Saves[number]['ArmasUsed']['Wood Sword']}  WHERE GameId = {number} and WeaponName = 'Wood Sword'")
    ExecuteQuerry(f"UPDATE weapons SET Equiped = {Saves[number]['Inventario Armas']['Wood Shield'][2]}, WeaponDurability = {Saves[number]['Inventario Armas']['Wood Shield'][0]}, WeaponQuantity = {Saves[number]['Inventario Armas']['Wood Shield'][1]},TimesObtained = {Saves[number]['ArmasObteined']['Wood Shield']},TimesUsed = {Saves[number]['ArmasUsed']['Wood Shield']}  WHERE GameId = {number} and WeaponName = 'Wood Shield'")

    ExecuteQuerry(f"UPDATE Sanctuaries SET Opened = {Saves[number]['SanctuariesOpened'][0]} WHERE GameId = {number} and SanctuaryId = 0")
    ExecuteQuerry(f"UPDATE Sanctuaries SET Opened = {Saves[number]['SanctuariesOpened'][1]} WHERE GameId = {number} and SanctuaryId = 1")
    ExecuteQuerry(f"UPDATE Sanctuaries SET Opened = {Saves[number]['SanctuariesOpened'][2]} WHERE GameId = {number} and SanctuaryId = 2")
    ExecuteQuerry(f"UPDATE Sanctuaries SET Opened = {Saves[number]['SanctuariesOpened'][3]} WHERE GameId = {number} and SanctuaryId = 3")
    ExecuteQuerry(f"UPDATE Sanctuaries SET Opened = {Saves[number]['SanctuariesOpened'][4]} WHERE GameId = {number} and SanctuaryId = 4")
    ExecuteQuerry(f"UPDATE Sanctuaries SET Opened = {Saves[number]['SanctuariesOpened'][5]} WHERE GameId = {number} and SanctuaryId = 5")
    ExecuteQuerry(f"UPDATE Sanctuaries SET Opened = {Saves[number]['SanctuariesOpened'][6]} WHERE GameId = {number} and SanctuaryId = 6")

    for locationName,locationvalue in Saves[number]["MapInformation"].items():
        for enemy in locationvalue["Enemies"]:
            ExecuteQuerry(f"UPDATE enemies SET EnemyLife = {enemy['life']}, PosX = {enemy['x']}, PosY = {enemy['y']} WHERE GameId = {number} and EnemyId = {enemy['EnemyNumber']} and Loacation = '{locationName}'")
        for i,chest in enumerate(locationvalue["Chests"]):
            ExecuteQuerry(f"UPDATE chests SET Opened = {chest['opened']} WHERE GameId = {number} and ChestId = {i} and Loacation = '{locationName}'")

def DeleteSaveFromDB(number):
    try:
        ExecuteQuerry(f"DELETE FROM food WHERE GameId = {number}")
        ExecuteQuerry(f"DELETE FROM weapons WHERE GameId = {number}")
        ExecuteQuerry(f"DELETE FROM Sanctuaries WHERE GameId = {number}")
        ExecuteQuerry(f"DELETE FROM enemies WHERE GameId = {number}")
        ExecuteQuerry(f"DELETE FROM chests WHERE GameId = {number}")
        ExecuteQuerry(f"DELETE FROM game WHERE GameId = {number}")
    except Exception as e:
        print(f"Error deleting save game {number}: {e}")

def LoadFromDB():
    global Saves
    Saves = {}
    for game in ExecuteQuerry("SELECT * FROM game"):
        Saves[game[0]] = {
            "DateStarted" : game[2],
            "SaveDate" : game[3],
            "PlayerName" : game[1],
            "LastLocation" : game[8],
            "PlayerLife" : game[5],
            "PlayerMaxLife" : game[4],
            "BloodMoon" : game[6],
            "BloodMoonAppearances" : game[7],
            "SanctuariesOpened" : [],
            "Inventario" : {},
            "FoodObtained" : {},
            "FoodConsumed" : {},
            "Inventario Armas" : {},
            "ArmasObteined" : {},
            "ArmasUsed" : {},
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
    
    for food in ExecuteQuerry("SELECT * FROM food"):
        Saves[food[0]]["Inventario"][food[1]] = food[2]
        Saves[food[0]]["FoodObtained"][food[1]] = food[3]
        Saves[food[0]]["FoodConsumed"][food[1]] = food[4]
    
    for weapon in ExecuteQuerry("SELECT * FROM weapons"):
        if weapon[4] == 1:
            Saves[weapon[0]]["Inventario Armas"][weapon[1]] = [weapon[3], weapon[2], True]
        else:
            Saves[weapon[0]]["Inventario Armas"][weapon[1]] = [weapon[3], weapon[2], False]
        Saves[weapon[0]]["ArmasObteined"][weapon[1]] = weapon[5]
        Saves[weapon[0]]["ArmasUsed"][weapon[1]] = weapon[6]
    
    for sanctuary in ExecuteQuerry("SELECT * FROM Sanctuaries order by SanctuaryId asc"):
        if sanctuary[2] == 1:
            Saves[sanctuary[0]]["SanctuariesOpened"].append(True)
        else:
            Saves[sanctuary[0]]["SanctuariesOpened"].append(False)

    for enemy in ExecuteQuerry("SELECT * FROM enemies order by EnemyId asc"):
        Saves[enemy[0]]["MapInformation"][enemy[1]]["Enemies"][enemy[2]]["life"] = enemy[3]
        Saves[enemy[0]]["MapInformation"][enemy[1]]["Enemies"][enemy[2]]["x"] = enemy[4]
        Saves[enemy[0]]["MapInformation"][enemy[1]]["Enemies"][enemy[2]]["y"] = enemy[5]
    
    for chest in ExecuteQuerry("SELECT * FROM chests order by ChestId asc"):
        if chest[3] == 1:
            Saves[chest[0]]["MapInformation"][chest[1]]["Chests"][chest[2]]["opened"] = True
        else:
            Saves[chest[0]]["MapInformation"][chest[1]]["Chests"][chest[2]]["opened"] = False
    
def NewSave(PlayerName):
    return {
        "DateStarted" : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "SaveDate" : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "PlayerName" : PlayerName,
        "LastLocation" : "Hyrule",
        "PlayerLife" : 3,
        "PlayerMaxLife" : 3,
        "BloodMoon" : 0,
        "BloodMoonAppearances" : 0,
        "SanctuariesOpened" : [False,False,False,False,False,False,False],
        "Inventario" : {"Vegetable": 0, "Fish": 0, "Meat": 0, "Salad": 0, "Pescatarian": 0, "Roasted": 0},
        "FoodObtained" : {"Vegetable": 0, "Fish": 0, "Meat": 0, "Salad": 0, "Pescatarian": 0, "Roasted": 0},
        "FoodConsumed" : {"Vegetable": 0, "Fish": 0, "Meat": 0, "Salad": 0, "Pescatarian": 0, "Roasted": 0},
        "Inventario Armas" : {"Wood Sword":[0, 0, False], "Sword": [0, 0, False], "Wood Shield":[0, 0, False], "Shield":[0, 0, False]},
        "ArmasObteined" : {"Wood Sword" : 0, "Sword" : 0, "Wood Shield": 0, "Shield" :0},
        "ArmasUsed" : {"Wood Sword" : 0, "Sword" : 0, "Wood Shield": 0, "Shield" :0},
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
    return [Saves[number]["PlayerLife"],Saves[number]["PlayerMaxLife"],Saves[number]["BloodMoon"],Saves[number]["BloodMoonAppearances"]]

def GetSavedGameId(n):
    return list(Saves.keys())[n]

def GetNewGameId():
    if len(Saves.keys()) == 0:
        return 1
    return max(Saves.keys()) + 1

def DBConnectionTest():
    try:
        ExecuteQuerry("SELECT * FROM customers")
        return True
    except Exception as e:
        print(e)
        return False