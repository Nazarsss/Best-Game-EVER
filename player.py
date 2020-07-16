from person import Person


class Player(Person):
    def __init__(self):
        super().__init__()
        self.__level = None

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        self.__level = level
