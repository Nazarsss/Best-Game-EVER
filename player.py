class Player(Person):
    def __init__(self):
        super().__init__()
        self.__level = None
    @property
    def Level(self):
        return self.__level

    @Level.setter
    def Level(self, level):
        self.__level = level
    
