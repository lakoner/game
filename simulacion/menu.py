from character import Person
from items.weapon import *
from items.armor import *
from race import *


class Menu:

    def createChar():
        print("\nSaludos, vamos a crear tu personaje para esta aventura. ")
        character = Person("", "", vitAct=10, vitMax=10, attack=1, armor=0, gold=0, exp=0, inventory=[])
        character.name = input("¿Cual será tu nombre?: ")
        character.vitMax = 10
        character.attack = 1 
        character.armor = 1 
        character.gold = 0
        character.exp = 0
        character.inventory = []

        while True:
            character.race = input("¿Qué raza eres? orco, humano, druida o demonio? ")
            if character.race == orc.race:
                character.vitMax += orc.vitMax
                character.attack += orc.attack
                character.armor += orc.armor
                character.inventory.append(axe)
                break
            elif character.race == human.race:
                character.vitMax += human.vitMax
                character.attack += human.attack
                character.armor += human.armor
                character.inventory.append(sword)
                character.inventory.append(shield)
                break
            elif character.race == druid.race:
                character.vitMax += druid.vitMax
                character.attack += druid.attack
                character.armor += druid.armor
                character.inventory.append(claws)
                break
            elif character.race == demon.race:
                character.vitMax += demon.vitMax
                character.attack += demon.attack
                character.armor += demon.armor
                character.inventory.append(staff)
                character.inventory.append(doll)
                break
            elif character.race == asshole.race:
                character.vitMax += asshole.vitMax
                character.attack += asshole.attack
                character.armor += asshole.armor
                break
            else:
                print("Raza no válida")

        character.restoreAll()
        character.setCreateChar(character.name, character.race, character.vitAct, character.vitMax, character.attack, character.armor, character.gold, character.exp, character.inventory)
        return character

    def menu(player):
        while True:
            print("\n")
            print("1. Ver estadísticas del personaje")
            print("2. Ver inventario del personaje")
            print("3. Usar objetos")
            print("4. Salir\n")
            choice = int(input("Seleccione una opción: "))
            
            if choice == 1:
                player.printStats()
            elif choice == 2:
                player.printInventario()
            elif choice == 3:
                print("en proceso")
            elif choice == 4:
                break
            else:
                print("Opción inválida. Intente nuevamente.")