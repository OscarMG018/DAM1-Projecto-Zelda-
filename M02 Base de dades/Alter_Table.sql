
ALTER TABLE game ADD CONSTRAINT CKPlayerMaxLife CHECK (PlayerMaxLife > 0);
ALTER TABLE game ALTER COLUMN PlayerMaxLife SET DEFAULT 3;
ALTER TABLE game ADD CONSTRAINT CKPlayerCurrentLife CHECK (PlayerCurrentLife > 0 && PlayerCurrentLife <= PlayerMaxLife);
ALTER TABLE game ALTER COLUMN  PlayerCurrentLife SET DEFAULT 3;

ALTER TABLE food ADD CONSTRAINT CKFoodQuantity CHECK (FoodQuantity >= 0);
ALTER TABLE food ALTER COLUMN  FoodQuantity SET DEFAULT 0;
ALTER TABLE food ADD CONSTRAINT CKFoodTimesObtained CHECK (TimesObtained >= 0);
ALTER TABLE food ALTER COLUMN  TimesObtained SET DEFAULT 0;
ALTER TABLE food ADD CONSTRAINT CKFoodTTimesComsumed CHECK (TimesConsumed >= 0);
ALTER TABLE food ALTER COLUMN  TimesConsumed SET DEFAULT 0;

ALTER TABLE weapons ADD CONSTRAINT CKWeaponQuantity CHECK (WeaponQuantity >= 0);
ALTER TABLE weapons ALTER COLUMN  WeaponQuantity SET DEFAULT 0;
ALTER TABLE weapons ADD CONSTRAINT CKWeaponDurability CHECK (WeaponDurability >= 0);
ALTER TABLE weapons ALTER COLUMN  WeaponDurability SET DEFAULT 0;

ALTER TABLE weapons ALTER COLUMN Equiped SET DEFAULT false;

ALTER TABLE weapons ADD CONSTRAINT CKWeaponsTimesObtained CHECK (TimesObtained >= 0);
ALTER TABLE weapons ALTER COLUMN  TimesObtained SET DEFAULT 0;
ALTER TABLE weapons ADD CONSTRAINT CKWeaponsTimesUsed CHECK (TimesUsed >= 0);
ALTER TABLE weapons ALTER COLUMN  TimesUsed SET DEFAULT 0;

ALTER TABLE Sanctuaries ADD CONSTRAINT CKSanctuaryId CHECK (SanctuaryId >= 0);
ALTER TABLE Sanctuaries ALTER COLUMN Opened SET DEFAULT false;

ALTER TABLE Enemies ADD CONSTRAINT CKPosX CHECK (PosX >= 0);
ALTER TABLE Enemies ADD CONSTRAINT CKPosY CHECK (PosY >= 0);
ALTER TABLE Enemies ADD CONSTRAINT CKEnemyLife CHECK (EnemyLife >= 0);
ALTER TABLE Enemies ALTER COLUMN EnemyLife SET DEFAULT 1;
ALTER TABLE Enemies ADD CONSTRAINT CKEnemyId CHECK (EnemyId >= 0);

ALTER TABLE Chests ADD CONSTRAINT CKChestId CHECK (ChestId >= 0);
ALTER TABLE Chests ALTER COLUMN Opened SET DEFAULT false;

ALTER TABLE game ADD CONSTRAINT PKGame PRIMARY KEY (GameId);
ALTER TABLE food ADD CONSTRAINT PKFood PRIMARY KEY (GameId, FoodName);
ALTER TABLE weapons ADD CONSTRAINT PKWeapons PRIMARY KEY (GameId, WeaponName);
ALTER TABLE Sanctuaries ADD CONSTRAINT PKSanctuaries PRIMARY KEY (GameId, SanctuaryId);
ALTER TABLE Enemies ADD CONSTRAINT PKEnemies PRIMARY KEY (GameId, Loacation, EnemyId);
ALTER TABLE Chests ADD CONSTRAINT PKChests PRIMARY KEY (GameId, Loacation, ChestId);

ALTER TABLE food ADD CONSTRAINT FKFood FOREIGN KEY (GameId) REFERENCES game(GameId);
ALTER TABLE weapons ADD CONSTRAINT FKWeapons FOREIGN KEY (GameId) REFERENCES game(GameId);
ALTER TABLE Sanctuaries ADD CONSTRAINT FKSanctuaries FOREIGN KEY (GameId) REFERENCES game(GameId);
ALTER TABLE Enemies ADD CONSTRAINT FKEnemies FOREIGN KEY (GameId) REFERENCES game(GameId);
ALTER TABLE Chests ADD CONSTRAINT FKChests FOREIGN KEY (GameId) REFERENCES game(GameId);

ALTER TABLE game MODIFY UserName VARCHAR(255) NOT NULL;




