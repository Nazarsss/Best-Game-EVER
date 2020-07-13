class Weapon:
    def __init__(self):
        self.__name = None
    @property 
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self,name):
        self.__name = name
    