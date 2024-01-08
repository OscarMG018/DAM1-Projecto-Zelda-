ALTER TABLE game ADD CONSTRAINT PlayerMaxLife CHECK (PlayerMaxLife > 0);
ALTER TABLE game ADD CONSTRAINT PlayerMaxLife DEFAULT (PlayerMaxLife = 3);
ALTER TABLE game ADD CONSTRAINT PlayerCurrentLife CHECK (PlayerCurrentLife > 0 && PlayerCurrentLife <= PlayerMaxLife);
ALTER TABLE game ADD CONSTRAINT PlayerCurrentLife DEFAULT (PlayerCurrentLife = 3);


ALTER TABLE food ADD CONSTRAINT FoodQuantity CHECK (FoodQuantity >= 0);
ALTER TABLE food ADD CONSTRAINT FoodQuantity DEFAULT (FoodQuantity = 0);
ALTER TABLE food ADD CONSTRAINT TimesObtaines CHECK (TimesObtaines >= 0);
ALTER TABLE food ADD CONSTRAINT TimesObtaines DEFAULT (TimesObtaines = 0);
ALTER TABLE food ADD CONSTRAINT TimesComsumed CHECK (TimesComsumed >= 0);
ALTER TABLE food ADD CONSTRAINT TimesComsumed DEFAULT (TimesComsumed = 0);


ALTER TABLE weapons ADD CONSTRAINT WeaponQuantity CHECK (WeaponQuantity >= 0);
ALTER TABLE weapons ADD CONSTRAINT WeaponQuantity DEFAULT (WeaponQuantity = 0);
ALTER TABLE weapons ADD CONSTRAINT WeaponDurability CHECK (WeaponDurability >= 0);
ALTER TABLE weapons ADD CONSTRAINT WeaponDurability DEFAULT (WeaponDurability = 0);


ALTER TABLE weapons ADD CONSTRAINT TimesObtaines CHECK (TimesObtaines >= 0);
ALTER TABLE weapons ADD CONSTRAINT TimesObtaines DEFAULT (TimesObtaines = 0);
ALTER TABLE weapons ADD CONSTRAINT TimesUsed CHECK (TimesUsed >= 0);
ALTER TABLE weapons ADD CONSTRAINT TimesUsed DEFAULT (TimesUsed = 0);


ALTER TABLE Sanctuaries ADD CONSTRAINT SanctuaryId CHECK (SanctuaryId >= 0);
ALTER TABLE Sanctuaries ADD CONSTRAINT Opened DEFAULT (Opened = false);


ALTER TABLE Enemies ADD CONSTRAINT PosX CHECK (PosX >= 0);
ALTER TABLE Enemies ADD CONSTRAINT PosY CHECK (PosY >= 0);
ALTER TABLE Enemies ADD CONSTRAINT EnemyLife CHECK (EnemyLife >= 0);
ALTER TABLE Enemies ADD CONSTRAINT EnemyLife DEFAULT (EnemyLife = 1);
ALTER TABLE Enemies ADD CONSTRAINT EnemyId CHECK (EnemyId >= 0);


ALTER TABLE Chests ADD CONSTRAINT ChestId CHECK (ChestId >= 0);
ALTER TABLE Chests ADD CONSTRAINT Opened DEFAULT (Opened = false);