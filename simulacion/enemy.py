import random

class Enemy:
    def __init__(self, name, level, vitAct, vitMax, attack, armor, exp):
        self.name = name
        self.level = level
        self.vitAct = vitAct
        self.vitMax = vitMax
        self.attack = attack
        self.armor = armor
        self.exp = exp

    def __str__(self):
        return f"Enemigo: {self.name}, Vida: {self.vitMax}, Ataque: {self.attack}, Defensa: {self.armor}"
    
    def get_name(self):
        return self.name

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
    
    def get_exp(self):
        return self.exp

    def createEnemy():
        enemy = random.choice(enemys)
        return enemy
    
dog = Enemy("Perro", 1, 3, 3, 2, 1, 1)
crab = Enemy("Cangrejo", 1, 2, 2, 2, 2, 1)
rat = Enemy("Rata", 1, 1, 1, 4, 1, 1)
wildPig= Enemy("Jabalí", 2, 4, 4, 3, 4, 3)
eagle = Enemy("Aguila", 2, 3, 3, 5, 2, 3)
corruptedHuman = Enemy("Humano corrupto", 2, 3, 3, 3, 3, 2)
bear = Enemy("Oso", 3, 5, 5, 7, 4, 6)
cannibal = Enemy("Canibal", 3, 4, 4, 6, 4, 5)
alien = Enemy("Alien", 4, 6, 6, 5, 4, 6)
mutant = Enemy("Mutante", 4, 5, 5, 8, 8, 8)
boss = Enemy("Jefe", 5, 10, 10, 10, 10, 10)

enemys = [dog, crab, rat, wildPig, eagle, corruptedHuman, bear, cannibal, alien, mutant, boss]
