from character import *
from enemy import *


class Combat:

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy


    def startBattle(self):
        print(self.player)
        print(self.enemy)
        print("\n")
        fasterPlayer = self.checkFasterFight()
        while not self.checkIfDead() or not Person.checkIfDead(self.player):
            if fasterPlayer:
                self.playerDoDamage()
                if self.checkIfDead():
                    Person.checkLevelUp(self.player)
                    break
                self.enemyDoDamage()
                Person.checkIfDead(self.player)
            else:
                self.enemyDoDamage()
                if Person.checkIfDead(self.player):
                    break
                self.playerDoDamage()
                if self.checkIfDead():
                    Person.checkLevelUp(self.player)
                    break

            print("\nSiguiente turno!\n")


    def checkIfDead(self):
        if self.enemy.vitAct <= 0:
            print(f"\nHas matado a {self.enemy.name}")
            print(f"Recibes {self.enemy.exp} de exp.")
            self.player.exp += self.enemy.exp
            print(f"Tienes {self.player.exp} de exp total.")
            oro = random.randint(0, 3)
            if oro != 0:
                print(f"Recibes {oro} de oro.")
                self.player.gold += oro
                print(f"Tienes {self.player.gold} de oro total.")
            return True


    def playerDoDamage(self):
        print("Golpeas!")
        print(f"\nEl enemigo recibe: {self.player.attack} de daño.")
        self.enemy.vitAct -= self.player.attack
        print(f"El enemigo tiene: {self.enemy.vitAct} de HP restante.")
        return self.enemy.vitAct      
    
    def enemyDoDamage(self):
        print("El enemigo golpea!")
        print(f"Recibes: {self.enemy.get_attack()} de daño.")
        self.player.vitAct -= self.enemy.attack
        print(f"Tienes: {self.player.vitAct} de HP.")
        return self.player.vitAct    

    def checkFasterFight(self):
        playerSpeed = self.player.speed
        enemySpeed = self.enemy.speed
        if playerSpeed >= enemySpeed:
            print(f"{self.player.name} empieza.")
            return True
        elif playerSpeed < enemySpeed:
            print(f"El enemigo {self.enemy.name} empieza.")
            return False