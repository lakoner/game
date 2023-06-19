from character import Person
from items.weapon import *
from items.armor import *
from items.singleUseItem import *
from race import *


class Menu:

    def createChar():
        print("\nSaludos, vamos a crear tu personaje para esta aventura. ")
        character = Person("", "", level=1, vitAct=10, vitMax=10, attack=1, armor=0, speed=1, gold=0, exp=0, inventory=[])
        character.name = input("¿Cual será tu nombre?: ")
        character.vitMax = 10
        character.attack = 1 
        character.armor = 1 
        character.gold = 0
        character.exp = 0
        character.inventory = []

        while True:
            character.race = input("¿Qué raza eres? orco, humano, druida o demonio? ")
            race_stats = {
                orc.race: {
                    "vitMax": orc.vitMax,
                    "attack": orc.attack,
                    "armor": orc.armor,
                    "items": [axe]
                },
                human.race: {
                    "vitMax": human.vitMax,
                    "attack": human.attack,
                    "armor": human.armor,
                    "items": [sword, shield]
                },
                druid.race: {
                    "vitMax": druid.vitMax,
                    "attack": druid.attack,
                    "armor": druid.armor,
                    "items": [claws]
                },
                demon.race: {
                    "vitMax": demon.vitMax,
                    "attack": demon.attack,
                    "armor": demon.armor,
                    "items": [staff, doll]
                },
                asshole.race: {
                    "vitMax": asshole.vitMax,
                    "attack": asshole.attack,
                    "armor": asshole.armor,
                    "items": []
                },
                hacker.race: {
                    "vitMax": hacker.vitMax,
                    "attack": hacker.attack,
                    "armor": hacker.armor,
                    "items": [greatSword, armor, biscuite, potionBigger, potion]
                }
            }

            if character.race in race_stats:
                stats = race_stats[character.race]
                character.vitMax += stats["vitMax"]
                character.attack += stats["attack"]
                character.armor += stats["armor"]
                character.inventory.extend(stats["items"])
                break
            else:
                print("Raza no válida")

        character.restoreAll()
        character.setCreateChar(character.name, character.race, character.vitAct, character.vitMax, character.attack, character.armor, character.speed, character.gold, character.exp, character.inventory)
        return character

    def menu(player):
        while True:
            print("1. Ver estadísticas del personaje")
            print("2. Ver inventario del personaje")
            print("3. Usar objetos")
            print("4. Salir\n")
            choice = int(input("Seleccione una opción: "))
            
            if choice == 1:
                player.printStats()
            elif choice == 2:
                player.printInventario()
                print("\n")
            elif choice == 3:
                player.useSingleItemUse()
            elif choice == 4:
                break
            else:
                print("Opción inválida. Intente nuevamente.")