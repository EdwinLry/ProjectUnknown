class Weapon:
    def __init__(self, name, weaponType, goldCost, dmg, Speed=None, ):
        self.name = name
        self.weaponType = weaponType
        self.goldCost = goldCost
        self.dmg = dmg
        self.Speed = Speed

        if (self.weaponType == "sword"):
            if (Speed == None):
                self.Speed = 3
            elif (Speed != None):
                self.Speed = Speed

        if (self.weaponType == "bow"):
            if (Speed == None):
                self.Speed = 2
            elif (Speed != None):
                self.Speed = Speed

        if (weaponType == "hammer"):
            if (Speed == None):
                self.Speed = 1
            elif (Speed != None):
                self.Speed = Speed

        if (weaponType == "staff"):
            if (Speed == None):
                self.Speed = 1
            elif (Speed != None):
                self.Speed = Speed

rustySword = Weapon(name="Rusty sword", weaponType = "sword", goldCost = 500 , dmg = 4)
trainingBow = Weapon(name="Training bow", weaponType = "bow", goldCost = 500 , dmg = 8)
wornWarhammer = Weapon(name="Worn warhammer", weaponType = "hammer", goldCost = 500 , dmg = 18)
vineStaff = Weapon(name= "Vine Staff", weaponType = "staff", goldCost = 750 , dmg = 10)

sturdySword = Weapon(name="Sturdy sword", weaponType = "sword", goldCost = 750, dmg = 8)
longBow = Weapon(name="Long bow", weaponType = "bow", goldCost = 750 , dmg = 12)
sturdyWarhammer = Weapon(name="Sturdy warhammer", weaponType = "hammer" ,goldCost = 750 , dmg = 24)

ironSword = Weapon(name="Iron Sword", weaponType = "sword", goldCost = 750 , dmg = 22)
softWoodBow = Weapon(name="Softwood bow", weaponType = "bow", goldCost = 750 , dmg = 28)
ironWarhammer = Weapon(name="Iron warhammer", weaponType = "hammer", goldCost = 750 , dmg = 38)

reinfocredIronSword = Weapon(name="Renfored Iron Sword",weaponType = "sword", goldCost = 750 , dmg = 30)
huntingBow = Weapon(name="Long bow", weaponType = "bow", goldCost = 750 , dmg = 36)
reinforcedIronWarhammer = Weapon(name="Reinforced Iron Warhammer",weaponType = "warhammer", goldCost = 750 , dmg = 45)
