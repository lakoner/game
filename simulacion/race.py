class Race:
    def __init__(self, race, vitMax, attack, armor):
        self.race = race
        self.vitMax = vitMax
        self.attack = attack
        self.armor = armor


orc = Race("orco", 3, 4, 3)
human = Race("humano", 4, 4, 2)
druid = Race("druida", 5, 2, 3)
demon = Race("demonio", 2, 6, 2)
asshole = Race("pringado", 1, 0, 0)
