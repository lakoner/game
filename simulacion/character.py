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

    def __init__(self, name, race, level, vitAct, vitMax, attack, armor, speed, gold, exp, inventory):
        self.name = name
        self.race = race
        self.level = level
        self.vitAct = vitAct
        self.vitMax = vitMax
        self.attack = attack
        self.armor = armor
        self.speed = speed
        self.gold = gold
        self.exp = exp
        self.inventory = inventory

    def setCreateChar(self, name, race, vitAct, vitMax, attack, armor, speed, gold, exp, inventory):
        self.name = name
        self.race = race
        self.vitAct = vitAct
        self.vitMax = vitMax
        self.attack = attack
        self.armor = armor
        self.speed = speed
        self.gold = gold
        self.exp = exp
        self.inventory = inventory

    def __str__(self):
        return f"Nombre: {self.name}, Vida: {self.vitAct}, Vida Total: {self.vitMax}, Ataque: {self.attack}, Defensa: {self.armor}"
    
    def get_name(self):
        return self.name

    def get_race(self):
        return self.race

    def get_level(self):
        return self.level
    
    def get_vitAct(self):
        return self.vitAct

    def get_vitMax(self):
        return self.vitMax

    def get_attack(self):
        return self.attack

    def get_armor(self):
        return self.armor
    
    def get_speed(self):
        return self.speed

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
    
    def set_level(self, level):
        self._level = level

    def set_vitAct(self, vitAct):
        self._vitAct = vitAct

    def set_vitMax(self, vitMax):
        self._vitMax = vitMax

    def set_attack(self, attack):
        self._attack = attack

    def set_armor(self, armor):
        self._armor = armor

    def set_speed(self, speed):
        self.speed = speed

    def set_gold(self, gold):
        self._gold = gold

    def set_exp(self, exp):
        self._exp = exp

    def set_inventory(self, inventory):
        self._inventory = inventory
        
    def printStats(self):
        totalAttack, totalArmor = self.calculateStats()
        print("\nEstos son los stats de tu personaje: \n"
            "Nombre: "            + self.name               + "\n" +
            "Raza: "              + self.race               + "\n" +
            "Nivel: "             + str(self.level)         + "\n" +
            "Vitalidad Actual: "  + str(self.vitAct)        + "\n" +
            "Vitalidad Maxima: "  + str(self.vitMax)        + "\n" +
            "Ataque: "            + str(totalAttack)       + "\n" +
            "Armadura: "          + str(totalArmor)        + "\n" +
            "Velocidad: "         + str(self.speed)         + "\n" +
            "Oro: "               + str(self.gold)          + "\n" +
            "Experiencia: "       + str(self.exp) + "\n")
        
    def printInventario(self):
        print("\nEquipo Actual: \n")
        for item in self.inventory:
            if isinstance(item, Weapon):
                print("Nombre: " + item.name + " / Daño: " + str(item.damage))
            elif isinstance(item, Armor):
                print("Nombre: " + item.name + " / Armadura: " + str(item.armor))
            elif isinstance(item, SingleUseItem):
                details = f"Nombre: {item.name}"
                if item.buffArmor != 0:
                    details += f" / Bonus armadura: {item.buffArmor}"
                if item.buffDamage != 0:
                    details += f" / Bonus daño: {item.buffDamage}"
                if item.restoreHP != 0:
                    details += f" / Restaura HP: {item.restoreHP}"
                print(details)

    def calculateStats(self):
        totalAttack = self.attack
        totalArmor = self.armor

        for item in self.inventory:
            if isinstance(item, Weapon):
                totalAttack += item.damage
            elif isinstance(item, Armor):
                totalArmor += item.armor
        print(totalArmor, totalAttack)
        return totalAttack, totalArmor

    def restoreAll(self):
        self.vitAct = self.vitMax

    def useSingleItemUse(self):
        print("Lista de objetos: ")
        itemListToUse = []
        index = 1
        for item in self.inventory:
            if isinstance(item, SingleUseItem):
                print(f"{index}. {item.name}")
                itemListToUse.append(item)
                index += 1

        print("\n")
        useItem = input("¿Que objeto quieres usar (Ingresa el número)?")

        try:
            itemIndex = int(useItem) - 1
            if 0 <= itemIndex < len(itemListToUse):
                itemToUse = itemListToUse[itemIndex]
                if itemToUse.buffArmor != 0:
                    self.armor += itemToUse.buffArmor
                    print(f"Tienes {self.armor} de armadura")
                if itemToUse.buffDamage != 0:
                    self.attack += itemToUse.buffDamage
                    print(f"Tienes {self.attack} de ataque.")
                if itemToUse.restoreHP != 0:
                    self.vitAct += itemToUse.restoreHP
                    print(f"Tienes {self.vitAct} de HP.")
                self.inventory.remove(itemToUse)
            else:
                print("Número de objeto no válido.\n")
        except ValueError:
            print("Error, tienes que ingresar un digito.\n")

    print("\n")

    def checkLevelUp(self):
        totalExpToUp = 5 + (self.get_level() * 4) + self.get_level()
        if self.exp >= totalExpToUp:
            print("\nLevel UP!")
            self.level += 1
            print(f"has subido a nivel {self.level}")
            self.exp = self.exp - totalExpToUp
            print(f"Tienes {self.exp} de exp restante.")

    def checkIfDead(self):
        if self.vitAct <= 0:
            print("Has muerto.")
            print("Resucitando...")
            Person.restoreAll(self)
            self.level = 1
            self.exp = 0
            return True
        