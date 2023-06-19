from menu import *
from combat import *
from events import *

player = Menu.createChar()
print("\nBienvenid@ a esta aventura " + player.race + " " + player.name)

while True:
    print("\nQue deseas hacer ahora " + player.name + "? ")
    print("1. Acceder al menú")
    print("2. Mazmorrear")
    print("3. Eventos\n")
    print("4. Salir\n")
    
    choice = int(input("Selecciona una opción: "))
    print("\n")

    if choice == 1:
        print("Bienvenid@ al Menú!")
        print("¿Que deseas hacer?\n")
        Menu.menu(player)
    elif choice == 2:
        enemy = Enemy.createEnemy()
        combat = Combat(player, enemy)
        combat.startBattle()
    elif choice == 3:
        generateEvent()
    elif choice == 4:
        break
    else:
        print("Opción inválida. Intente nuevamente.")