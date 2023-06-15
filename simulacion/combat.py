from character import *
from enemy import *


class Combat:

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy


    def peleaPlayer(self):
        print(self.player)
        print(self.enemy)
        enemyHPAct = self.enemy.get_vitAct()
        vitAct = self.player.get_vitAct()

        while True:
            enemyHPAct -= self.player.attack
            print(f"\nEl enemigo recibe: {self.player.attack} de daño.")
            print(f"El enemigo tiene: {enemyHPAct} de HP.")
            if enemyHPAct <= 0:
                print("\nHas ganado!\n")
                print(f"Recibes {self.enemy.exp} de exp.")
                oro = random.randint(0, 3)
                print(f"Recibes {oro} de oro.\n")
                self.player.vitAct = vitAct
                print(f"Tienes {self.player.get_vitAct()} de HP restante.")
                self.player.exp += self.enemy.exp
                print(f"Tienes {self.player.exp} de exp total.")
                self.player.gold += oro
                print(f"Tienes {self.player.gold} de oro total.")
                break
            vitAct -= self.enemy.attack
            print(f"Recibes: {self.enemy.get_attack()} de daño.")
            print(f"Tienes: {vitAct} de HP.")
            if vitAct <= 0:
                print("has muerto")
                print("restaurando toda la HP.")
                Person.restoreAll(self.player)
                break
            print("\nSiguiente ronda\n")

        
    



    
