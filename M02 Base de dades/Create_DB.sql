DROP DATABASE IF EXISTS ZeldaDB;
CREATE DATABASE ZeldaDB;
USE ZeldaDB;

CREATE TABLE Game (
    GameId INT,
    UserName VARCHAR(255),
    DateStarted DATETIME,
    LastSaved DATETIME,
    PlayerMaxLife INT,
    PlayerCurrentLife INT,
    BloodMoon INT,
    BloodMoonAppearances INT,
    LastRegion ENUM("Hyrule","Death mountain","Gerudo","Necluda","Castle")
);

CREATE Table Food (
    GameId INT,
    FoodName ENUM("Vegetable","Fish","Meat","Salad","Pescatarian","Roasted"),
    FoodQuantity INT,
    TimesObtained INT,
    TimesConsumed INT
);

CREATE Table Weapons (
    GameId INT,
    WeaponName ENUM("Sword","Shield","Wood Sword","Wood Shield"),
    WeaponQuantity INT,
    WeaponDurability INT,
    Equiped BOOLEAN,
    TimesObtained INT,
    TimesUsed INT
);

CREATE Table Sanctuaries (
    GameId INT,
    SanctuaryId INT,
    Opened BOOLEAN
);

CREATE Table Enemies (
    GameId INT,
    Loacation ENUM("Hyrule","Death mountain","Gerudo","Necluda"),
    EnemyId INT,
    EnemyLife INT,
    PosX INT,
    PosY INT
);

CREATE Table Chests (
    GameId INT,
    Loacation ENUM("Hyrule","Death mountain","Gerudo","Necluda"),
    ChestId INT,
    Opened BOOLEAN
);