import Guardado

PlayerLife = 3
PlayerMaxLife = 3
BloodMoon = 0
BloodMoonAppearances = 0

def InitCombate(CombateInfo=None):
    global PlayerLife, PlayerMaxLife, BloodMoon, BloodMoonAppearances
    if CombateInfo != None:
        PlayerLife = CombateInfo[0]
        PlayerMaxLife = CombateInfo[1]
        BloodMoon = CombateInfo[2]
        BloodMoonAppearances = CombateInfo[3]
    else:
        PlayerLife = 3
        PlayerMaxLife = 3
        BloodMoon = 0
        BloodMoonAppearances = 0

def SaveCombate(number):
    global PlayerLife, PlayerMaxLife, BloodMoon, BloodMoonAppearances
    Guardado.Saves[number]["PlayerLife"] = PlayerLife
    Guardado.Saves[number]["PlayerMaxLife"] = PlayerMaxLife
    Guardado.Saves[number]["BloodMoon"] = BloodMoon
    Guardado.Saves[number]["BloodMoonAppearances"] = BloodMoonAppearances