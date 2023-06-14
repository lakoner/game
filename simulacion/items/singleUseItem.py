class SingleUseItem:
    def __init__(self, name, restoreHP=0, buffDamage=0, buffArmor=0):
        self.name = name
        self.restoreHP = restoreHP
        self.buffDamage = buffDamage
        self.buffArmor = buffArmor

    def get_item(self, item_id):
        return self.items.get(item_id)
    


potionLower = SingleUseItem("Poción Pequeña", restoreHP=3)
potion = SingleUseItem("Poción", restoreHP=5)
potionBigger = SingleUseItem("Poción Grande", restoreHP=8)
biscuite = SingleUseItem("Galleta", buffDamage=1, buffArmor=1)

