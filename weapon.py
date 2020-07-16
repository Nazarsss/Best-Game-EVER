class Weapon:
    def __init__(self):
        self.__name = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
