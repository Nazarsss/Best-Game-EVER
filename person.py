class Person:
    def __init__(self):
        self.__hp = None
        self.__damage = None
    @property
    def Hp(self):
        return self.__hp
    @hp.setter
    def Hp(self,hp):
        self.__hp = hp
    
    @property
    def Damage(self):
        return self.__damage
    @Damage.setter
    def Damage(self,damage):
        self.__damage = damage
    
    def fight(self,enemy):
        self.Hp -= enemy.Damage
        enemy.Hp -= self.Damage
