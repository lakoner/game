class Race:
    def __init__(self, race, vitMax, attack, armor, speed):
        self.race = race
        self.vitMax = vitMax
        self.attack = attack
        self.armor = armor
        self.speed = speed


orc = Race("orco", 4, 4, 3, 3)
human = Race("humano", 3, 3, 2, 5)
druid = Race("druida", 5, 2, 3, 3)
demon = Race("demonio", 2, 6, 2, 4)
asshole = Race("pringado", 1, 0, 0, 0)
hacker = Race("hacker", 20, 20, 20, 20)
