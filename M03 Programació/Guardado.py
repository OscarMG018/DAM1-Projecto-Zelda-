from datetime import datetime
import json
import os
import copy
import mysql.connector

DBhost = 'your_host'
DBuser = 'your_username'
DBpassword = 'your_password'
DBdatabase = 'your_database_name'


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
    mydb = mysql.connector.connect(
        host=DBhost,
        user=DBuser,
        password=DBpassword,
        database=DBdatabase
    )
    mycursor = mydb.cursor()
    mycursor.execute(querry)
    mydb.commit()
    mydb.close()
    return mycursor.fetchall()

def NewDBSave(PlayerName,number):
    ExecuteQuerry(f"INSERT INTO game VALUES ({number},{PlayerName}, {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}, {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}, 3, 3, 0, 0, 'Hyrule')")
    ExecuteQuerry(f"INSERT INTO food VALUES ({number},Vegetables,0,0,0)")
    ExecuteQuerry(f"INSERT INTO food VALUES ({number},Fish,0,0,0)")
    ExecuteQuerry(f"INSERT INTO food VALUES ({number},Meat,0,0,0)")
    ExecuteQuerry(f"INSERT INTO food VALUES ({number},Salad,0,0,0)")
    ExecuteQuerry(f"INSERT INTO food VALUES ({number},Pescatarian,0,0,0)")
    ExecuteQuerry(f"INSERT INTO food VALUES ({number},Roasted,0,0,0)")
    ExecuteQuerry(f"INSERT INTO weapons VALUES ({number},Sword,0,0,0,0)")
    ExecuteQuerry(f"INSERT INTO weapons VALUES ({number},Shield,0,0,0,0)")
    ExecuteQuerry(f"INSERT INTO weapons VALUES ({number},Wood Sword,0,0,0,0)")
    ExecuteQuerry(f"INSERT INTO weapons VALUES ({number},Wood Shield,0,0,0,0)")
    for i in range(len(Saves[number]["SanctuariesOpened"])):
        ExecuteQuerry(f"INSERT INTO Sanctuaries VALUES ({number},Sanctuaries{i},False)")
    for location in Saves[number]["MapInformation"]:
        for enemy in location["Enemies"]:
            ExecuteQuerry(f"INSERT INTO enemies VALUES ({number},{location},{enemy['EnemyNumber']},{enemy['life']},{enemy['x']},{enemy['y']})")
        for chest in location["Chests"]:
            ExecuteQuerry(f"INSERT INTO chests VALUES ({number},{location},{chest['x']},{chest['y']},{chest['opened']})")

def SaveToDB(number):
    ExecuteQuerry(f"UPDATE game SET DateStarted = '{Saves[number]['DateStarted']}', LastSaved = '{Saves[number]['SaveDate']}', UserName = '{Saves[number]['PlayerName']}', LastRegion = '{Saves[number]['LastLocation']}', PlayerCurrentLife = {Saves[number]['PlayerLife']}, PlayerMaxLife = {Saves[number]['PlayerMaxLife']}, BloodMoon = {Saves[number]['BloodMoon']}, BloodMoonAppearences = {Saves[number]['BloodMoonAppearences']} WHERE GameId = {number}")

    ExecuteQuerry(f"UPDATE food SET FoodQuantity = {Saves[number]['Inventario']['Vegetable']},TimesObtained = {Saves[number]['FoodObtained']['Vegetable']},TimesConsumed = {Saves[number]['FoodComsumed']['Vegetable']}  WHERE GameId = {number} and FoodName = 'Vegetables'")
    ExecuteQuerry(f"UPDATE food SET FoodQuantity = {Saves[number]['Inventario']['Fish']},TimesObtained = {Saves[number]['FoodObtained']['Fish']},TimesConsumed = {Saves[number]['FoodComsumed']['Fish']}  WHERE GameId = {number} and FoodName = 'Fish'")
    ExecuteQuerry(f"UPDATE food SET FoodQuantity = {Saves[number]['Inventario']['Meat']},TimesObtained = {Saves[number]['FoodObtained']['Meat']},TimesConsumed = {Saves[number]['FoodComsumed']['Meat']}  WHERE GameId = {number} and FoodName = 'Meat'")
    ExecuteQuerry(f"UPDATE food SET FoodQuantity = {Saves[number]['Inventario']['Salad']},TimesObtained = {Saves[number]['FoodObtained']['Salad']},TimesConsumed = {Saves[number]['FoodComsumed']['Salad']}  WHERE GameId = {number} and FoodName = 'Salad'")
    ExecuteQuerry(f"UPDATE food SET FoodQuantity = {Saves[number]['Inventario']['Pescatarian']},TimesObtained = {Saves[number]['FoodObtained']['Pescatarian']},TimesConsumed = {Saves[number]['FoodComsumed']['Pescatarian']}  WHERE GameId = {number} and FoodName = 'Pescatarian'")
    ExecuteQuerry(f"UPDATE food SET FoodQuantity = {Saves[number]['Inventario']['Roasted']},TimesObtained = {Saves[number]['FoodObtained']['Roasted']},TimesConsumed = {Saves[number]['FoodComsumed']['Roasted']}  WHERE GameId = {number} and FoodName = 'Roasted'")

    ExecuteQuerry(f"UPDATE weapons SET WeaponsQuantity = {Saves[number]['Inventario Armas']['Sword'][0]},TimesObtained = {Saves[number]['ArmasObteined']['Sword']},TimesUsed = {Saves[number]['ArmasUsed']['Sword']}  WHERE GameId = {number} and WeaponName = 'Sword'")
    ExecuteQuerry(f"UPDATE weapons SET WeaponsQuantity = {Saves[number]['Inventario Armas']['Shield'][0]},TimesObtained = {Saves[number]['ArmasObteined']['Shield']},TimesUsed = {Saves[number]['ArmasUsed']['Shield']}  WHERE GameId = {number} and WeaponName = 'Shield'")
    ExecuteQuerry(f"UPDATE weapons SET WeaponsQuantity = {Saves[number]['Inventario Armas']['Wood Sword'][0]},TimesObtained = {Saves[number]['ArmasObteined']['Wood Sword']},TimesUsed = {Saves[number]['ArmasUsed']['Wood Sword']}  WHERE GameId = {number} and WeaponName = 'Wood Sword'")
    ExecuteQuerry(f"UPDATE weapons SET WeaponsQuantity = {Saves[number]['Inventario Armas']['Wood Shield'][0]},TimesObtained = {Saves[number]['ArmasObteined']['Wood Shield']},TimesUsed = {Saves[number]['ArmasUsed']['Wood Shield']}  WHERE GameId = {number} and WeaponName = 'Wood Shield'")

    ExecuteQuerry(f"UPDATE Sanctuaries SET SanctuaryOpened = {Saves[number]['SanctuariesOpened'][0]} WHERE GameId = {number} and SanctuaryId = 0")
    ExecuteQuerry(f"UPDATE Sanctuaries SET SanctuaryOpened = {Saves[number]['SanctuariesOpened'][1]} WHERE GameId = {number} and SanctuaryId = 1")
    ExecuteQuerry(f"UPDATE Sanctuaries SET SanctuaryOpened = {Saves[number]['SanctuariesOpened'][2]} WHERE GameId = {number} and SanctuaryId = 2")
    ExecuteQuerry(f"UPDATE Sanctuaries SET SanctuaryOpened = {Saves[number]['SanctuariesOpened'][3]} WHERE GameId = {number} and SanctuaryId = 3")
    ExecuteQuerry(f"UPDATE Sanctuaries SET SanctuaryOpened = {Saves[number]['SanctuariesOpened'][4]} WHERE GameId = {number} and SanctuaryId = 4")
    ExecuteQuerry(f"UPDATE Sanctuaries SET SanctuaryOpened = {Saves[number]['SanctuariesOpened'][5]} WHERE GameId = {number} and SanctuaryId = 5")
    ExecuteQuerry(f"UPDATE Sanctuaries SET SanctuaryOpened = {Saves[number]['SanctuariesOpened'][6]} WHERE GameId = {number} and SanctuaryId = 6")

    for location in Saves[number]["MapInformation"]:
        for enemy in location["Enemies"]:
            ExecuteQuerry(f"UPDATE enemies SET EnemyLife = {enemy['life']}, PosX = {enemy['x']}, PosY = {enemy['y']} WHERE GameId = {number} and EnemyId = {enemy['EnemyNumber']} and Loacation = '{location}'")
        for chest in location["Chests"]:
            ExecuteQuerry(f"UPDATE chests SET Opened = {chest['opened']} WHERE GameId = {number} and PosX = {chest['x']} and PosY = {chest['y']} and Loacation = '{location}'")

def DeleteSaveFromDB(number):
    return

def LoadFromDB():
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
        "FoodObtained" : {"Vegetable": 0, "Fish": 0, "Meat": 0, "Salad": 0, "Pescatarian": 0, "Roasted": 0},
        "FoodComsumed" : {"Vegetable": 0, "Fish": 0, "Meat": 0, "Salad": 0, "Pescatarian": 0, "Roasted": 0},
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
    return [Saves[number]["PlayerLife"],Saves[number]["PlayerMaxLife"],Saves[number]["BloodMoon"],Saves[number]["BloodMoonAppearences"]]

def RealNumeberList():
    dic = {}
    for i in range(len(Saves.keys())):
        dic[i] = Saves.keys()[i]
    return dic