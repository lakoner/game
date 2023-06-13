from items.weapon import *
from items.armor import *

class Person:
    name = ""
    race = ""
    vitAct = 0
    vitMax = 0
    attack = 0
    armor = 0
    gold = 0
    exp = 0
    inventory = []

    def __init__(self, name, race, vitAct, vitMax, attack, armor, gold, exp, inventory):
        self.name = name
        self.race = race
        self.vitAct = vitAct
        self.vitMax = vitMax
        self.attack = attack
        self.armor = armor
        self.gold = gold
        self.exp = exp
        self.inventory = inventory

    def setCreateChar(self, name, race, vitAct, vitMax, attack, armor, gold, exp, inventory):
        self.name = name
        self.race = race
        self.vitAct = vitAct
        self.vitMax = vitMax
        self.attack = attack
        self.armor = armor
        self.gold = gold
        self.exp = exp
        self.inventory = inventory

    def printStats(self):
        total_attack, total_armor = self.calculateStats()
        print("\nEstos son los stats de tu personaje: \n"
            "Nombre: "            + self.name               + "\n" +
            "Raza: "              + self.race               + "\n" +
            "Vitalidad Actual: "  + str(self.vitAct)        + "\n" +
            "Vitalidad Maxima: "  + str(self.vitMax)        + "\n" +
            "Ataque: "            + str(total_attack)       + "\n" +
            "Armadura: "          + str(total_armor)        + "\n" +
            "Oro: "               + str(self.gold)          + "\n" +
            "Experiencia: "       + str(self.exp))
        
    def printInventario(self):
        print("\nInventario: \n")
        for item in self.inventory:
            if isinstance(item, Weapon):
                print("Nombre: " + item.name + " / Daño: " + str(item.damage))
            elif isinstance(item, Armor):
                print("Nombre: " + item.name + " / Armadura: " + str(item.armor))

    def calculateStats(self):
        total_attack = self.attack
        total_armor = self.armor

        for item in self.inventory:
            if isinstance(item, Weapon):
                total_attack += item.damage
            elif isinstance(item, Armor):
                total_armor += item.armor
        print(total_armor, total_attack)
        return total_attack, total_armor

    def restoreAll(self):
        self.vitAct = self.vitMax

