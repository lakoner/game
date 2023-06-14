class Weapon:
    def __init__(self, item_id, name, damage, hand):
        self.item_id = item_id
        self.name = name
        self.damage = damage
        self.hand = hand

def get_item(self, item_id):
        return self.items.get(item_id)


sword = Weapon(1, "Espada", 3, 1)
axe = Weapon(2, "Hacha", 5, 2)
greatSword = Weapon(3, "Espadón", 7, 2)
staff = Weapon(4, "Varita", 3, 1)
claws = Weapon(5, "Garras", 6, 2)
doll = Weapon(6, "Muñeca", 2, 1)
