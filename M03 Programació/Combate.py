import Guardado

PlayerLife = 3
PlayerMaxLife = 3
BloodMoon = 0
BloodMoonAppearences = 0

def CombateInit(CombateInfo=None):
    global PlayerLife, PlayerMaxLife, BloodMoon, BloodMoonAppearences
    if CombateInfo != None:
        PlayerLife = CombateInfo[0]
        PlayerMaxLife = CombateInfo[1]
        BloodMoon = CombateInfo[2]
        BloodMoonAppearences = CombateInfo[3]
    else:
        PlayerLife = 3
        PlayerMaxLife = 3
        BloodMoon = 0
        BloodMoonAppearences = 0

def SaveCombate(number):
    global PlayerLife, PlayerMaxLife, BloodMoon, BloodMoonAppearences
    Guardado.Saves[number]["PlayerLife"] = PlayerLife
    Guardado.Saves[number]["PlayerMaxLife"] = PlayerMaxLife
    Guardado.Saves[number]["BloodMoon"] = BloodMoon
    Guardado.Saves[number]["BloodMoonAppearences"] = BloodMoonAppearences