-- Active: 1698162559588@@127.0.0.1@3306@projectodb

DROP DATABASE IF EXISTS ProjectoDB;
CREATE DATABASE ProjectoDB;
USE ProjectoDB;

DROP TABLE IF EXISTS game;
CREATE TABLE game (
    GameId INT AUTO_INCREMENT PRIMARY KEY,
    UserName VARCHAR(255) NOT NULL,
    DateStarted DATETIME,
    LastSaved DATETIME,
    PlayerMaxLife INT,
    PlayerCurrentLife INT,
    BloodMoon INT,
    BloodMoonAppearances INT,
    LastRegion ENUM("Hyrule","Death mountain","Gerudo","Necluda","Castle")
);

CREATE Table food (
    GameId INT NOT NULL,
    FoodName ENUM("Vegetable","Fish","Meat","Salad","Pescatarian","Roasted"),
    FoodQuantity INT,
    TimesObtained INT,
    TimesComsumed INT,
    PRIMARY KEY(GameId, FoodName),
    FOREIGN KEY(GameId) REFERENCES game(GameId)
);

CREATE Table weapons (
    GameId INT NOT NULL,
    WeaponName ENUM("Sword","Shield","Wood Sword","Wood Shield"),
    WeaponQuantity INT,
    WeaponDurability INT,
    Equiped BOOLEAN,
    TimesObtained INT,
    TimesUsed INT,
    PRIMARY KEY(GameId, WeaponName),
    FOREIGN KEY(GameId) REFERENCES game(GameId)
)

CREATE Table Sanctuaries (
    GameId INT NOT NULL,
    SanctuaryId INT,
    Opened BOOLEAN,
    PRIMARY KEY(GameId, SanctuaryId),
    FOREIGN KEY(GameId) REFERENCES game(GameId)
)

CREATE Table Enemies (
    GameId INT NOT NULL,
    Loacation ENUM("Hyrule","Death mountain","Gerudo","Necluda"),
    EnemyId INT,
    EnemyLife INT,
    PosX INT,
    PoxY INT,
    PRIMARY KEY(GameId, Loacation, EnemyId),
    FOREIGN KEY(GameId) REFERENCES game(GameId)
)

CREATE Table Chests (
    GameId INT NOT NULL,
    Loacation ENUM("Hyrule","Death mountain","Gerudo","Necluda"),
    ChestId INT NOT NULL,
    Opened BOOLEAN,
    PRIMARY KEY(GameId, Loacation, ChestId),
    FOREIGN KEY(GameId) REFERENCES game(GameId)
)

DELETE FROM enemies;
DELETE FROM food;
DELETE FROM weapons;
DELETE FROM sanctuaries;
DELETE FROM chests;
DELETE FROM game;

DELETE FROM enemies WHERE `GameId` = 2;
DELETE FROM food WHERE `GameId` = 2;
DELETE FROM weapons WHERE `GameId` = 2;
DELETE FROM sanctuaries WHERE `GameId` = 2;
DELETE FROM chests WHERE `GameId` = 2;
DELETE FROM game WHERE `GameId` = 2;

SELECT * From game;
SELECT * FROM food;
SELECT * FROM weapons;
SELECT * FROM Sanctuaries;
SELECT * FROM Enemies;
SELECT * FROM Chests;

UPDATE enemies SET `PoxY` = 2  WHERE `GameId` = 1 AND `Loacation` = "Hyrule" AND `EnemyId` = 1;

