class Person:
    def __init__(self):
        self.__hp = None
        self.__damage = None

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, hp):
        self.__hp = hp

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, damage):
        self.__damage = damage

    def fight(self, enemy):
        self.hp -= enemy.Damage
        enemy.Hp -= self.damage
