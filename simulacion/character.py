from items.weapon import *
from items.armor import *
from items.singleUseItem import *
from race import *
from menu import *

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

    def __str__(self):
        return f"Nombre: {self.name}, Vida: {self.vitAct}, Vida Total: {self.vitMax}, Ataque: {self.attack}, Defensa: {self.armor}"
    
    def get_name(self):
        return self.name

    def get_race(self):
        return self.race

    def get_vitAct(self):
        return self.vitAct

    def get_vitMax(self):
        return self.vitMax

    def get_attack(self):
        return self.attack

    def get_armor(self):
        return self.armor

    def get_gold(self):
        return self.gold

    def get_exp(self):
        return self.exp

    def get_inventory(self):
        return self.inventory
    
    def set_name(self, name):
        self._name = name

    def set_race(self, race):
        self._race = race

    def set_vitAct(self, vitAct):
        self._vitAct = vitAct

    def set_vitMax(self, vitMax):
        self._vitMax = vitMax

    def set_attack(self, attack):
        self._attack = attack

    def set_armor(self, armor):
        self._armor = armor

    def set_gold(self, gold):
        self._gold = gold

    def set_exp(self, exp):
        self._exp = exp

    def set_inventory(self, inventory):
        self._inventory = inventory
        
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
        print("\nEquipo Actual: \n")
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

    def useSingleItemUse(self):
        print("Pocion")
       
