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
            print(f"El enemigo recibe: {self.player.attack} de daño.")
            print(f"El enemigo tiene: {enemyHPAct} de HP.")
            if enemyHPAct <= 0:
                print("Has ganado!")
                print(f"Recibes {self.enemy.exp} de exp.")
                break
            vitAct -= self.enemy.attack
            print(f"Recibes: {self.enemy.get_attack()} de daño.")
            print(f"Tienes: {vitAct} de HP.")
            if vitAct <= 0:
                print("has muerto")
                break
            print("\nSiguiente ronda\n")

        
    



    
