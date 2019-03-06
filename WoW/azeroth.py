class AzerothCitizen:
    """
    Creates a citizen of Azeroth
    """
    # class constant attributes
    ALLEGIANCE = ("The Horde", "The Alliance", "The Burning Legion", "Neutral")
    JOBS = ("Warrior", "Mage", "Hunter", "Rogue", "Warlock", "Priest", "Druid", "Shaman", "Paladin", "NPC")
    RACE = ("Orc", "Human", "Troll", "Undead", "Gnome", "Tauren", "Night Elf", "Other")
    SEX = ("Male", "Female")

    def __init__(self, name: str, race: RACE, sex: SEX, job: JOBS):
        self._name = name
        # race value must be in RACE
        if race not in self.RACE:
            raise ValueError(f"race must be one of these {self.RACE}")
        else:
            self._race = race

        self.job = job
        self.sex = sex
    #__repr__ should be unambigous, this will help developer/us to debug code
    def __repr__(self):
        return f"{self.__class__.__name__}({self._name}, {self._race}, {self.job}, {self.sex})"

    def battle_cry(self):
        return f"{self._name} yells: Charge!!"

    def get_name(self):
        return self._name



class Orc(AzerothCitizen):
    """
    Creates Azeroth Citizen Orc
    """
    def __init__(self, name: str, sex: str, job: str):

        # _denotes class private variable - Python does not enforce, but rather it is convention
        self._allegiance = "The Horde"
        super().__init__(name, "Orc", sex, job)
    def __repr__(self):
        return f"{self.__class__.__name__} class instance - ({self._name}, {self._race}, {self.job}, {self._allegiance})"

    def battle_cry(self):
        return f"{self.get_name()} yells: FOR THE HORDE!!"

    @classmethod
    def thrall(cls):
        return cls("Thrall", "Male", "Shaman")

class Human(AzerothCitizen):
    """
    Creates Azeroth Citizen Human
    """
    def __init__(self, name: str, sex: str, job: str):
        self._allegiance = "The Alliance"
        super().__init__(name, "Human", sex, job)
    def __repr__(self):
        return f"{self.__class__.__name__} class instance - ({self._name}, {self._race}, {self.job}, {self._allegiance})"

    def battle_cry(self):
        return f"{self.get_name()} yells: FOR THE ALLIANCE!!"

    @classmethod
    def jaina(cls):
        return cls("Jaina", "Female", "Mage")

class Leader(AzerothCitizen):
    """
    Creates a Azeroth Citizen Leader
    """
    def __init(self, name: str, race: str, job: str, allegance: str, tribe: str):
        self.tribe=tribe
        super().__init__(name, race, sex, job, allegiance)

    def __repr__(self):
        return f"{self.__class__.__name__} class instance ({self._name}, {self._race}, {self.allegiance}, {self.tribe})"






if __name__ == "__main__":

    thrall = Orc.thrall()
    print(thrall)
    print(thrall.battle_cry())

    jaina = Human.jaina()
    print(jaina)
    print(jaina.battle_cry())


