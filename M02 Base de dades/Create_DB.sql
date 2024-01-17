-- Active: 1698162559588@@127.0.0.1@3306

DROP DATABASE IF EXISTS ZeldaDB;
CREATE DATABASE ZeldaDB;
USE ZeldaDB;

CREATE TABLE Game (
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

CREATE Table Food (
    GameId INT NOT NULL,
    FoodName ENUM("Vegetable","Fish","Meat","Salad","Pescatarian","Roasted"),
    FoodQuantity INT,
    TimesObtained INT,
    TimesConsumed INT,
    PRIMARY KEY(GameId, FoodName),
    FOREIGN KEY(GameId) REFERENCES game(GameId)
);

CREATE Table Weapons (
    GameId INT NOT NULL,
    WeaponName ENUM("Sword","Shield","Wood Sword","Wood Shield"),
    WeaponQuantity INT,
    WeaponDurability INT,
    Equiped BOOLEAN,
    TimesObtained INT,
    TimesUsed INT,
    PRIMARY KEY(GameId, WeaponName),
    FOREIGN KEY(GameId) REFERENCES game(GameId)
);

CREATE Table Sanctuaries (
    GameId INT NOT NULL,
    SanctuaryId INT,
    Opened BOOLEAN,
    PRIMARY KEY(GameId, SanctuaryId),
    FOREIGN KEY(GameId) REFERENCES game(GameId)
);

CREATE Table Enemies (
    GameId INT NOT NULL,
    Loacation ENUM("Hyrule","Death mountain","Gerudo","Necluda"),
    EnemyId INT,
    EnemyLife INT,
    PosX INT,
    PosY INT,
    PRIMARY KEY(GameId, Loacation, EnemyId),
    FOREIGN KEY(GameId) REFERENCES game(GameId)
);

CREATE Table Chests (
    GameId INT NOT NULL,
    Loacation ENUM("Hyrule","Death mountain","Gerudo","Necluda"),
    ChestId INT NOT NULL,
    Opened BOOLEAN,
    PRIMARY KEY(GameId, Loacation, ChestId),
    FOREIGN KEY(GameId) REFERENCES game(GameId)
);

DELETE FROM Enemies;
DELETE FROM Food;
DELETE FROM Weapons;
DELETE FROM Sanctuaries;
DELETE FROM Chests;
DELETE FROM Game;


DELETE FROM enemies WHERE `GameId` = 2;
DELETE FROM food WHERE `GameId` = 2;
DELETE FROM weapons WHERE `GameId` = 2;
DELETE FROM sanctuaries WHERE `GameId` = 2;
DELETE FROM chests WHERE `GameId` = 2;
DELETE FROM game WHERE `GameId` = 2;

SELECT * From Game;
SELECT * FROM Food;
SELECT * FROM Weapons;
SELECT * FROM Sanctuaries;
SELECT * FROM Enemies;
SELECT * FROM Chests;

INSERT into game VALUES (1, "Juan", NOW(), NOW(), 100, 100, 0, 0, "Hyrule");


MItjana de blood moons de les partides
jugades.
● Dades de la partida on han aparegut més
blood moons, data partida, nom del jugador i
quantitat de blood moons.

SELECT avg(BloodMoonAppearances) from game;

SELECT * FROM game WHERE BloodMoonAppearances > (SELECT max(BloodMoonAppearances) from game);