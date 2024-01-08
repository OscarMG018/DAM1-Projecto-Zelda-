CREATE TABLE game {
    GameId INT AUTO_INCREMENT PRIMARY KEY,
    UserName VARCHAR(255) NOT NULL,
    DateStarted DATE,
    LastSaved DATE,
    PlayerMaxLife INT,
    PlayerCurrentLife INT,
    BloodMoon INT,
    BloodMoonAppearances INT,
    LastRegion char(20) Values("Hyrules","Death mountain","Gerudo","Necluda","Castle")
}

CREATE Table food {
    GameId INT NOT NULL,
    FoodName VARCHAR(30) Values("Vegetable","Fish","Meat","Salad","Pescatarian","Roasted"),
    FoodQuantity INT,
    TimesObtained INT,
    TimesComsumed INT,
    PRIMARY KEY(GameId, FoodName),
    FOREIGN KEY(GameId) REFERENCES game(GameId)
}

CREATE Table weapons {
    GameId INT NOT NULL,
    WeaponName VARCHAR(30) Values("Sword","Shield","Wood Sword","Wood Shield"),
    WeaponQuantity INT,
    WeaponDurability INT
    TimesObtained INT,
    TimesUsed INT,
    PRIMARY KEY(GameId, WeaponName)
    FOREIGN KEY(GameId) REFERENCES game(GameId)
}

CREATE Table Sanctuaries {
    GameId INT NOT NULL,
    SanctuaryId INT,
    Opened BOOLEAN,
    PRIMARY KEY(GameId, SanctuaryId)
    FOREIGN KEY(GameId) REFERENCES game(GameId)
}

CREATE Table Enemies {
    GameId INT NOT NULL,
    EnemyId INT,
    EnemyLife INT,
    PosX INT,
    PoxY INT,
    PRIMARY KEY(GameId, EnemyId)
    FOREIGN KEY(GameId) REFERENCES game(GameId)
}

CREATE Table Chests {
    GameId INT NOT NULL,
    ChestId INT NOT NULL,
    Opened BOOLEAN,
    PRIMARY KEY(GameId, ChestId)
    FOREIGN KEY(GameId) REFERENCES game(GameId)
}